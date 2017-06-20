#! /usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright(C) 2013 Mark Tully <markjtully@gmail.com>
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

import gettext
import html
import locale
import os
from xml.etree import cElementTree as ET

from gi.repository import GLib, Gio
from gi.repository import Unity

APP_NAME = 'unity-scope-yelp'
LOCAL_PATH = '/usr/share/locale/'
locale.setlocale(locale.LC_ALL, '')
gettext.bindtextdomain(APP_NAME, LOCAL_PATH)
gettext.textdomain(APP_NAME)
_ = gettext.gettext

GROUP_NAME = 'com.canonical.Unity.Scope.Help.Yelp'
UNIQUE_PATH = '/com/canonical/unity/scope/help/yelp'

SEARCH_HINT = _('Ubuntu Help')
NO_RESULTS_HINT = _('Sorry, there are no Ubuntu Help results that match your search.')
PROVIDER_CREDITS = _('')
SVG_DIR = '/usr/share/icons/unity-icon-theme/places/svg/'
PROVIDER_ICON = SVG_DIR + 'service-yelp.svg'
DEFAULT_RESULT_ICON = SVG_DIR + 'result-help.svg'
DEFAULT_RESULT_MIMETYPE = 'text/html'
DEFAULT_RESULT_TYPE = Unity.ResultType.DEFAULT
HELP_DIR = "/usr/share/help/"
YELP_CACHE = None
MAX_RESULTS = 25
YELP_EXECUTABLE = '/usr/bin/yelp'

c1 = {'id': 'help',
      'name': _('Official Help Documents'),
      'icon': SVG_DIR + 'group-installed.svg',
      'renderer': Unity.CategoryRenderer.VERTICAL_TILE}
CATEGORIES = [c1]

FILTERS = []
m1 = {'id'   :'manual',
      'type' :'s',
      'field':Unity.SchemaFieldType.OPTIONAL}
EXTRA_METADATA = [m1]


def _get_manuals_in_dir(dir, manuals):
    """Yield the manuals found in the given directory, omitting those
    that have already been discovered."""
    if not os.path.isdir(dir):
        return
    for manual in os.listdir(dir):
        if manual in manuals:
            continue
        manualdir = os.path.join(dir, manual)
        if os.path.isdir(manualdir):
            manuals.add(manual)
            yield manualdir


def get_manuals(helpdir):
    """Get the manuals found in the given directory according to the
    user's locale."""
    language, encoding = locale.getlocale()
    manuals = set()
    if language is not None:
        languagedir = os.path.join(helpdir, language)
        yield from _get_manuals_in_dir(languagedir, manuals)
        # If the locale includes a country, look for manuals 
        if language[:2] != language:
            languagedir = os.path.join(helpdir, language[:2])
            yield from _get_manuals_in_dir(languagedir, manuals)
    # Now return untranslated versions of remaining manuals.
    languagedir = os.path.join(helpdir, 'C')
    yield from _get_manuals_in_dir(languagedir, manuals)


def get_yelp_documents():
    '''
     Parses local help files for <desc> and 1st <title> tags and associates
    them with the page's uri in self.data as: {uri, page description, page title}
    If a help file has no <desc> or <title> tag, it is excluded.
    '''
    data = []
    namespaces = {'m': 'http://projectmallard.org/1.0/'}
    for manualdir in get_manuals(HELP_DIR):
        for filename in os.listdir(manualdir):
            filename = os.path.join(manualdir, filename)
            if not (filename.endswith('page') and os.path.isfile(filename)):
                continue
            try:
                tree = ET.parse(filename)
            except ET.ParseError:
                # Not an XML file
                continue
            if (tree.getroot().tag != '{http://projectmallard.org/1.0/}page' or
                tree.getroot().get('type') != 'topic'):
                # Not a Mallard documentation file.
                continue
            title = desc = ""
            node = tree.find('m:title', namespaces)
            if node is not None:
                title = node.text
            node = tree.find('m:info/m:desc', namespaces)
            if node is not None:
                desc = ''.join(node.itertext())
            desc = desc.strip(' \t\n\r')
            if desc == "":
                desc = title

            data.append((filename, title, desc, os.path.basename(manualdir)))
    return data


def search(search, filters):
    '''
    Search for help documents matching the search string
    '''
    results = []
    if len(search) < 2:
        return results

    global YELP_CACHE
    if not YELP_CACHE:
        YELP_CACHE = get_yelp_documents()
    help_data = YELP_CACHE

    search = search.lower()

    for (filename, title, desc, manual) in help_data:
        if len(results) >= MAX_RESULTS:
            break
        try:
            if manual == "ubuntu-help":
                icon_hint = Gio.ThemedIcon.new("distributor-logo").to_string()
            else:
                icon_hint = Gio.ThemedIcon.new(manual).to_string()
        except:
            icon_hint = Gio.ThemedIcon.new("help").to_string()
            manual = "ubuntu-help"
        if (search in title.lower() or
            search in desc.lower() or
            search in manual.lower()):
            results.append({'uri': filename,
                            'icon': icon_hint,
                            'title': title,
                            'comment': desc,
                            'manual': manual.title()})
    return results


class Previewer(Unity.ResultPreviewer):

    def do_run(self):
        image = Gio.ThemedIcon.new(self.result.icon_hint)
        preview = Unity.GenericPreview.new(
            self.result.title, html.escape(self.result.comment), image)
        if self.result.metadata:
            preview.props.subtitle = self.result.metadata['manual'].get_string()
        icon = Gio.FileIcon.new (Gio.file_new_for_path(PROVIDER_ICON))
        action = Unity.PreviewAction.new("open", _("Open"), icon)
        preview.add_action(action)
        return preview


# Classes below this point establish communication
# with Unity, you probably shouldn't modify them.


class MySearch(Unity.ScopeSearchBase):
    def __init__(self, search_context):
        super(MySearch, self).__init__()
        self.set_search_context(search_context)

    def do_run(self):
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
                i['metadata'] = {}
                if EXTRA_METADATA:
                    for e in i:
                        for m in EXTRA_METADATA:
                            if m['id'] == e:
                                i['metadata'][e] = i[e]
                i['metadata']['provider_credits'] = GLib.Variant('s', PROVIDER_CREDITS)
                result_set.add_result(**i)
        except Exception as error:
            print(error)


class Scope(Unity.AbstractScope):
    def __init__(self):
        Unity.AbstractScope.__init__(self)

    def do_get_search_hint(self):
        return SEARCH_HINT

    def do_get_schema(self):
        '''
        Adds specific metadata fields
        '''
        schema = Unity.Schema.new()
        if EXTRA_METADATA:
            for m in EXTRA_METADATA:
                schema.add_field(m['id'], m['type'], m['field'])
        #FIXME should be REQUIRED for credits
        schema.add_field('provider_credits', 's', Unity.SchemaFieldType.OPTIONAL)
        return schema

    def do_get_categories(self):
        '''
        Adds categories
        '''
        cs = Unity.CategorySet.new()
        if CATEGORIES:
            for c in CATEGORIES:
                cat = Unity.Category.new(c['id'], c['name'],
                                         Gio.ThemedIcon.new(c['icon']),
                                         c['renderer'])
                cs.add(cat)
        return cs

    def do_get_filters(self):
        '''
        Adds filters
        '''
        fs = Unity.FilterSet.new()
        #if FILTERS:
        #
        return fs

    def do_get_group_name(self):
        return GROUP_NAME

    def do_get_unique_name(self):
        return UNIQUE_PATH

    def do_create_search_for_query(self, search_context):
        se = MySearch(search_context)
        return se

    def do_create_previewer(self, result, metadata):
        rp = Previewer()
        rp.set_scope_result(result)
        rp.set_search_metadata(metadata)
        return rp

    def do_activate(self, result, metadata, id):
        parameters = [YELP_EXECUTABLE, result.uri]
        GLib.spawn_async(parameters)
        return Unity.ActivationResponse(handled=Unity.HandledType.HIDE_DASH, goto_uri=None)


def load_scope():
    return Scope()
