#!/usr/bin/python3
from gi.repository import Gio
import os
import time
import sys

AFTER_ICON = "unity://running-apps"

UNITY_LAUNCHER_SETTINGS = "com.canonical.Unity.Launcher"
UNITY_LAUNCHER_FAVORITE_KEY = "favorites"

def modify_webapps_in_launcher(new_desktop_files, current_default_favorites, do_install=True):
    if len(new_desktop_files) != 0:
        try:
            settings = Gio.Settings.new (UNITY_LAUNCHER_SETTINGS)
            default_favorites = current_default_favorites
            if not settings.is_writable(UNITY_LAUNCHER_FAVORITE_KEY):
                print ("Unity Webapps migration process (preinstallation): 'favorites' key not writable")
                return
            favorites = settings.get_strv(UNITY_LAUNCHER_FAVORITE_KEY)

            if do_install:
                # only append the desktop icons that are not already present in the favorites list if any
                to_modify = [d for d in new_desktop_files if not d in favorites]
            else:
                to_modify = [d for d in new_desktop_files if d in favorites]

            available_desktop_files = [d for d in favorites if ".desktop" in d]

            if do_install:
                new_index = -1
                
                if len(available_desktop_files):
                    new_index = favorites.index(available_desktop_files[-1]) + 1
                elif AFTER_ICON in favorites:
                    new_index = favorites.index(AFTER_ICON)
                    
                if new_index >= 0:
                    new_index = favorites.index(AFTER_ICON)
                    next = favorites[new_index:]
                    favorites[new_index:] = to_modify
                    favorites.extend(next)
                else:
                    favorites.extend(to_modify)
            else:
                favorites = [f for f in favorites if not f in to_modify]

            settings.set_strv(UNITY_LAUNCHER_FAVORITE_KEY, favorites)

            # force sync to avoid race
            settings.sync()
        except Exception as e:
            print ("Unity Webapps migration exception:", str(e))

def install_webapps_in_launcher(new_desktop_files, current_default_favorites):
    print ('Webapp migration script: installing', new_desktop_files, 'in launcher favorites')
    modify_webapps_in_launcher(new_desktop_files, current_default_favorites, True)

def remove_webapps_in_launcher(old_desktop_files, current_default_favorites):
    print ('Webapp migration script: removing', old_desktop_files, 'in launcher favorites')
    modify_webapps_in_launcher(old_desktop_files, current_default_favorites, False)

def get_launcher_favorites():
    settings = Gio.Settings.new(UNITY_LAUNCHER_SETTINGS)
    return settings.get_strv(UNITY_LAUNCHER_FAVORITE_KEY)

def cleanup_local_webapps():
    local_webapp_desktop_files = [
        'GoogleCalendargooglecom.desktop',
        'GoogleDocsdocsgooglecom.desktop',
        'GooglePlusplusgooglecom.desktop',
        'Gmailmailgooglecom.desktop',
        'FacebookMessengerfacebookcom.desktop',
        'YouTubeyoutubecom.desktop',
        'Twittertwittercom.desktop',
        'LiveMailmaillivecom.desktop',
        'YahooMailmailyahoocom.desktop',
    ]

    favorite_webapps_found = []

    default_favorites = set()
    current_favorites = set(get_launcher_favorites())

    for local_webapp_desktop_file in local_webapp_desktop_files:
        current_favorite_webapp_name = "application://{0}".format(
            local_webapp_desktop_file)

        local_webapp_desktop_filename = os.path.join(
            os.path.expanduser("~/.local/share/applications")
            , local_webapp_desktop_file)

        if os.path.exists(local_webapp_desktop_filename):
            print ("Removing local webapp desktop file:", local_webapp_desktop_filename)
            os.remove(local_webapp_desktop_filename)

            if current_favorite_webapp_name in current_favorites:
                favorite_webapps_found.append(current_favorite_webapp_name)

    remove_webapps_in_launcher(favorite_webapps_found, current_favorites);

    # needed so that unity & its filesystem monitors can track down the changes & update its structures
    time.sleep(2)

    current_favorites = set(get_launcher_favorites())
    install_webapps_in_launcher(favorite_webapps_found, current_favorites);


if __name__ == "__main__":
    source = Gio.SettingsSchemaSource.get_default()
    if source.lookup(UNITY_LAUNCHER_SETTINGS, True) is None: # schema not found
        sys.exit(1)
    cleanup_local_webapps()
