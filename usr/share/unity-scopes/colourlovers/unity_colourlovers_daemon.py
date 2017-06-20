#! /usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2013 David Callé <davidc@framli.eu>
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
import urllib.parse
import urllib.request
import json
import gettext
import os
import datetime

APP_NAME = 'unity-scope-colourlovers'
LOCAL_PATH = '/usr/share/locale/'
gettext.bindtextdomain(APP_NAME, LOCAL_PATH)
gettext.textdomain(APP_NAME)
_ = gettext.gettext

CACHE = "%s/unity-scope-colourlovers/" % GLib.get_user_cache_dir()
GROUP_NAME = 'com.canonical.Unity.Scope.Graphics.Colourlovers'
UNIQUE_PATH = '/com/canonical/unity/scope/graphics/colourlovers'
SEARCH_URI = "https://www.colourlovers.com/"
SEARCH_HINT = _('Search COLOURlovers palettes, patterns and colors')
NO_RESULTS_HINT = _('Sorry, there are no COLOURlovers results that match your search.')
PROVIDER_CREDITS = _('Powered by COLOURlovers')
SVG_DIR = '/usr/share/icons/unity-icon-theme/places/svg/'
PROVIDER_ICON = SVG_DIR+'service-colourlovers.svg'
DEFAULT_RESULT_ICON = SVG_DIR+'result-graphics.svg'
DEFAULT_RESULT_MIMETYPE = 'text/html'
DEFAULT_RESULT_TYPE = Unity.ResultType.DEFAULT

c1 = {'id'      :'top',
      'name'    :_('Colours'),
      'icon'    :SVG_DIR+'group-graphics.svg',
      'renderer':Unity.CategoryRenderer.VERTICAL_TILE}
CATEGORIES = [c1]

FILTERS = []

m1 = {'id'   :'description',
      'type' :'s',
      'field':Unity.SchemaFieldType.OPTIONAL}
m2 = {'id'   :'comment_nb',
      'type' :'s',
      'field':Unity.SchemaFieldType.OPTIONAL}
m3 = {'id'   :'rating',
      'type' :'s',
      'field':Unity.SchemaFieldType.OPTIONAL}
m4 = {'id'   :'date_created',
      'type' :'s',
      'field':Unity.SchemaFieldType.OPTIONAL}
EXTRA_METADATA = [m1, m2, m3, m4]

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
    if not search or len(search) < 2:
        return results
    search = urllib.parse.quote(search)
    for cat in ['patterns']:
        uri = '%sapi/%s?format=json&keywords=%s' % (SEARCH_URI, cat,search)
        try:
            req = urllib.request.Request(uri, headers={'User-Agent' : "Magic Browser"})
            response = urllib.request.urlopen(req).read()
            data = json.loads(response.decode('utf-8'))
        except Exception as error:
            print(error)
            data = None
        if not data:
            return results
        for d in data:
            results.append({'uri':d['url'],
                            'icon':d['imageUrl'],
                            'title':d['title'],
                            'comment':d['userName'],
                            'description':d['description'],
                            'rating':str(d['numHearts']),
                            'date_created':str(d['dateCreated']),
                            'comment_nb':str(d['numComments'])})
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
                i['provider_credits'] = GLib.Variant('s', PROVIDER_CREDITS)
                result_set.add_result(**i)
        except Exception as error:
            print (error)

class Preview (Unity.ResultPreviewer):

    def do_run(self):
        if self.result.metadata and 'description' in self.result.metadata and self.result.metadata['description'].get_string() != '':
            description = self.result.metadata['description'].get_string()
        else:
            description = ''
        preview = Unity.GenericPreview.new(self.result.title, description.strip(), None)
        preview.props.subtitle = _("By ") + self.result.comment
        preview.props.image_source_uri = self.result.icon_hint
        if self.result.metadata and 'date_created' in self.result.metadata and self.result.metadata['date_created'].get_string() != '':
            # Format date
            date = datetime.datetime.strptime(self.result.metadata['date_created'].get_string(), '%Y-%m-%d %H:%M:%S')
            translated_date = date.strftime('%x')
            preview.add_info(Unity.InfoHint.new("date_created", _("Created"), None, translated_date))
        if self.result.metadata and 'comment_nb' in self.result.metadata and self.result.metadata['comment_nb'].get_string() != '':
            preview.add_info(Unity.InfoHint.new("comment_nb", _("Comments"), None, self.result.metadata['comment_nb'].get_string()))
        if self.result.metadata and 'rating' in self.result.metadata and self.result.metadata['rating'].get_string() != '':
            # Create hearts rating
            fullhearts = int(float(self.result.metadata['rating'].get_string())) * "\u2665"
            emptyhearts = (5 - int(float(self.result.metadata['rating'].get_string()))) * "\u2661"
            if self.result.metadata['rating'].get_string() != '0':
                preview.add_info(Unity.InfoHint.new("rating", _("Rating"), None, fullhearts+emptyhearts))
        if "/patterns/" in self.result.icon_hint:
            wallpaper_action = Unity.PreviewAction.new("wallpaper", _("Set as wallpaper"), None)
            preview.add_action(wallpaper_action)
        icon = Gio.FileIcon.new (Gio.file_new_for_path(PROVIDER_ICON))
        view_action = Unity.PreviewAction.new("view", _("View"), icon)
        preview.add_action(view_action)
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
        if id == 'wallpaper':
            self.wallpaper_action(result.icon_hint)
            return Unity.ActivationResponse(handled=Unity.HandledType.SHOW_DASH, goto_uri=None)
        return Unity.ActivationResponse()

    def wallpaper_action(self, image):
        pattern_name = image.split('/')[-1]
        local_path = os.path.join(CACHE, pattern_name)
        if not os.path.isfile(local_path):
            if not os.path.isdir(CACHE):
                os.makedirs(CACHE)
            urllib.request.urlretrieve(image, local_path)
        self.set_as_wallpaper(local_path)
        return

    def set_as_wallpaper(self, pattern):
        gsettings = Gio.Settings.new('org.gnome.desktop.background')
        gsettings.set_string('picture-uri', "file://" + pattern)
        gsettings.set_string('picture-options', "wallpaper")
        gsettings.apply()

def load_scope():
    return Scope()
