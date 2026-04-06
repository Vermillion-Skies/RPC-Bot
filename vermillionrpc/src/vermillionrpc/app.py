"""
Cross-platform Discord presence app
"""
import pathlib
from pathlib import Path
import toga
from toga.sources import ListSource
from toga.style.pack import COLUMN, ROW, CENTER, Pack
from toga.constants import Direction
from toga.command import Group
import os

class VermillionRPC(toga.App):
    def startup(self):
        global startbroadbutton
        global endbroadbutton
        global contentd
        global contents
        global contentli
        global contentlt
        global contentsi
        global contentst
        # Declares window title and existence
        self.main_window = toga.MainWindow(
            title=self.formal_name)
        # Column to show status files
        filecol = toga.Box(
            style=Pack(
                margin=(
                    0, 
                    0
                ),
                direction=COLUMN
            ),
            children=[
                toga.Label(
                    "Saved Statuses"
                )
            ])
        # Make a table with contents of app data folder
        datadir = self.paths.data
        files = os.listdir(datadir)
        self.filetable = toga.Table(
            headings=[
                "Files"
            ],
            accessors={
                "file"
            },
            on_select=self.filechanged
        )
        for item in files:
            self.filetable.data.append(
                {
                    "file": item
                }
            )
        filecol.add(
            self.filetable
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
            ])
        self.contentd = toga.Label(
            "Details")
        self.contents = toga.Label(
            "State")
        self.contentli = toga.Label(
            "Large image internal code")
        self.contentlt = toga.Label(
            "Large image hover text")
        self.contentsi = toga.Label(
            "Small image internal code")
        self.contentst = toga.Label(
            "Small image hover text")
        contentbox.add(
            self.contentd,
            self.contents,
            self.contentli,
            self.contentlt,
            self.contentsi,
            self.contentst)
        startbroadbutton = toga.Button(
            "Start Broadcast",
            on_press=self.startbroadcast,
            enabled=True)
        endbroadbutton = toga.Button(
            "End Broadcast",
            on_press=self.endbroadcast,
            enabled=False)
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
            ])
        rightsplit = toga.SplitContainer(
            content=[
                (contentbox, 9),
                (broadcastcont, 1)
            ],
            direction=Direction.HORIZONTAL)
        fullsplit = toga.SplitContainer(
            content=[
                filecol,
                rightsplit
            ])
        # Adds a custom settings group to the toolbar
        maingroup = Group(
            "RPC Settings", 
            order=40)
        # Adds a custom status management subgroup to the toolbar
        mgstat = Group(
            "Status management...", 
            parent=maingroup, 
            order=10)
        # Command to index the preferences command to the toolbar
        prefs_menu = toga.Command(
            self.openprefsmenu,
            text="Preferences",
            tooltip="Manage configuration",
            group=maingroup,
            section=0)
        # Command to index the statmake command to the toolbar
        statmake_menu = toga.Command(
            self.openstatmake,
            text="Statmake",
            tooltip="Make a new status file",
            group=mgstat,
            order=1)
        # Command to index the statedit command to the toolbar
        statedit_menu = toga.Command(
            self.openstatedit,
            text="Statedit",
            tooltip="Edit an existing status file",
            group=mgstat,
            order=2)
        self.commands.add(
            prefs_menu,
            statmake_menu,
            statedit_menu)
        main_box = toga.Box()
        main_box.add(fullsplit)
        self.main_window.content = main_box
        self.main_window.show()
    # Command to manage file selection
    def filechanged(self, widget):
        selectedfile = self.filetable.selection
        path = self.paths.data / selectedfile.file
        entrylist = []
        try:
            with open(path, "r") as file:
                entrylist = [line.strip() for line in file]
        except:
            pass
        print(entrylist)
        self.contentd.text = entrylist[0]
        self.contents.text = entrylist[1]
        self.contentli.text = entrylist[2]
        self.contentlt.text = entrylist[3]
        self.contentsi.text = entrylist[4]
        self.contentst.text = entrylist[5]
    # Command to start the presence broadcast
    async def startbroadcast(self, widget):
        startbroadbutton.enabled = False
        endbroadbutton.enabled = True
        await self.main_window.dialog(
            toga.InfoDialog(
                "Error: Broadcast not started",
                "Broadcast code is still in development."
            ))
    # Command to end the presence broadcast
    async def endbroadcast(self, widget):
        startbroadbutton.enabled = True
        endbroadbutton.enabled = False
        await self.main_window.dialog(
            toga.InfoDialog(
                "Error: Broadcast not ended",
                "Broadcast code is still in development"
            ))
    # Command to make and open the preferences menu
    def openprefsmenu(self, widget):
        self.appid_input = toga.TextInput(flex=1)
        prefswindow = toga.Window(
            title="Preferences")
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
            ],)
        # Checks if the app ID config exists. If so, sets the value of appid_input to the inputted ID
        path = self.paths.config / "appid.toml"
        if not path.exists():
            pass
        else:
            self.appid_input.value = path.read_text(
                encoding="utf-8"
            )
        prefswindow.show()
    # Command to save your settings to local appdata folder
    def savesettings(self, widget):
        path = self.paths.config / "appid.toml"
        path.write_text(
            self.appid_input.value, 
            encoding='utf-8')
    # Command to open statmake tool
    def openstatmake(self, widget):
        self.statmakewin = toga.Window(
            title="Statmake")
        self.ninput = toga.TextInput(
            flex=1)
        self.dinput = toga.TextInput(
            flex=1)
        self.sinput = toga.TextInput(
            flex=1)
        self.liinput = toga.TextInput(
            flex=1)
        self.ltinput = toga.TextInput(
            flex=1)
        self.siinput = toga.TextInput(
            flex=1)
        self.stinput = toga.TextInput(
            flex=1)
        self.statmakewin.content = toga.Box(
            direction=COLUMN,
            children=[
                toga.Label(
                    "Statmake tool"
                ),
                toga.Label(
                    "Status Name:"
                ),
                self.ninput,
                toga.Label(
                    "Details:"
                ),
                self.dinput,
                toga.Label(
                    "State:"
                ),
                self.sinput,
                toga.Label(
                    "Large image code:"
                ),
                self.liinput,
                toga.Label(
                    "Large image hover text"
                ),
                self.ltinput,
                toga.Label(
                    "Small image code:"
                ),
                self.siinput,
                toga.Label(
                    "Small image hover text:"
                ),
                self.stinput,
                toga.Button(
                    "Save status",
                    on_press=self.savestatmake
                )
            ])
        self.statmakewin.show()
    # Command to save a created status
    async def savestatmake(self, widget):
        filecontents = [
            self.dinput.value,
            self.sinput.value,
            self.liinput.value,
            self.ltinput.value,
            self.siinput.value,
            self.stinput.value]
        filename = self.ninput.value + ".txt"
        path = self.paths.data / filename
        try:
            with open(path, "w") as f:
                f.write("\n".join(filecontents))
                pass
            pass
        except Exception as e:
            await self.statmakewin.dialog(
                toga.InfoDialog(
                    "Error",
                    "Exception " + str(e) + " has occurred"
                )
            )
        else:
            await self.statmakewin.dialog(
                toga.InfoDialog(
                    "Success!",
                    "Status file successfully created!"
                )
            )
    # Command to open statedit tool
    def openstatedit(self, widget):
        stateditwin = toga.Window(
            title="Statedit")
        stateditwin.content = toga.Box(
            children=[
                toga.Label(
                    "Statedit is still in development"
                )
            ])
        stateditwin.show()


def main():
    return VermillionRPC()
