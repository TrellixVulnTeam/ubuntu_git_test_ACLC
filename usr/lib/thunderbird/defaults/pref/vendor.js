// Use LANG environment variable to choose locale
pref("intl.locale.matchOS", true);

// Disable default mailer checking.
pref("mail.shell.checkDefaultMail", false);

// Enable Network Manager integration
pref("network.manage-offline-status", true);

// identify default locale to use for searchplugins
pref("distribution.searchplugins.defaultLocale", "en-US");

// Don't disable our bundled extensions in the application directory
pref("extensions.autoDisableScopes", 0);
pref("extensions.shownSelectionUI", true);

// Enable system alerts
pref("mail.biff.use_system_alert", true);
