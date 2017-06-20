#! /usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright(C) 2012 Frederik Elwert <frederik.elwert@web.de>
#              2012 Pawel Stolowski <stolowski@gmail.com>
#              2012 Mark Tully <markjtully@gmail.com>
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
import re
import os.path
from subprocess import Popen, PIPE
from mimetypes import guess_type
from html.parser import HTMLParser

try:
    from pyPdf import PdfFileReader
    from pyPdf.utils import PdfReadError
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False


APP_NAME = 'unity-scope-texdoc'
LOCAL_PATH = '/usr/share/locale/'
gettext.bindtextdomain(APP_NAME, LOCAL_PATH)
gettext.textdomain(APP_NAME)
_ = gettext.gettext

GROUP_NAME = 'com.canonical.Unity.Scope.Help.Texdoc'
UNIQUE_PATH = '/com/canonical/unity/scope/help/texdoc'

SEARCH_HINT = _('Search Texdoc')
NO_RESULTS_HINT = _('Sorry, there are no Texdoc results that match your search.')
PROVIDER_CREDITS = _('')
SVG_DIR = '/usr/share/icons/unity-icon-theme/places/svg/'
PROVIDER_ICON = SVG_DIR + 'service-texdoc.svg'
DEFAULT_RESULT_ICON = SVG_DIR + 'result-help.svg'
DEFAULT_RESULT_MIMETYPE = 'text/html'
DEFAULT_RESULT_TYPE = Unity.ResultType.DEFAULT
TEXDOC_RE = re.compile('^\s*(\d+)\s+(.+?)$')

c1 = {'id': 'help',
      'name': _('Technical Documents'),
      'icon': SVG_DIR + 'group-installed.svg',
      'renderer': Unity.CategoryRenderer.VERTICAL_TILE}
CATEGORIES = [c1]

FILTERS = []

EXTRA_METADATA = []


def get_file_info(filepath):
    info = {}
    info['uri'] = 'file://' + filepath
    info['filename'] = os.path.basename(filepath)
    info['mimetype'] = guess_type(info['uri'])[0] or ''
    if info['mimetype']:
        info['icon'] = Gio.content_type_get_icon(info['mimetype'])
        if info['mimetype'] == 'application/pdf' and PDF_AVAILABLE:
            info['title'] = get_pdf_title(filepath)
        elif info['mimetype'] == 'text/html':
            info['title'] = get_html_title(filepath)
        else:
            info['title'] = ''
    else:
        info['icon'] = Gio.ThemedIcon.new('text-x-generic')
        info['title'] = ''
    return info


def get_pdf_title(filepath):
    with open(filepath, 'rb') as pdffile:
        reader = PdfFileReader(pdffile)
        try:
            return reader.documentInfo.title or ''
        except PdfReadError:
            return ''


def get_html_title(filepath):

    class HTMLTitleParser(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.is_title = False
            self.title_complete = False
            self.title = ''

        def handle_starttag(self, tag, attrs):
            if tag == 'title':
                self.is_title = True

        def handle_data(self, data):
            if self.is_title:
                self.title += data

        def handle_endtag(self, tag):
            if tag == 'title':
                self.title_complete = True
                self.is_title = False

    with open(filepath, 'r') as htmlfile:
        parser = HTMLTitleParser()
        for line in htmlfile:
            parser.feed(line)
            if parser.title_complete:
                return parser.title


def search(search, filters):
    '''
    Search for help documents matching the search string
    '''
    results = []
    result = []
    if len(search) > 2:   # don't run texdoc for strings shorter than 3 chars
        proc = Popen(["texdoc", "--list", "--nointeract", search], stdout=PIPE)
        os.waitpid(proc.pid, 0)
        out = proc.communicate()[0]
        out = out.decode('utf8')
        for line in out.splitlines():
            m = TEXDOC_RE.match(line)
            if m:
                result.append(m.group(2))
    for res in result:
        info = get_file_info(res)
        if info['mimetype']:
            # Only handle known file types, otherwise we might get
            # Makefiles and things like that.
            results.append({'uri': info['uri'],
                            'icon': info['icon'].to_string(),
                            'category': 0,
                            'mimetype': info['mimetype'],
                            'title': info['filename'],
                            'comment': info['title']})
    return results


def activate(scope, uri):
    '''
    Open the url in the default webbrowser
    Args:
      uri: The url to be opened
    '''
    uri = uri[:len(uri) - 3]
    parameters = ["devhelp", "-s", uri]
    subprocess.Popen(parameters)
    return Unity.ActivationResponse(handled=Unity.HandledType.HIDE_DASH, goto_uri='')


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


def load_scope():
    return Scope()
