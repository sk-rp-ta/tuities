from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

class Tuities(App):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

    def on_key(self, event):
        if event.key == "ctrl+c":
            self.exit()