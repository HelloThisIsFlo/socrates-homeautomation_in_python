from appdaemontestframework import automation_fixture

from src.morse import MorseCode


@automation_fixture(MorseCode)
def morse_code():
    pass


class TestMorseCode:
    def test_listens_to_changes_in_morse_text(self, morse_code: MorseCode, assert_that):
        assert_that(morse_code) \
            .listens_to.state('input_text.morse') \
            .with_callback(morse_code.on_new_text)


