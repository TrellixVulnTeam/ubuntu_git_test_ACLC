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

from gi.repository import Unity
from gi.repository import Gio, GLib
import gettext
import datetime
import re
import urllib.parse
import urllib.request

APP_NAME = 'unity-scope-tomboy'
LOCAL_PATH = '/usr/share/locale/'
gettext.bindtextdomain(APP_NAME, LOCAL_PATH)
gettext.textdomain(APP_NAME)
_ = gettext.gettext

GROUP_NAME = 'com.canonical.Unity.Scope.Notes.Tomboy'
UNIQUE_PATH = '/com/canonical/unity/scope/notes/tomboy'
SEARCH_URI = ''
SEARCH_HINT = _('Search Tomboy notes')
NO_RESULTS_HINT = _('Sorry, there are no Tomboy notes that match your search.')
PROVIDER_CREDITS = _('Powered by Tomboy')
SVG_DIR = '/usr/share/icons/unity-icon-theme/places/svg/'
PROVIDER_ICON = SVG_DIR+'service-tomboy.svg'
DEFAULT_RESULT_ICON = 'tomboy'
DEFAULT_RESULT_MIMETYPE = 'application/x-desktop'
DEFAULT_RESULT_TYPE = Unity.ResultType.PERSONAL

c1 = {'id'      :'recent',
      'name'    :_('Notes'),
      'icon'    :SVG_DIR+'group-notes.svg',
      'renderer':Unity.CategoryRenderer.VERTICAL_TILE}
CATEGORIES = [c1]

FILTERS = []

m1 = {'id'   :'last_changed',
      'type' :'s',
      'field':Unity.SchemaFieldType.OPTIONAL}
m2 = {'id'   :'tags',
      'type' :'s',
      'field':Unity.SchemaFieldType.OPTIONAL}
EXTRA_METADATA = [m1, m2]

def get_dbus(name, path, iface):
    try:
        session_bus = Gio.bus_get_sync (Gio.BusType.SESSION, None)
        return Gio.DBusProxy.new_sync ( session_bus, 0, None,
                                        name, path, iface, None)
    except Exception as error:
        print (error)
        return None

tomboy = get_dbus('org.gnome.Tomboy',
                  '/org/gnome/Tomboy/RemoteControl',
                  'org.gnome.Tomboy.RemoteControl')

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
    if not tomboy:
        return results
    if search:
        tomboy_search = tomboy.SearchNotes('(sb)', search, False)
    else:
        tomboy_search = tomboy.ListAllNotes()
    for note in tomboy_search:
        timestamp = tomboy.GetNoteChangeDate('(s)', note)
        last_changed = datetime.datetime.fromtimestamp(timestamp).strftime('%x')
        # Has anyone ever seen Tomboy tags?
        try:
            tags = ','.join(tomboy.GetTagsForNote('(s)', note))
        except Exception as error:
            print(error)
            tags = ''
        results.append({'uri':note,
                        'title':tomboy.GetNoteTitle('(s)', note),
                        'comment':tomboy.GetNoteContents('(s)', note),
                        'last_changed':GLib.Variant('s',last_changed),
                        'tags':GLib.Variant('s',tags)})
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
        preview = Unity.GenericPreview.new(self.result.title, self.result.comment.strip(), None)
        image = None
        try:
            link_search = re.search('https?://[^\s]*(\"|\'|\s|$)', self.result.comment.strip(), re.IGNORECASE)
            if link_search:
                link = urllib.request.urlopen(link_search.group(0)).read().decode('utf-8')
                image_search = re.search('https?://[^\s]*\.(jpg|png|gif)', link, re.IGNORECASE)
                if image_search:
                    image = image_search.group(0)
        except Exception as error:
            print (error)
        try:
            link_search = re.search('https?://.*\.(jpg|png|gif)', self.result.comment.strip(), re.IGNORECASE)
            if link_search:
                    image = link_search.group(0)
        except Exception as error:
            print (error)
        if image:
            im = Gio.FileIcon.new(Gio.file_new_for_uri(image))
            preview.props.image = im
        if self.result.metadata and 'last_changed' in self.result.metadata and self.result.metadata['last_changed'].get_string() != '':
            preview.props.subtitle = self.result.metadata['last_changed'].get_string()
        view_action = Unity.PreviewAction.new("view", _("Edit"), None)
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
        tomboy = get_dbus('org.gnome.Tomboy',
                  '/org/gnome/Tomboy/RemoteControl',
                  'org.gnome.Tomboy.RemoteControl')
        tomboy.DisplayNote('(s)', result.uri)
        return Unity.ActivationResponse(handled=Unity.HandledType.HIDE_DASH, goto_uri=None)

def load_scope():
    return Scope()
