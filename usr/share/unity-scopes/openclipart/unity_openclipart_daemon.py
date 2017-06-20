#! /usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright(C) 2013 Canonical, ltd.
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3, as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Unity, UnityExtras
from gi.repository import Gio, GLib
import urllib
import feedparser
import gettext
import shutil

APP_NAME = 'unity-scope-openclipart'
LOCAL_PATH = '/usr/share/locale/'
gettext.bindtextdomain(APP_NAME, LOCAL_PATH)
gettext.textdomain(APP_NAME)
_ = gettext.gettext

GROUP_NAME = 'com.canonical.Unity.Scope.Graphics.Openclipart'
UNIQUE_PATH = '/com/canonical/unity/scope/graphics/openclipart'
SEARCH_URI = 'https://openclipart.org/'
SEARCH_HINT = _('Search OpenClipArt')
NO_RESULTS_HINT = _('Sorry, there are no OpenClipArt results that match your search.')
PROVIDER_CREDITS = _('Powered by OpenClipArt')
SVG_DIR = '/usr/share/icons/unity-icon-theme/places/svg/'
PROVIDER_ICON = SVG_DIR+'service-openclipart.svg'
DEFAULT_RESULT_ICON = SVG_DIR+'result-graphics.svg'
DEFAULT_RESULT_MIMETYPE = 'text/html'
DEFAULT_RESULT_TYPE = Unity.ResultType.DEFAULT

c1 = {'id'      :'top',
      'name'    :_('Images'),
      'icon'    :SVG_DIR+'group-installed.svg',
      'renderer':Unity.CategoryRenderer.VERTICAL_TILE}
CATEGORIES = [c1]

FILTERS = []

m1 = {'id'   :'published',
      'type' :'s',
      'field':Unity.SchemaFieldType.OPTIONAL}
m2 = {'id'   :'author',
      'type' :'s',
      'field':Unity.SchemaFieldType.OPTIONAL}
m3 = {'id'   :'resource',
      'type' :'s',
      'field':Unity.SchemaFieldType.OPTIONAL}
EXTRA_METADATA = [m1, m2, m3]

def search(search, filters):
    '''
    Any search method returning results as a list of tuples.
    Available tuple fields:
    uri (string)
    icon (string)
    title (string)
    comment (string)
    dnd_uri (string)
    mimetype (string)
    category (int)
    result_type (Unity ResultType)
    extras metadata fields (variant)
    '''
    results = []
    if not search:
        return results
    search = urllib.parse.quote(search)
    uri = "%sapi/search/?query=%s" % (SEARCH_URI, search)
    print(uri)
    try:
        feed = feedparser.parse(uri)
    except Exception as error:
        print(error)
        feed = None
    if not feed or not 'entries' in feed:
        return results
    for f in feed['entries']:
        try:
            if f is None:
                continue
            resource = ''
            for link in f['links']:
                if link['rel'] == 'enclosure':
                    resource = link['href']
            if 'published' not in f:
                # support feedparser == 5.1
                published = f['updated']
            else:
                published = f['published']
            results.append({'uri':f['link'],
                            'icon':f['media_thumbnail'][0]['url'],
                            'title':f['title'],
                            'comment':f['summary'],
                            'published':published,
                            'author':f['author'],
                            'resource':resource})
        except Exception as error:
            print(error)
    return results



# Classes below this point establish communication
# with Unity, you probably shouldn't modify them.


class MySearch (Unity.ScopeSearchBase):
    def __init__(self, search_context):
        super (MySearch, self).__init__()
        self.set_search_context (search_context)

    def do_run (self):
        '''
        Adds results to the model
        '''
        try:
            result_set = self.search_context.result_set
            for i in search(self.search_context.search_query,
                            self.search_context.filter_state):
                if not 'uri' in i or not i['uri'] or i['uri'] == '':
                    continue
                if not 'icon' in i or not i['icon'] or i['icon'] == '':
                    i['icon'] = DEFAULT_RESULT_ICON
                if not 'mimetype' in i or not i['mimetype'] or i['mimetype'] == '':
                    i['mimetype'] = DEFAULT_RESULT_MIMETYPE
                if not 'result_type' in i or not i['result_type'] or i['result_type'] == '':
                    i['result_type'] = DEFAULT_RESULT_TYPE
                if not 'category' in i or not i['category'] or i['category'] == '':
                    i['category'] = 0
                if not 'title' in i or not i['title']:
                    i['title'] = ''
                if not 'comment' in i or not i['comment']:
                    i['comment'] = ''
                if not 'dnd_uri' in i or not i['dnd_uri'] or i['dnd_uri'] == '':
                    i['dnd_uri'] = i['uri']
                result_set.add_result(**i)
        except Exception as error:
            print (error)

class Preview (Unity.ResultPreviewer):

    def do_run(self):
        resource = False
        if self.result.metadata and 'resource' in self.result.metadata and self.result.metadata['resource'].get_string() != '':
            resource = True
            thumb = Gio.FileIcon.new(Gio.file_new_for_uri(self.result.metadata['resource'].get_string()))
        else:
            thumb = Gio.FileIcon.new(Gio.file_new_for_uri(self.result.icon_hint))
        preview = Unity.GenericPreview.new(self.result.title, self.result.comment.strip(), thumb)
        preview.add_info(Unity.InfoHint.new("license", _("License"), None, _("Public Domain")))
        if self.result.metadata and 'author' in self.result.metadata and self.result.metadata['author'].get_string() != '':
            preview.props.subtitle = _("By ") + self.result.metadata['author'].get_string()
        icon = Gio.FileIcon.new (Gio.file_new_for_path(PROVIDER_ICON))
        view_action = Unity.PreviewAction.new("view", _("View"), icon)
        preview.add_action(view_action)

        if resource and shutil.which("inkscape"):
            inkscape_action = Unity.PreviewAction.new("inkscape", _("Open in Inkscape"), None)
            preview.add_action(inkscape_action)
        return preview

class Scope (Unity.AbstractScope):
    def __init__(self):
        Unity.AbstractScope.__init__(self)

    def do_get_search_hint (self):
        return SEARCH_HINT

    def do_get_schema (self):
        '''
        Adds specific metadata fields
        '''
        schema = Unity.Schema.new ()
        if EXTRA_METADATA:
            for m in EXTRA_METADATA:
                schema.add_field(m['id'], m['type'], m['field'])
        #FIXME should be REQUIRED for credits
        schema.add_field('provider_credits', 's', Unity.SchemaFieldType.OPTIONAL)
        return schema

    def do_get_categories (self):
        '''
        Adds categories
        '''
        cs = Unity.CategorySet.new ()
        if CATEGORIES:
            for c in CATEGORIES:
                cat = Unity.Category.new (c['id'], c['name'],
                                          Gio.ThemedIcon.new(c['icon']),
                                          c['renderer'])
                cs.add (cat)
        return cs

    def do_get_filters (self):
        '''
        Adds filters
        '''
        fs = Unity.FilterSet.new ()
#        if FILTERS:
#
        return fs

    def do_get_group_name (self):
        return GROUP_NAME

    def do_get_unique_name (self):
        return UNIQUE_PATH

    def do_create_search_for_query (self, search_context):
        se = MySearch (search_context)
        return se

    def do_create_previewer(self, result, metadata):
        rp = Preview()
        rp.set_scope_result(result)
        rp.set_search_metadata(metadata)
        return rp

    def do_activate(self, result, metadata, id):
        if id == 'inkscape':
            uri = Gio.file_new_for_uri(result.metadata['resource'].get_string()).get_uri()
            GLib.spawn_async([shutil.which("inkscape"), uri.replace(' ', '%20')])
            return Unity.ActivationResponse(handled=Unity.HandledType.HIDE_DASH, goto_uri=None)
        return Unity.ActivationResponse()

def load_scope():
    return Scope()