#!/usr/bin/python3
from gi.repository import Gio
import os
import sys

PREINSTALLED_LAUNCHER_DESKTOP_FILES = ["application://ubuntu-amazon-default.desktop",]
AFTER_ICON = "unity://running-apps"

UNITY_LAUNCHER_SETTINGS = "com.canonical.Unity.Launcher"
UNITY_LAUNCHER_FAVORITE_KEY = "favorites"

def get_default_favorites():
    settings = Gio.Settings.new(UNITY_LAUNCHER_SETTINGS)
    settings.delay()
    settings.reset(UNITY_LAUNCHER_FAVORITE_KEY)
    return settings.get_strv(UNITY_LAUNCHER_FAVORITE_KEY)

def install_default_webapps_in_launcher():
    # Workaround for the script triggering on systems where it shouldn't.
    if os.path.exists("/usr/share/glib-2.0/schemas/95_edubuntu-artwork.gschema.override"):
        return

    new_desktop_files = PREINSTALLED_LAUNCHER_DESKTOP_FILES

    if len(new_desktop_files) != 0:
        try:
            settings = Gio.Settings.new (UNITY_LAUNCHER_SETTINGS)
            default_favorites = get_default_favorites()
            # "If there are no common elements between these sets..."
            if not set(default_favorites).intersection(set(new_desktop_files)):
                print ("Skipping Unity Webapps migration for what seems to be a vendor-patched schema")
                return
            if not settings.is_writable(UNITY_LAUNCHER_FAVORITE_KEY):
                print ("Unity Webapps migration process (preinstallation): 'favorites' key not writable")
                return
            favorites = settings.get_strv(UNITY_LAUNCHER_FAVORITE_KEY)

            # only append the desktop icons that are not already present in the favorites list if any
            to_add = [d for d in new_desktop_files if not d in favorites]
            available_desktop_files = [d for d in favorites if ".desktop" in d]
            new_index = -1

            if len(available_desktop_files):
                new_index = favorites.index(available_desktop_files[-1]) + 1
            elif AFTER_ICON in favorites:
                new_index = favorites.index(AFTER_ICON)

            if new_index >= 0:
                new_index = favorites.index(AFTER_ICON)
                next = favorites[new_index:]
                favorites[new_index:] = to_add
                favorites.extend(next)
            else:
                favorites.extend(to_add)

            settings.set_strv(UNITY_LAUNCHER_FAVORITE_KEY, favorites)

            # force sync to avoid race
            settings.sync()
        except Exception as e:
            print ("Unity Webapps migration exception:", str(e))

if __name__ == "__main__":
    source = Gio.SettingsSchemaSource.get_default()
    if source.lookup(UNITY_LAUNCHER_SETTINGS, True) is None: # schema not found
        sys.exit(1)
    install_default_webapps_in_launcher()
