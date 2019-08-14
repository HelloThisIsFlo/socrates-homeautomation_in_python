import pytest
from appdaemontestframework import automation_fixture

from src.morse import MorseCode, morse


@automation_fixture(MorseCode)
def morse_code():
    pass


@pytest.fixture
def on_new_text(morse_code: MorseCode):
    return lambda new_text: morse_code.on_new_text(None, None, None, new_text, None)


@pytest.fixture
def mock_duration(given_that):
    def do_mock_duration(short, long, between_symbols, between_letters):
        def to_float_str(number):
            return str(number) + '.0'

        given_that.state_of('input_number.morse_short').is_set_to(to_float_str(short))
        given_that.state_of('input_number.morse_long').is_set_to(to_float_str(long))
        given_that.state_of('input_number.morse_interval_symbols').is_set_to(to_float_str(between_symbols))
        given_that.state_of('input_number.morse_interval_letters').is_set_to(to_float_str(between_letters))

    return do_mock_duration


class TestMorseCode:
    def test_listens_to_changes_in_morse_text(self, morse_code: MorseCode, assert_that):
        assert_that(morse_code) \
            .listens_to.state('input_text.morse') \
            .with_callback(morse_code.on_new_text)

    def test_short_letter(self, mock_duration, on_new_text, assert_that, time_travel):
        # Sanity check
        assert morse['E'] == '.'

        # Given: Duration for short letter == 2s
        mock_duration(short=2, long=4, between_symbols=10, between_letters=20)

        # When: Receiving short letter
        on_new_text('E')

        # Then: Light turned on for short duration
        #
        # T=0 Nothing happens
        # T=1 Light should turn on
        # T=3 Light should turn off (T=1 + short_duration=2)
        time_travel.assert_current_time(0)
        assert_that('switch.demoswitch').was_not.turned_on()

        time_travel.fast_forward(1).seconds()
        time_travel.assert_current_time(1)
        assert_that('switch.demoswitch').was.turned_on()

        time_travel.fast_forward(1).seconds()
        time_travel.assert_current_time(2)
        assert_that('switch.demoswitch').was_not.turned_off()

        time_travel.fast_forward(1).seconds()
        time_travel.assert_current_time(3)
        assert_that('switch.demoswitch').was.turned_off()

    def test_long_letter(self, mock_duration, on_new_text, assert_that, time_travel):
        # Sanity check
        assert morse['T'] == '-'

        # Given: Duration for long letter == 4s
        mock_duration(short=2, long=4, between_symbols=10, between_letters=20)

        # When: Receiving long letter
        on_new_text('T')

        # Then: Light turned on for long duration
        #
        # T=0 Nothing happens
        # T=1 Light should turn on
        # T=5 Light should turn off (T=1 + long_duration=4)
        time_travel.assert_current_time(0)
        assert_that('switch.demoswitch').was_not.turned_on()

        time_travel.fast_forward(1).seconds()
        time_travel.assert_current_time(1)
        assert_that('switch.demoswitch').was.turned_on()

        time_travel.fast_forward(3).seconds()
        time_travel.assert_current_time(4)
        assert_that('switch.demoswitch').was_not.turned_off()

        time_travel.fast_forward(1).seconds()
        time_travel.assert_current_time(5)
        assert_that('switch.demoswitch').was.turned_off()
