import appdaemon.plugins.hass.hassapi as hass


class MorseCode(hass.Hass):
    def initialize(self):
        self.log('MorseCode was initialized')

    def say_hi(self):
        return 'hi'
