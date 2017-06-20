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

from gi.repository import GLib, Gio
from gi.repository import Unity
import gettext
import os.path
import gzip
import subprocess
from xml.dom import minidom
import lxml.html
import re

APP_NAME = 'unity-scope-devhelp'
LOCAL_PATH = '/usr/share/locale/'
gettext.bindtextdomain(APP_NAME, LOCAL_PATH)
gettext.textdomain(APP_NAME)
_ = gettext.gettext

GROUP_NAME = 'com.canonical.Unity.Scope.Developer.Devhelp'
UNIQUE_PATH = '/com/canonical/unity/scope/developer/devhelp'

SEARCH_HINT = _('Search Devhelp')
NO_RESULTS_HINT = _('Sorry, there are no Devhelp results that match your search.')
PROVIDER_CREDITS = _('')
SVG_DIR = '/usr/share/icons/unity-icon-theme/places/svg/'
PROVIDER_ICON = SVG_DIR + 'service-firefoxbookmarks.svg'
DEFAULT_RESULT_ICON = SVG_DIR + 'result-help.svg'
DEFAULT_RESULT_MIMETYPE = 'text/html'
DEFAULT_RESULT_TYPE = Unity.ResultType.DEFAULT
HELP_LOCATION = "/usr/share/gtk-doc/html/"
DEVHELP_COMMAND = 'devhelp'

c1 = {'id': 'documentation',
      'name': _('Technical Documents'),
      'icon': SVG_DIR + 'group-installed.svg',
      'renderer': Unity.CategoryRenderer.VERTICAL_TILE}
CATEGORIES = [c1]

FILTERS = []

EXTRA_METADATA = []

CACHE_DEVHELP = None

def setup_devhelp():
    '''
    Parses local devhelp index files for  <keyword> tags and associates
    them with the page's uri in self.data as: {name, link, type, source title}
    '''
    data = []
    for dirname in os.listdir(HELP_LOCATION):
        directory = HELP_LOCATION + dirname
        for filename in os.listdir(directory):
            filename = directory + "/" + filename
            if filename.endswith("devhelp2"):
                book = ""
                xmldoc = minidom.parse(filename)
                nodes = xmldoc.getElementsByTagName('book')
                for node in nodes:
                    book = node.getAttribute('title')
                nodes = xmldoc.getElementsByTagName('keyword')
                for node in nodes:
                    record = []
                    record.append(node.getAttribute('name'))
                    record.append(directory + '/' + node.getAttribute('link'))
                    record.append(node.getAttribute('type'))
                    record.append(book)
                    data.append(record)

            if filename.endswith("devhelp2.gz"):
                book = ""
                f = gzip.open(filename, 'rb')
                xmldoc = minidom.parse(f)
                nodes = xmldoc.getElementsByTagName('book')
                for node in nodes:
                    book = node.getAttribute('title')
                nodes = xmldoc.getElementsByTagName('keyword')
                for node in nodes:
                    record = []
                    record.append(node.getAttribute('name'))
                    record.append(directory + '/' + node.getAttribute('link'))
                    record.append(node.getAttribute('type'))
                    record.append(book)
                    data.append(record)

    return data


def search(search, filters):
    '''
    Search for help documents matching the search string
    '''
    results = []
    if len(search) < 2:
        return results
    global CACHE_DEVHELP
    if not CACHE_DEVHELP:
        print("Loading results...")
        devhelp = setup_devhelp()
        CACHE_DEVHELP = devhelp
    else:
        devhelp = CACHE_DEVHELP
    icon_hint = Gio.ThemedIcon.new("text-x-generic").to_string()
    for data in devhelp:
        if search.lower() in data[0].lower():
            if len(results) < 50:
                results.append({'uri': data[0],
                                'icon': icon_hint,
                                'category': 0,
                                'title': data[0],
                                'comment': data[3],
                                'dnd_uri': data[1]})
    return results


class Preview(Unity.ResultPreviewer):

    def do_run(self):
        preview = Unity.GenericPreview.new(self.result.title, '', None)
        preview.props.subtitle = self.result.comment
        preview.props.image = Gio.ThemedIcon.new(self.result.icon_hint)
        description = self.result.dnd_uri
        match = re.search('#', self.result.dnd_uri)
        f = open(self.result.dnd_uri[:match.start()])
        f = f.read()
        path = lxml.html.fromstring(f)
        anchor = self.result.dnd_uri[match.end():]
        anchorpath = path.xpath("//a[@name='%s']" % anchor)[0]
        parent = anchorpath.getparent()
        description = parent.text_content()
        lines = description.split('\n')
        description = ''
        for line in lines:
            if self.result.title in line:
                line = line[len(self.result.title):]
            elif line.endswith(':'):
                line = '\n \n<b>%s</b>\n\t' % line
            elif ' : ' in line:
                line = '%s\n \n' % line
            elif line.endswith(';'):
                line = '%s\n \n' % line
            elif line.startswith('Since'):
                line = '\n \n<b>%s</b>\n' % line
            else:
                line = '%s ' % line
            description = description + line

        while '    ' in description:
            description = description.replace('    ', '  ')
        while '\n\n' in description:
            description = description.replace('\n\n', '\n')

        if len(description) > 5000:
            description = description[:5000] + '…'
        preview.props.description_markup = description
        view_action = Unity.PreviewAction.new("show", _("Show"), None)
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
        
    def do_activate(self, result, metadata, id):
        uri = result.uri[:len(result.uri) - 3]
        parameters = [DEVHELP_COMMAND, "-s", uri]
        subprocess.Popen(parameters)
        return Unity.ActivationResponse(handled=Unity.HandledType.HIDE_DASH, goto_uri=None)

    def do_create_previewer(self, result, metadata):
        rp = Preview()
        rp.set_scope_result(result)
        rp.set_search_metadata(metadata)
        return rp


def load_scope():
    return Scope()
