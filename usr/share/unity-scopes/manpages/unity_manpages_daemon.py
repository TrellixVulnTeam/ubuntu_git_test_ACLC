#! /usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright(C) 2012 Pawel Stolowski <stolowski@gmail.com>
#              2013 Mark Tully <markjtully@gmail.com>
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

from gi.repository import GLib, Gio, Gtk
from gi.repository import Unity
import gettext
import subprocess
import re
import os

APP_NAME = 'unity-scope-manpages'
LOCAL_PATH = '/usr/share/locale/'
gettext.bindtextdomain(APP_NAME, LOCAL_PATH)
gettext.textdomain(APP_NAME)
_ = gettext.gettext


GROUP_NAME = 'com.canonical.Unity.Scope.Development.Manpages'
UNIQUE_PATH = '/com/canonical/unity/scope/development/manpages'

SEARCH_HINT = _('Search Manpages')
NO_RESULTS_HINT = _('Sorry, there are no Manpages that match your search.')
SVG_DIR = '/usr/share/icons/unity-icon-theme/places/svg/'
PROVIDER_ICON = SVG_DIR + 'service-manpages.svg'
DEFAULT_RESULT_ICON = SVG_DIR + 'service-manpages.svg'
DEFAULT_RESULT_MIMETYPE = 'x-scheme-handler/man'
DEFAULT_RESULT_TYPE = Unity.ResultType.DEFAULT

c1 = {'id': 'documentation',
      'name': _('Technical Documents'),
      'icon': SVG_DIR + 'group-installed.svg',
      'renderer': Unity.CategoryRenderer.VERTICAL_TILE}
CATEGORIES = [c1]

FILTERS = []

EXTRA_METADATA = []

regex_apropos = re.compile('^(.+?)\s+\((\d+)\)\s+-\s(.+?)$')
def search(search, filters):
    '''
    Use apropos to search for manpages matching the search string
    '''
    results = []
    icon_hint = Gio.ThemedIcon.new("text-x-generic").to_string()
    result = []
    if len(search) > 2:   # don't run apropos for strings shorter than 3 chars
        apropos = subprocess.Popen(["apropos", search], stdout=subprocess.PIPE)
        os.waitpid(apropos.pid, 0)
        out = apropos.communicate()[0]
        out = out.decode('utf8')
        for line in out.split("\n"):
            m = regex_apropos.match(line)
            if m:
                result.append((m.group(1), m.group(2), m.group(3)))
    for res in result:
        uri = 'man:' + res[0] + '(' + res[1] + ')'
        icon_theme = Gtk.IconTheme()
        icon_info = icon_theme.lookup_icon(res[0], 128, 0)
        if icon_info:
            icon_hint = Gio.ThemedIcon.new(res[0]).to_string()
        else:
            icon_hint = None
        results.append({'uri': uri,
                        'icon': icon_hint,
                        'category': 0,
                        'title': res[0],
                        'comment': res[2]})
    return results


class Preview(Unity.ResultPreviewer):

    def do_run(self):
        preview = Unity.GenericPreview.new(self.result.title, '', None)
        preview.props.subtitle = self.result.comment
        image = Gio.ThemedIcon.new(self.result.icon_hint)
        preview.props.image = image
        manpage = subprocess.check_output(['man', self.result.title])
        match = re.search('NAME', manpage.decode('utf-8'))
        description = manpage.decode('utf-8')[match.start():]
        description = description.replace('‐\n       ', '')
        if len(description) > 5000:
            description = description[:5000] + '…'
        preview.props.description_markup = description
        icon = Gio.FileIcon.new (Gio.file_new_for_path(PROVIDER_ICON))
        view_action = Unity.PreviewAction.new("open", _("Open"), icon)
        preview.add_action(view_action)
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
                result_set.add_result(**i)
        except Exception as error:
            print (error)


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
        rp = Preview()
        rp.set_scope_result(result)
        rp.set_search_metadata(metadata)
        return rp


def load_scope():
    return Scope()
