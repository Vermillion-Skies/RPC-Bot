"""
Cross-platform Discord presence app
"""
import pathlib
from pathlib import Path
import toga
from toga.style.pack import COLUMN, ROW, CENTER, Pack
from toga.constants import Direction
from toga.command import Group

class VermillionRPC(toga.App):
    def startup(self):
        global startbroadbutton
        global endbroadbutton
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
        startbroadbutton = toga.Button(
            "Start Broadcast",
            on_press=self.startbroadcast,
            enabled=True
        )
        endbroadbutton = toga.Button(
            "End Broadcast",
            on_press=self.endbroadcast,
            enabled=False
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
                startbroadbutton,
                endbroadbutton
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
    # Command to start the presence broadcast
    async def startbroadcast(self, widget):
        startbroadbutton.enabled = False
        endbroadbutton.enabled = True
        await self.main_window.dialog(
            toga.InfoDialog(
                "Error: Broadcast not started",
                "Broadcast code is still in development."
            )
        )
    # Command to end the presence broadcast
    async def endbroadcast(self, widget):
        startbroadbutton.enabled = True
        endbroadbutton.enabled = False
        await self.main_window.dialog(
            toga.InfoDialog(
                "Error: Broadcast not ended",
                "Broadcast code is still in development"
            )
        )
    # Command to make and open the preferences menu
    def openprefsmenu(self, widget):
        self.appid_input = toga.TextInput(flex=1)
        prefswindow = toga.Window(
            title="Preferences"
        )
        prefswindow.content = toga.Box(
            direction=COLUMN,
            children=[
                toga.Label(
                    "App ID: "
                ),
                self.appid_input,
                toga.Button(
                    "Save changes",
                    on_press=self.savesettings
                )
            ],
        )
        # Checks if the app ID config exists. If so, sets the value of appid_input to the inputted ID
        path = self.paths.data / "appid.toml"
        if not path.exists():
            pass
        else:
            self.appid_input.value = path.read_text(
                encoding="utf-8"
            )
        prefswindow.show()
    # Command to save your settings to local appdata folder
    def savesettings(self, widget):
        path = self.paths.data / "appid.toml"
        path.write_text(
            self.appid_input.value, 
            encoding='utf-8'
        )
    # Command to open statmake tool
    def openstatmake(self, widget):
        statmakewin = toga.Window(
            title="Statmake"
        )
        statmakewin.content = toga.Box(
            children=[
                toga.Label(
                    "Statmake still in development"
                )
            ]
        )
        statmakewin.show()
    # Command to open statedit tool
    def openstatedit(self, widget):
        stateditwin = toga.Window(
            title="Statedit"
        )
        stateditwin.content = toga.Box(
            children=[
                toga.Label(
                    "Statedit is still in development"
                )
            ]
        )
        stateditwin.show()


def main():
    return VermillionRPC()
