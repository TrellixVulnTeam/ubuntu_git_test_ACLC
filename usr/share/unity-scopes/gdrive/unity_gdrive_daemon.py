#! /usr/bin/python3
# -*- mode: python; python-indent: 2 -*-
#
# Copyright 2012 Canonical Ltd.
#
# Contact: Alberto Mardegan <alberto.mardegan@canonical.com>
#
# GPLv3
#

from datetime import datetime, timedelta
import gettext
import locale
import sys
import time

from gi.repository import GLib, GObject, Gio
from gi.repository import Accounts, Signon
from gi.repository import GData
from gi.repository import Unity


APP_NAME = "unity-scope-gdrive"
LOCAL_PATH = "/usr/share/locale/"

locale.setlocale(locale.LC_ALL, '')
gettext.bindtextdomain(APP_NAME, LOCAL_PATH)
gettext.textdomain(APP_NAME)
_ = gettext.gettext

# Map Google Docs types to the values of the "type" filter
TYPE_MAP = {
    "document": "documents",
    "pdf": "documents",
    "folder": "folders",
    "drawing": "images",
    "presentation": "presentations"
}
THEME = "/usr/share/icons/unity-icon-theme/places/svg/"


class GDriveScope(Unity.AbstractScope):
  __g_type_name__ = "GDriveScope"

  def __init__(self):
    super(GDriveScope, self).__init__()
    self.search_in_global = True;

    self._gdocs_accounts = []
    self.setup_accounts()

  def do_get_group_name(self):
    # The primary bus name we grab *must* match what we specify in our
    # .scope file
    return "com.canonical.Unity.Scope.File.Gdrive"

  def do_get_unique_name(self):
    return "/com/canonical/unity/scope/file/gdrive"

  def do_get_schema(self):
    schema = Unity.Schema.new()
    schema.add_field('author', 's', Unity.SchemaFieldType.REQUIRED)
    schema.add_field('shared', 'b', Unity.SchemaFieldType.REQUIRED)
    schema.add_field('starred', 'b', Unity.SchemaFieldType.REQUIRED)
    schema.add_field('updated', 'i', Unity.SchemaFieldType.REQUIRED)
    return schema

  def do_get_filters(self):
    filters = Unity.FilterSet.new()
    f = Unity.RadioOptionFilter.new ("modified", _("Last modified"), Gio.ThemedIcon.new("input-keyboard-symbolic"), False)
    f.add_option ("last-7-days", _("Last 7 days"), None)
    f.add_option ("last-30-days", _("Last 30 days"), None)
    f.add_option ("last-year", _("Last year"), None);
    filters.add(f)
    f2 = Unity.CheckOptionFilter.new ("type", _("Type"), Gio.ThemedIcon.new("input-keyboard-symbolic"), False)
    f2.add_option ("documents", _("Documents"), None)
    f2.add_option ("folders", _("Folders"), None)
    f2.add_option ("images", _("Images"), None)
    f2.add_option ("audio", _("Audio"), None)
    f2.add_option ("videos", _("Videos"), None)
    f2.add_option ("presentations", _("Presentations"), None)
    f2.add_option ("other", _("Other"), None)
    filters.add (f2)
    return filters

  def do_get_categories(self):
    cats = Unity.CategorySet.new()
    cats.add (Unity.Category.new ('global',
                                  _("Files & Folders"),
                                  Gio.ThemedIcon.new(THEME + "group-folders.svg"),
                                  Unity.CategoryRenderer.VERTICAL_TILE))
    cats.add (Unity.Category.new ('recent',
                                  _("Recent"),
                                  Gio.ThemedIcon.new(THEME + "group-recent.svg"),
                                  Unity.CategoryRenderer.VERTICAL_TILE))
    cats.add (Unity.Category.new ('downloads',
                                  _("Downloads"),
                                  Gio.ThemedIcon.new(THEME + "group-downloads.svg"),
                                  Unity.CategoryRenderer.VERTICAL_TILE))
    cats.add (Unity.Category.new ('folders',
                                  _("Folders"),
                                  Gio.ThemedIcon.new(THEME + "group-folders.svg"),
                                  Unity.CategoryRenderer.VERTICAL_TILE))
    return cats

  def do_create_search_for_query(self, search_context):
    return GDriveScopeSearch(search_context, self._gdocs_accounts)

  def do_create_previewer(self, result, metadata):
    previewer = GDriveScopePreviewer()
    previewer.set_scope_result(result)
    previewer.set_search_metadata(metadata)
    return previewer

  def setup_accounts(self):
    try:
      self._account_manager = Accounts.Manager.new_for_service_type("google-documents")
    except TypeError as e:
      print ("Couldn't start account manager, not initialising: %s" % e)
      sys.exit(0)
    self._account_manager.connect("enabled-event", self._on_enabled_event);
    for account in self._account_manager.get_enabled_account_services():
      self.add_account_service(account)

  def _on_enabled_event (self, account_manager, account_id):
    account = self._account_manager.get_account(account_id)
    for service in account.list_services():
      account_service = Accounts.AccountService.new(account, service)
      if account_service.get_enabled():
        self.add_account_service(account_service)

  def add_account_service(self, account_service):
    for gdocs_account in self._gdocs_accounts:
      if gdocs_account.get_account_service() == account_service:
        return
    gdocs_account = GDocsAccount(account_service);
    self._gdocs_accounts.append(gdocs_account)


class GDriveScopeSearch(Unity.ScopeSearchBase):
  __g_type_name__ = "GDriveScopeSearch"

  def __init__(self, search_context, accounts):
    super(GDriveScopeSearch, self).__init__()
    self.set_search_context(search_context)
    self._gdocs_accounts = accounts

  def do_run(self):
    print("Search changed to: '%s'" % self.search_context.search_query)
    result_set = self.search_context.result_set
    for gdocs_account in self._gdocs_accounts:
      results = gdocs_account.search(self.search_context)
      try:
        for i in results:
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


class GDriveScopePreviewer(Unity.ResultPreviewer):
  __g_type_name__ = "GDriveScopePreviewer"

  def do_run(self):
    icon = Gio.ThemedIcon.new(self.result.icon_hint)
    preview = Unity.GenericPreview.new(self.result.title, '', icon)
    author = self.result.metadata['author'].get_string()
    modified = datetime.fromtimestamp(
      self.result.metadata['updated'].get_int32())
    shared = self.result.metadata['shared'].get_boolean()
    starred = self.result.metadata['starred'].get_boolean()
    preview.props.subtitle = _("By %s") % author
    preview.add_info(Unity.InfoHint.new(
        "format", _("Format"), None, self.result.comment))
    preview.add_info(Unity.InfoHint.new(
        "modified", _("Modified"), None, modified.strftime('%x, %X')))
    preview.add_info(Unity.InfoHint.new(
        "shared", _("Shared"), None, _('yes') if shared else _('no')))
    preview.add_info(Unity.InfoHint.new(
        "starred", _("Starred"), None, _('yes') if starred else _('no')))

    action = Unity.PreviewAction.new("open", _("Open"), None)
    preview.add_action(action)
    return preview


class SignOnAuthorizer(GObject.Object, GData.Authorizer):
  __g_type_name__ = "SignOnAuthorizer"
  def __init__(self, account_service):
    GObject.Object.__init__(self)
    self._account_service = account_service
    self._main_loop = None
    self._token = None

  def do_process_request(self, domain, message):
    message.props.request_headers.replace('Authorization', 'OAuth %s' % (self._token, ))

  def do_is_authorized_for_domain(self, domain):
    return True if self._token else False

  def do_refresh_authorization(self, cancellable):
    if self._main_loop:
      print("Authorization already in progress")
      return False

    old_token = self._token
    # Get the global account settings
    auth_data = self._account_service.get_auth_data()
    identity = auth_data.get_credentials_id()
    session_data = auth_data.get_parameters()
    self._auth_session = Signon.AuthSession.new(identity, auth_data.get_method())
    self._main_loop = GLib.MainLoop()
    self._auth_session.process(session_data,
            auth_data.get_mechanism(),
            self.login_cb, None)
    if self._main_loop:
      self._main_loop.run()
    if self._token == old_token:
      print("Got the same token")
      return False
    else:
      print("Got token: %s" % (self._token, ))
      return True

  def login_cb(self, session, reply, error, user_data):
    print("login finished")
    self._main_loop.quit()
    self._main_loop = None
    if error:
      print("Got authentication error:", error.message)
      return
    if "AuthToken" in reply:
      self._token = reply["AuthToken"]
    elif "AccessToken" in reply:
      self._token = reply["AccessToken"]
    else:
      print("Didn't find token in session:", reply)


# Encapsulates searching a single user's GDocs
class GDocsAccount:
  def __init__ (self, account_service):
    self._account_service = account_service
    self._account_service.connect("enabled", self._on_account_enabled)
    self._enabled = self._account_service.get_enabled()
    self._authenticating = False
    authorizer = SignOnAuthorizer(self._account_service)
    authorizer.refresh_authorization(None)
    self._client = GData.DocumentsService(authorizer=authorizer)

  def get_account_service (self):
    return self._account_service

  def _on_account_enabled (self, account, enabled):
    print("account %s, enabled %s" % (account, enabled))
    self._enabled = enabled

  def search (self, context):
    results = []

    if not self._enabled:
      return results

    # Get the list of documents
    is_global = context.search_type == Unity.SearchType.GLOBAL
    feed = self.get_doc_list(
      context.search_query, context.filter_state, is_global)
    for entry in feed:
      rtype = entry.get_resource_id().split(":")[0]

      if is_global:
        category = 0
      else:
        if rtype == "folder":
          category = 3
        else:
          category = 1

      authors = sorted([author.get_name() for author in entry.get_authors()])
      shared = False
      starred = False
      for cat in entry.get_categories():
        if cat.get_scheme() != 'http://schemas.google.com/g/2005/labels':
          continue
        if cat.get_label() == 'shared':
          shared = True
        elif cat.get_label() == 'starred':
          starred = True

      results.append({
        'uri':entry.look_up_link(GData.LINK_ALTERNATE).get_uri(),
        'icon':self.icon_for_type(rtype),
        'category':category,
        'result_type':Unity.ResultType.PERSONAL,
        'mimetype':"text/html",
        'title':entry.get_title(),
        'comment':rtype,
        'dnd_uri':entry.get_content_uri(),
        'author':GLib.Variant('s', ', '.join(authors)),
        'shared':GLib.Variant('b', shared),
        'starred':GLib.Variant('b', starred),
        'updated':GLib.Variant('i', entry.get_updated()),
        })
    return results

  # This is where we do the actual search for documents
  def get_doc_list (self, search, filters, is_global):
    query = GData.DocumentsQuery()
    query.props.title = search
    query.props.exact_title = False

    # We do not want filters to effect global results
    if not is_global:
      self.apply_filters(query, filters)

    print("Searching for: " + search)

    if not self._client.is_authorized():
      if not self._client.props.authorizer.refresh_authorization(None):
        return []
    try:
      feed = self._client.query_documents(query, None, None, None).get_entries()
    except GObject.GError as e:
      print(e.message)
      return []

    if not is_global:
      feed = self.filter_results(feed, filters)
    return feed

  def apply_filters (self, query, filters):
    f = filters.get_filter_by_id("modified")
    if f != None:
      o = f.get_active_option()
      if o != None:
        age = 0
        if o.props.id == "last-year":
          age = 365
        elif o.props.id == "last-30-days":
          age = 30
        elif o.props.id == "last-7-days":
          age = 7
        if age:
          last_time = datetime.now() - timedelta(age)
          query.set_updated_min(time.mktime(last_time.timetuple()))

  def filter_results (self, feed, filters):
    f = filters.get_filter_by_id("type")
    if not f: return feed
    if not f.props.filtering:
      return feed
    r = []
    for entry in feed:
        rtype = entry.get_resource_id().split(":")[0]
        filter_type = TYPE_MAP.get(rtype, "other")
        if f.get_option(filter_type).props.active:
            r.append(entry)
    return r

  # Send back a useful icon depending on the document type
  def icon_for_type (self, doc_type):
    ret = "text-x-preview"

    if doc_type == "pdf":
      ret = "gnome-mime-application-pdf"
    elif doc_type == "drawing":
      ret = "x-office-drawing"
    elif doc_type == "document":
      ret = "x-office-document"
    elif doc_type == "presentation":
      ret = "libreoffice-oasis-presentation"
    elif doc_type == "spreadsheet" or doc_type == "text/xml":
      ret = "x-office-spreadsheet"
    elif doc_type == "folder":
      ret = "folder"
    elif doc_type == "file":
      ret = "gnome-fs-regular"
    else:
      print("Unhandled icon type: ", doc_type)

    return ret;


def load_scope():
  return GDriveScope()
