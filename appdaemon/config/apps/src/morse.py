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
        self.flash_word(new_text)

    def flash_word(self, word):
        for letter in word.upper():
            self.flash_letter(letter)
            self.current += self.durations['interval_letters']

    def flash_letter(self, letter):
        code = morse[letter]
        i = 0
        for symbol in code:
            if symbol == '.':
                self.flash('short')
            elif symbol == '-':
                self.flash('long')
            else:
                raise ValueError(f"Unknown symbol: '{symbol}' in letter '{letter}")

            i += 1
            is_last_symbol = i == len(code)
            if not is_last_symbol:
                self.current += self.durations['interval_symbols']

    def flash(self, duration_key):
        start = self.current
        end = self.current + self.durations[duration_key]

        self.run_in(lambda _: self.turn_on('switch.demoswitch'), start)
        self.run_in(lambda _: self.turn_off('switch.demoswitch'), end)

        self.current = end
