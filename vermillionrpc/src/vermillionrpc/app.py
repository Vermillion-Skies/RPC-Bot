"""
Cross-platform Discord presence app
"""

import toga
from toga.style.pack import COLUMN, ROW, Pack
from toga.constants import Direction


class VermillionRPC(toga.App):
    def startup(self):
        # Column to show status files
        filecol = toga.Box(
            style=Pack(
                margin=(0, 75)
            )
        )
        # Column to show status file contents, as well as broadcast status
        contentbox = toga.Box(
            style=Pack(
                margin=(0, 5)
            )
        )
        # Controls for the RPC broadcast
        broadcastcont = toga.Box(
            style=Pack(
                margin=(0,5),
            )
        )
        # Starts RPC broadcast
        bcs = toga.Button(
            "Start broadcast"
        )
        # Ends RPC broadcast
        bce = toga.Button(
            "End broadcast"
        )
        broadcastcont.add(
            bcs,
            bce
        )
        filecol.add(toga.Label("Statuses"))
        contentbox.add(toga.Label("Contents"))
        rightsplit = toga.SplitContainer(
            content=[
                contentbox,
                broadcastcont
            ],
            direction=Direction.HORIZONTAL
        )
        fullsplit = toga.SplitContainer(
            content=[
                filecol,
                rightsplit
            ]
        )
        main_box = toga.Box()
        main_box.add(fullsplit)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return VermillionRPC()
