"""
Cross-platform Discord presence app
"""

import toga
from toga.style.pack import COLUMN, ROW, CENTER, Pack
from toga.constants import Direction
from toga.command import Group

class VermillionRPC(toga.App):
    def startup(self):
        # Declares window title and existence
        self.main_window = toga.MainWindow(title=self.formal_name)
        # Column to show status files
        filecol = toga.Box(
            style=Pack(
                margin=(
                    0, 
                    75
                ),
                direction=COLUMN
            ),
            children=[
                toga.Label(
                    "Saved Statuses"
                ),
                toga.Label(
                    "File One"
                )
            ]
        )
        # Column to show status file contents, as well as broadcast status
        contentbox = toga.Box(
            style=Pack(
                margin=(
                    200,
                    300
                ),
                direction=COLUMN,
                justify_content=CENTER,
            ),
            children=[
                toga.Label(
                    "File contents"
                ),
                toga.Label(
                    "Details"
                ),
                toga.Label(
                    "State"
                ),
                toga.Label(
                    "Large image internal code"
                ),
                toga.Label(
                    "Large image hover text"
                ),
                toga.Label(
                    "Small image internal code"
                ),
                toga.Label(
                    "Small image hover text"
                )
            ]
        )
        # Controls for the RPC broadcast
        broadcastcont = toga.Box(
            style=Pack(
                margin=(
                    0, 
                    0
                ),
                direction=COLUMN,
            ),
            children=[
                toga.Button(
                    "Start Broadcast"
                ),
                toga.Button(
                    "End Broadcast",
                    enabled=False
                )
            ]
        )
        rightsplit = toga.SplitContainer(
            content=[
                (contentbox, 9),
                (broadcastcont, 1)
            ],
            direction=Direction.HORIZONTAL
        )
        fullsplit = toga.SplitContainer(
            content=[
                filecol,
                rightsplit
            ]
        )
        # Adds a custom settings group to the toolbar
        maingroup = Group(
            "RPC Settings", 
            order=40
        )
        # Adds a custom status management subgroup to the toolbar
        mgstat = Group(
            "Status management...", 
            parent=maingroup, 
            order=10
        )
        # Command to index the preferences command to the toolbar
        prefs_menu = toga.Command(
            self.openprefsmenu,
            text="Preferences",
            tooltip="Manage configuration",
            group=maingroup,
            section=0
        )
        # Command to index the statmake command to the toolbar
        statmake_menu = toga.Command(
            self.openstatmake,
            text="Statmake",
            tooltip="Make a new status file",
            group=mgstat,
            order=1
        )
        # Command to index the statedit command to the toolbar
        statedit_menu = toga.Command(
            self.openstatedit,
            text="Statedit",
            tooltip="Edit an existing status file",
            group=mgstat,
            order=2
        )
        self.commands.add(prefs_menu)
        self.commands.add(statmake_menu)
        self.commands.add(statedit_menu)
        main_box = toga.Box()
        main_box.add(fullsplit)
        self.main_window.content = main_box
        self.main_window.show()
    # Command to make and open the preferences menu
    def openprefsmenu(self, widget):
        prefswindow = toga.Window(
            title="Preferences"
        )
        prefswindow.content = toga.Box(
            children=[
                toga.Label(
                    "Prefs menu still in development"
                ),
            ],
        )
        prefswindow.show()
    # Command to open statmake tool
    def openstatmake(self, widget):
        pass
    # Command to open statedit tool
    def openstatedit(self, widget):
        pass


def main():
    return VermillionRPC()
