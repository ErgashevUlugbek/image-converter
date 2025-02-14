class TextFormatter:
    selected_format = None
    def __init__(self):
        pass

    def set_format(self, selected_format: str = "underscore"):
        self.selected_format = selected_format

    def format(self, text, seperator):
        if self.selected_format == "underscore":
            self.do_underscore_formatting(text=text, seperator=seperator)

    def do_underscore_formatting(self, text: str, seperator: str):
        return text.lower().replace(seperator, '_')