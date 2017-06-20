/*
 * Copyright 2014-2017 Canonical Ltd.
 *
 * This file is part of webbrowser-app.
 *
 * webbrowser-app is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; version 3.
 *
 * webbrowser-app is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

.pragma library

// Note: when changing the values of these variables, all domains which
// use them must be carefully tested to ensure no regression.
var android_no_device_override = "Mozilla/5.0 (Linux; Android 5.0;) AppleWebKit/537.36 Chrome/${CHROMIUM_VERSION} Mobile Safari/537.36";
var nexus5_override = "Mozilla/5.0 (Linux; Ubuntu 17.04; Android 5.0; Nexus 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/${CHROMIUM_VERSION} Mobile Safari/537.36";
var ubuntu_like_android_override = "Mozilla/5.0 (Linux; Ubuntu 17.04 like Android 5.0;) AppleWebKit/537.36 Chrome/${CHROMIUM_VERSION} Mobile Safari/537.36";
var no_android_token = "Mozilla/5.0 (Linux; Ubuntu 17.04;) AppleWebKit/537.36 Chrome/${CHROMIUM_VERSION} Mobile Safari/537.36";

var overrides = [
    // Youtube (https://launchpad.net/bugs/1228415, https://launchpad.net/bugs/1415107, https://launchpad.net/bugs/1417258, https://launchpad.net/bugs/1499394, https://launchpad.net/bugs/1408760, https://launchpad.net/bugs/1437485)
    ["^https:\/\/(www|m)\.youtube\.com\/", android_no_device_override],

    // Gmail (https://launchpad.net/bugs/1375889)
    ["^https:\/\/mail\.google\.com\/", android_no_device_override],

    // Google plus (https://launchpad.net/bugs/1656310)
    ["^https:\/\/plus\.google\.com\/", ubuntu_like_android_override],

    // Google hangouts (https://launchpad.net/bugs/1565055)
    ["^https:\/\/hangouts\.google\.com\/", ubuntu_like_android_override],
    ["^https:\/\/talkgadget\.google\.com\/hangouts\/", ubuntu_like_android_override],
    ["^https:\/\/plus\.google\.com\/hangouts\/", ubuntu_like_android_override],

    // Google recaptcha (https://launchpad.net/bugs/1599146)
    ["^https:\/\/www\.google\.com\/recaptcha\/", ubuntu_like_android_override],

    // Google photos (https://launchpad.net/bugs/1665926)
    ["^https:\/\/photos\.google\.com\/", ubuntu_like_android_override],

    // Facebook (https://launchpad.net/bugs/1538056, https://launchpad.net/bugs/1457661)
    ["^https:\/\/(www|m)\.facebook\.com\/", nexus5_override],

    // Twitter (https://launchpad.net/bugs/1577834)
    ["^https:\/\/mobile\.twitter\.com\/", no_android_token],

    // meet.jit.si (https://launchpad.net/bugs/1635971)
    ["^https:\/\/meet\.jit\.si\/", ubuntu_like_android_override],

    // ESPN websites (https://launchpad.net/bugs/1316259)
    ["^http:\/\/(\w+\.)*espn\.(go\.)?com\/", ubuntu_like_android_override],

    // New York Times (https://launchpad.net/bugs/1573620)
    ["^https?:\/\/(mobile\.)?nytimes\.com\/", nexus5_override],

    // appear.in (https://launchpad.net/bugs/1659288)
    ["^https:\/\/appear\.in\/", no_android_token],
];
