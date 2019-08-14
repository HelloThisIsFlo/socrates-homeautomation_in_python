import appdaemon.plugins.hass.hassapi as hass

morse = {'A': '.-',
         'B': '-...',
         'C': '-.-.',
         'D': '-..',
         'E': '.',
         'F': '..-.',
         'G': '--.',
         'H': '....',
         'I': '..',
         'J': '.---',
         'K': '-.-',
         'L': '.-..',
         'M': '--',
         'N': '-.',
         'O': '---',
         'P': '.--.',
         'Q': '--.-',
         'R': '.-.',
         'S': '...',
         'T': '-',
         'U': '..-',
         'V': '...-',
         'W': '.--',
         'X': '-..-',
         'Y': '-.--',
         'Z': '--..'}


class MorseCode(hass.Hass):
    durations = None
    current = None

    def initialize(self):
        self.log('MorseCode was initialized')
        self.listen_state(self.on_new_text, 'input_text.morse')
        self.durations = dict()

    def _update_config(self):
        self.durations['short'] = float(self.get_state('input_number.morse_short'))
        self.durations['long'] = float(self.get_state('input_number.morse_long'))
        self.durations['interval_symbols'] = float(self.get_state('input_number.morse_interval_symbols'))
        self.durations['interval_letters'] = float(self.get_state('input_number.morse_interval_letters'))

    def on_new_text(self, _entity, _attribute, _old, new_text, _kwargs):
        self._update_config()
        self.current = 1
        if new_text == 'E':
            self.short()
        else:
            self.long()

    def short(self):
        self._turn_on_then_off('short')

    def long(self):
        self._turn_on_then_off('long')

    def _turn_on_then_off(self, duration_key):
        start = self.current
        end = self.current + self.durations[duration_key]
        next = end + self.durations['interval_symbols']

        self.run_in(lambda _: self.turn_on('switch.demoswitch'), start)
        self.run_in(lambda _: self.turn_off('switch.demoswitch'), end)

        self.current = next
