import appdaemon.plugins.hass.hassapi as hass


class LogText(hass.Hass):
    def initialize(self):
        self.listen_state(self.on_new_text, 'input_text.my_text')

    def on_new_text(self, _entity, _attribute, _old, new_text, _kwargs):
        self.log(f"Text updated on 'input_text.my_text' - New text: '{new_text}'")
