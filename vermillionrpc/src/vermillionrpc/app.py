"""
Cross platform Discord Rich Presence application
"""

import toga
from toga.style.pack import COLUMN, ROW


class VermillionRPC(toga.App):
    def startup(self):
        main_box = toga.Box(direction=COLUMN)
        
        details_label = toga.Label(
            "Details: ",
            margin=(0, 5),
        )
        self.details_input = toga.TextInput(flex=1)
        
        details_box = toga.Box(direction=ROW, margin=5)
        details_box.add(details_label)
        details_box.add(self.details_input)

        broadcastbutton = toga.Button(
            "Start Broadcast",
            on_press=self.start_broadcast,
            margin=5
        )

        main_box.add(details_box)
        main_box.add(broadcastbutton)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
    
    def start_broadcast(self, widget):
        print(f"Details= {self.details_input.value}")


def main():
    return VermillionRPC()
