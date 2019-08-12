import appdaemon.plugins.hass.hassapi as hass


class MorseCode(hass.Hass):
    def initialize(self):
        self.log('MorseCode was initialized')
        self.listen_state(self.on_new_text, 'input_text.morse')

    def on_new_text(self, _entity, _attribute, _old, new_text, _kwargs):
        pass
