"""
Cross-platform Discord presence app
"""

import toga
from toga.style.pack import COLUMN, ROW, Pack


class VermillionRPC(toga.App):
    def startup(self):
        filecol = toga.Box(style=Pack(margin=(0, 20))) # Column to show status files
        contentcol = toga.Box(style=Pack(margin=(0, 5))) # Column to show status file contents, as well as broadcast status
        filecol.add(toga.Label("Status Files"))
        contentcol.add(toga.Label("Contents"))
        split = toga.SplitContainer()
        split.content = [filecol, contentcol]
        main_box = toga.Box()
        main_box.add(split)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return VermillionRPC()
