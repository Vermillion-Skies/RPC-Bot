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

        state_label = toga.Label(
            "State: ",
            margin=(0, 5),
        )
        self.state_input = toga.TextInput(flex=1)

        state_box = toga.Box(direction=ROW, margin=5)
        state_box.add(state_label)
        state_box.add(self.state_input
        )
        broadcastbutton = toga.Button(
            "Start Broadcast",
            on_press=self.start_broadcast,
            margin=5
        )

        main_box.add(details_box)
        main_box.add(state_box)
        main_box.add(broadcastbutton)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
    def start_broadcast_check(self):
        # Modify this to check APP ID, connection to RPC, and other things if needed
        print("testing shit")
        return("t")
    async def start_broadcast(self, widget):
        if self.start_broadcast_check() == "t":
            self.rpcstart()
            await self.main_window.dialog(
                toga.InfoDialog(
                    "Broadcast started",
                    "Close the window to end the broadcast",
                )
            )
        else:
            await self.main_window.dialog(
                toga.InfoDialog(
                    "Broadcast start failed",
                    "Error undefined"
                )
            )
        self.rpcterminate()
    def rpcstart(self):
        print("RPC session started")
    def rpcterminate(self):
        print("RPC Session ended")


def main():
    return VermillionRPC()
