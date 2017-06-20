/*
 * Copyright (C) 2016, 2017 Canonical Ltd
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 3 as
 * published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Authored-by: Florian Boucault <florian.boucault@canonical.com>
 *              Andrew Hayzen <andrew.hayzen@canonical.com>
 */
import QtQuick 2.4
import QtQml.Models 2.2
import QtQuick.Window 2.2
import Ubuntu.Components 1.3
import "TabsBar" as LocalTabs

import Ubuntu.Components.Extras 0.3

Item {
    id: tabsBar

    implicitWidth: units.gu(60)
    implicitHeight: units.gu(3)

    property color color: "white"
    property color backgroundColor: "white"
    property color foregroundColor: "black"
    property color contourColor: Qt.rgba(0.0, 0.0, 0.0, 0.2)
    property color actionColor: "black"
    property color highlightColor: Qt.rgba(actionColor.r, actionColor.g, actionColor.b, 0.1)
    /* 'model' needs to have the following members:
         property int selectedIndex
         function addExistingTab(var tab)
         function selectTab(int index)
         function removeTab(int index)
         function removeTabWithoutDestroying(int index)
         function moveTab(int from, int to)

         removeTabWithoutDestroying is useful when a tab is being removed due
         to moving, so you don't want the content to be destroyed
    */
    property var model
    property list<Action> actions
    property bool dimmed: false

    /* To enable drag and drop set to enabled
     *
     * Use expose to set any information you need the DropArea to access
     * Then use drag.source.expose.myproperty
     *
     * Set mimeType to one of the keys in the DropArea's you want to accept
     *
     * Set a function for previewUrlFromIndex which is given the index
     * and returns a url to an image, which will be shown in the handle
     */
    readonly property alias dragAndDrop: dragAndDropImpl

    LocalTabs.DragAndDropSettings {
        id: dragAndDropImpl
    }

    property string fallbackIcon: ""

    property Component windowFactory: null
    property var windowFactoryProperties: ({})  // any addition properties such as height, width

    signal contextMenu(var tabDelegate, int index)

    function iconNameFromModelItem(modelItem, index) {
        return "";
    }

    function iconSourceFromModelItem(modelItem, index) {
        return "";
    }

    function titleFromModelItem(modelItem) {
        return modelItem.title;
    }

    Rectangle {
        id: backgroundLeft
        anchors {
            left: parent.left
            top: parent.top
            bottom: parent.bottom
        }
        width: bottomContourLeft.width
        color: tabsBar.color
    }

    Rectangle {
        id: backgroundRight
        anchors {
            right: parent.right
            top: parent.top
            bottom: parent.bottom
        }
        width: bottomContourRight.width
        color: tabsBar.color
    }

    LocalTabs.TabStepper {
        id: leftStepper
        anchors {
            top: parent.top
            bottom: parent.bottom
            left: parent.left
        }
        layoutDirection: Qt.LeftToRight
        foregroundColor: tabsBar.foregroundColor
        contourColor: tabsBar.contourColor
        highlightColor: tabsBar.highlightColor
        counter: tabs.indexFirstVisibleItem
        active: tabs.overflow
        onClicked: {
            var nextInvisibleItem = tabs.indexFirstVisibleItem - 1;
            tabs.animatedPositionAtIndex(nextInvisibleItem);
        }
    }

    LocalTabs.TabStepper {
        id: rightStepper
        anchors {
            top: parent.top
            bottom: parent.bottom
            right: actions.left
        }
        layoutDirection: Qt.RightToLeft
        foregroundColor: tabsBar.foregroundColor
        contourColor: tabsBar.contourColor
        highlightColor: tabsBar.highlightColor
        counter: tabs.count - tabs.indexLastVisibleItem - 1
        active: tabs.overflow
        onClicked: {
            var nextInvisibleItem = tabs.indexLastVisibleItem + 1;
            tabs.animatedPositionAtIndex(nextInvisibleItem);
        }
    }

    ListView {
        id: tabs
        anchors {
            top: parent.top
            bottom: parent.bottom
            left: tabs.overflow ? leftStepper.right : parent.left
            leftMargin: tabs.overflow ? 0 : units.gu(1)
            right: tabs.overflow ? rightStepper.left : actions.left
        }
        interactive: false
        objectName: "tabListView"
        orientation: ListView.Horizontal
        clip: true
        highlightMoveDuration: UbuntuAnimation.FastDuration

        UbuntuNumberAnimation { id: scrollAnimation; target: tabs; property: "contentX" }

        function animatedPositionAtIndex(index) {
            scrollAnimation.running = false;
            var pos = tabs.contentX;
            var destPos;
            tabs.positionViewAtIndex(index, ListView.Contain);
            destPos = tabs.contentX;
            scrollAnimation.from = pos;
            scrollAnimation.to = destPos;
            scrollAnimation.running = true;
        }

        property int indexFirstVisibleItem: indexAt(contentX+1, height / 2)
        property int indexLastVisibleItem: indexAt(contentX+width-1, height / 2)
        property real minimumTabWidth: units.gu(15)
        property int maximumTabsCount: Math.floor((tabsBar.width - actions.width - units.gu(1)) / minimumTabWidth)
        property real availableWidth: tabsBar.width - actions.width - units.gu(1)
        property real maximumTabWidth: availableWidth / tabs.count
        property bool overflow: tabs.count > maximumTabsCount

        displaced: Transition {
            UbuntuNumberAnimation { property: "x" }
        }

        currentIndex: tabsBar.model.selectedIndex
        model: tabsBar.model
        delegate: MouseArea {
            id: tabMouseArea
            objectName: "tabDelegate"

            acceptedButtons: Qt.LeftButton | Qt.RightButton | Qt.MiddleButton
            width: tab.width
            height: tab.height
            drag {
                target: (tabs.count > 1 || dragAndDrop.enabled) && tab.isFocused ? tab : null
                axis: dragAndDrop.enabled ? Drag.XAndYAxis : Drag.XAxis
                minimumX: tab.isDragged ? -tab.width/2 : -Infinity
                maximumX: tab.isDragged ? tabs.width - tab.width/2 : Infinity
            }
            z: tab.isFocused ? 1 : 0

            readonly property int tabIndex: index  // for autopilot

            Binding {
                target: tabsBar
                property: "selectedTabX"
                value: tabs.x + tab.x + (tab.isDragged ? 0 : tabMouseArea.x - tabs.contentX)
                when: tab.isFocused
            }
            Binding {
                target: tabsBar
                property: "selectedTabWidth"
                value: tab.width
                when: tab.isFocused
            }
            NumberAnimation {
                id: resetVerticalAnimation
                target: tab
                duration: 250
                property: "y"
                to: 0
            }

            onPressed: {
                if (mouse.button === Qt.LeftButton) {
                    tabsBar.model.selectTab(index)
                } else if (mouse.button === Qt.RightButton) {
                    tabsBar.contextMenu(tabMouseArea, index)
                } else if (mouse.button === Qt.MiddleButton) {
                    tabsBar.model.removeTab(index)
                }
            }
            onReleased: resetVerticalAnimation.start()
            onWheel: {
                if (wheel.angleDelta.y >= 0) {
                    tabsBar.model.selectTab(tabsBar.model.selectedIndex - 1);
                } else {
                    tabsBar.model.selectTab(tabsBar.model.selectedIndex + 1);
                }
            }

            hoverEnabled: true

            LocalTabs.Tab {
                id: tab
                objectName: "tabItem"

                anchors.left: tabMouseArea.left
                implicitWidth: tabs.availableWidth / 2
                width: tabs.overflow ? tabs.availableWidth / tabs.maximumTabsCount : Math.min(tabs.maximumTabWidth, implicitWidth)
                height: tabs.height

                // Reference the tab and window so that the dropArea can determine what to do
                readonly property var thisTab: tabsBar.model.get(index)
                readonly property var thisWindow: dragAndDrop.thisWindow

                property bool isDragged: tabMouseArea.drag.active
                Drag.active: tab.isDragged
                Drag.source: tabMouseArea
                Drag.hotSpot.x: width / 2
                Drag.hotSpot.y: height / 2

                states: State {
                    name: "dragging"
                    when: tab.isDragged
                    ParentChange { target: tab; parent: tabs }
                    AnchorChanges { target: tab; anchors.left: undefined }
                }
                transitions: Transition {
                    from: "dragging"
                    ParentAnimation {
                        NumberAnimation {
                            property: "x"
                            duration: UbuntuAnimation.FastDuration
                            easing: UbuntuAnimation.StandardEasing
                        }
                    }
                    AnchorAnimation {
                        duration: UbuntuAnimation.FastDuration
                        easing: UbuntuAnimation.StandardEasing
                    }
                }

                fallbackIcon: tabsBar.fallbackIcon
                iconName: tabsBar.iconNameFromModelItem(typeof(modelData) === "undefined" ? model : modelData, index)
                iconSource: tabsBar.iconSourceFromModelItem(typeof(modelData) === "undefined" ? model : modelData, index)
                isHovered: tabMouseArea.containsMouse
                isFocused: tabsBar.model.selectedIndex == index
                isBeforeFocusedTab: index == tabsBar.model.selectedIndex - 1
                title: tabsBar.titleFromModelItem(typeof(modelData) === "undefined" ? model : modelData)
                outsideColor: tabsBar.color
                backgroundColor: tabsBar.backgroundColor
                foregroundColor: tabsBar.foregroundColor
                contourColor: tabsBar.contourColor
                actionColor: tabsBar.actionColor
                highlightColor: tabsBar.highlightColor
                onClose: tabsBar.model.removeTab(index)
            }

            DropArea {
                anchors.fill: parent
                onEntered: {
                    tabsBar.model.moveTab(drag.source.DelegateModel.itemsIndex,
                                          tabMouseArea.DelegateModel.itemsIndex)
                    if (tabMouseArea.DelegateModel.itemsIndex == tabs.indexLastVisibleItem) {
                        tabs.animatedPositionAtIndex(tabs.indexLastVisibleItem + 1);
                    } else if (tabMouseArea.DelegateModel.itemsIndex == tabs.indexFirstVisibleItem) {
                        tabs.animatedPositionAtIndex(tabs.indexFirstVisibleItem - 1);
                    }
                }
            }

            DragHelper {
                id: dragHelper
                expectedAction: dragAndDrop.expectedAction
                mimeType: dragAndDrop.mimeType
                previewBorderWidth: dragAndDrop.previewBorderWidth
                previewSize: dragAndDrop.previewSize
                previewTopCrop: dragAndDrop.previewTopCrop
                previewUrl: dragAndDrop.previewUrlFromIndex(index)
                source: tab
            }

            onPositionChanged: {
                if (!dragAndDrop.enabled || !tabMouseArea.drag.active) {
                    return;
                }

                // Keep the visual tab within maxYDiff of starting point when
                // dragging vertically so that it doesn't cover other elements
                // or appear to be detached
                tab.y = Math.abs(tab.y) > dragAndDrop.maxYDiff ? (tab.y > 0 ? 1 : -1) * dragAndDrop.maxYDiff : tab.y

                // Initiate drag and drop if mouse y has gone further than the height from the object
                if (mouse.y > height * 2 || mouse.y < -height) {
                    // Reset visual position of tab delegate
                    resetVerticalAnimation.start();

                    var dropAction = dragHelper.execDrag(index);

                    // IgnoreAction - no DropArea accepted so New Window
                    // MoveAction   - DropArea accept but different window
                    // CopyAction   - DropArea accept but same window

                    if (dropAction === Qt.MoveAction) {
                        // Moved into another window

                        // Just remove from model and do not destroy
                        // as webview is used in other window
                        tabsBar.model.removeTabWithoutDestroying(index);
                    } else if (dropAction === Qt.CopyAction) {
                        // Moved into the same window

                        // So no action
                    } else if (dropAction === Qt.IgnoreAction) {
                        // Moved outside of any window

                        // Create new window and add existing tab
                        var window = windowFactory.createObject(null, windowFactoryProperties);
                        window.model.addExistingTab(tab.thisTab);
                        window.model.selectTab(window.model.count - 1);
                        window.show();

                        // Just remove from model and do not destroy
                        // as webview is used in other window
                        tabsBar.model.removeTabWithoutDestroying(index);
                    } else {
                        // Unknown state
                        console.debug("Unknown drop action:", dropAction);
                    }
                }
            }
        }
    }

    property real selectedTabX
    property real selectedTabWidth

    Rectangle {
        id: bottomContourLeft
        anchors {
            left: parent.left
            bottom: parent.bottom
        }
        width: MathUtils.clamp(selectedTabX,
                               leftStepper.width, parent.width - (actions.width + rightStepper.width))
        height: units.dp(1)
        color: tabsBar.contourColor
    }

    Rectangle {
        id: bottomContourRight
        anchors {
            right: parent.right
            bottom: parent.bottom
        }
        width: MathUtils.clamp(parent.width - selectedTabX - selectedTabWidth,
                               actions.width + rightStepper.width, parent.width - leftStepper.width)
        height: units.dp(1)
        color: tabsBar.contourColor
    }

    Row {
        id: actions

        anchors {
            top: parent.top
            bottom: parent.bottom
            right: parent.right
        }

        property real actionsSpacing: units.gu(1)
        property real sideMargins: units.gu(1)

        Repeater {
            id: actionsRepeater
            model: tabsBar.actions

            LocalTabs.TabButton {
                objectName: modelData.objectName
                iconColor: tabsBar.actionColor
                iconSource: modelData.iconSource
                onClicked: modelData.trigger()
                leftMargin: index == 0 ? actions.sideMargins : actions.actionsSpacing / 2.0
                rightMargin: index == actionsRepeater.count - 1 ? actions.sideMargins : actions.actionsSpacing / 2.0
            }
        }
    }

    Rectangle {
        anchors.fill: parent
        color: backgroundColor
        opacity: 0.4
        visible: !Window.active || (dimmed && !dropArea.containsDrag)
    }

    DropArea {
        id: dropArea
        anchors {
            fill: parent
        }
        keys: [dragAndDrop.mimeType]

        onDropped: {
            // IgnoreAction - no DropArea accepted so New Window
            // MoveAction   - DropArea accept but different window
            // CopyAction   - DropArea accept but same window
            if (drag.source.thisWindow === dragAndDrop.thisWindow) {
                // Dropped in same window
                drop.accept(Qt.CopyAction);
            } else {
                // Dropped in new window, moving tab
                tabsBar.model.addExistingTab(drag.source.thisTab);
                tabsBar.model.selectTab(tabsBar.model.count - 1);

                drop.accept(Qt.MoveAction);
            }
        }
        onEntered: {
            thisWindow.raise()
            thisWindow.requestActivate();
        }
        onPositionChanged: {
            if (drag.source.thisWindow === dragAndDrop.thisWindow) {
                // tab drag is within same window and in chrome
                // so reorder tabs by setting tab x position
                drag.source.x = drag.x - (drag.source.width / 2);
            }
        }
    }
}
