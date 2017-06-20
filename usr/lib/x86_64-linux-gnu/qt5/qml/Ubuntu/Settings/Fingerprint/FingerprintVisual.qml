/*
 * Copyright 2016 Canonical Ltd.
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation; version 3.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Authored by Jonas G. Drange <jonas.drange@canonical.com>
 *             Florian Boucault <florian.boucault@canonical.com>
 */

import QtQuick 2.4
import Ubuntu.Settings.Fingerprint 0.1

SegmentedImage {
    id: segmentedImage

    property var masks: []

    // http://stackoverflow.com/a/1830844/538866
    function isNumeric (n) {
        return !isNaN(parseFloat(n)) && isFinite(n);
    }

    function getMasksToEnroll () {
        var outMasks = [];
        if (masks && masks.length) {
            masks.forEach(function (mask, i) {
                // Format is "<source>/[x1,y1,w1,h1],…,[xn,yn,wn,hn]"
                // If any value is non-numeric, we drop the mask.
                if (!isNumeric(mask.x) || !isNumeric(mask.y) || !isNumeric(mask.width)
                    || !isNumeric(mask.height))
                    return;

                // Translate the box so as to mirror the mask
                mask.x = (1 - (mask.x + mask.width));

                outMasks.push(mask);
            });
        }
        return outMasks;
    }

    onMasksChanged: segmentedImage.enrollMasks(getMasksToEnroll())

    textureSource: "qrc:/assets/fingerprint_segmented.png"
    boxesSource: "qrc:/assets/fingerprint_boxes.json"

    Repeater {
        model: segmentedImage.masks

        Rectangle {
            visible: UbuntuSettingsFingerprint.debug
            color: "red"
            opacity: 0.25
            x: modelData.x * segmentedImage.implicitWidth
            y: modelData.y * segmentedImage.implicitHeight
            width: modelData.width * segmentedImage.implicitWidth
            height: modelData.height * segmentedImage.implicitHeight

            Component.onCompleted: console.log('Scanner mask (x, y, w, h):', x, y, width, height)
        }
    }
}
