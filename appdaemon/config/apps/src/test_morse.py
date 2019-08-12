from appdaemontestframework import automation_fixture

from src.morse import MorseCode


@automation_fixture(MorseCode)
def morse_code():
    pass


class TestMorseCode:
    def test_say_hi(self, morse_code: MorseCode):
        assert morse_code.say_hi() == 'hi'
