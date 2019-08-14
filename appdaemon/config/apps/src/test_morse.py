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


@pytest.fixture
def assert_flashed_for(given_that, assert_that, time_travel):
    def do_assert_flashed_for(duration):
        # T=t              - Light ON
        # T=t+(duration-1) - Light NOT OFF YET
        # T=t+duration     - Light OFF

        # T=t - Light ON
        assert_that('switch.demoswitch').was.turned_on()

        # T=t+(duration-1) - Light NOT OFF YET
        time_travel.fast_forward(duration - 1).seconds()
        assert_that('switch.demoswitch').was_not.turned_off()

        # T=t+duration - Light OFF
        time_travel.fast_forward(1).seconds()
        assert_that('switch.demoswitch').was.turned_off()

    return do_assert_flashed_for


class TestMorseCode:
    def test_listens_to_changes_in_morse_text(self, morse_code: MorseCode, assert_that):
        assert_that(morse_code) \
            .listens_to.state('input_text.morse') \
            .with_callback(morse_code.on_new_text)

    def test_short_letter(self, mock_duration, on_new_text, assert_flashed_for, time_travel):
        # Sanity check
        assert morse['E'] == '.'

        # Given: Duration for short letter == 2s
        mock_duration(short=2, long=4, between_symbols=10, between_letters=20)

        # When: Receiving short letter
        on_new_text('E')

        # Then: Light turned on for short duration
        time_travel.fast_forward(1).seconds()  # First symbol starts after 1sec
        assert_flashed_for(2)

    def test_long_letter(self, mock_duration, on_new_text, assert_flashed_for, time_travel):
        # Sanity check
        assert morse['T'] == '-'

        # Given: Duration for long letter == 4s
        mock_duration(short=2, long=4, between_symbols=10, between_letters=20)

        # When: Receiving long letter
        on_new_text('T')

        # Then: Light turned on for long duration
        time_travel.fast_forward(1).seconds()  # First symbol starts after 1sec
        assert_flashed_for(4)
