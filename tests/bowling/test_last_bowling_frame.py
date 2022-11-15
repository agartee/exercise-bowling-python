import pytest

from bowling.last_bowling_frame import LastBowlingFrame


def test_create_last_frame_with_second_throw_but_no_first_raises_error():
    with pytest.raises(ValueError) as err:
        LastBowlingFrame(second_throw=2)

    assert "Cannot initialize frame without sequential throws" in str(err.value)


def test_create_last_frame_with_third_throw_but_no_second_raises_error():
    with pytest.raises(ValueError) as err:
        LastBowlingFrame(first_throw=1, third_throw=2)

    assert "Cannot initialize frame without sequential throws" in str(err.value)


@pytest.mark.parametrize("pins", [-1, 11, 5.5])
def test_create_last_frame_with_invalid_pins_in_first_throw_raises_error(pins):
    with pytest.raises(ValueError) as err:
        LastBowlingFrame(first_throw=pins)

    assert "Invalid number of pins" in str(err.value)


@pytest.mark.parametrize("pins", [-1, 11, 5.5])
def test_create_last_frame_with_invalid_pins_in_second_throw_raises_error(pins):
    with pytest.raises(ValueError) as err:
        LastBowlingFrame(first_throw=10, second_throw=pins)

    assert "Invalid number of pins" in str(err.value)


@pytest.mark.parametrize("pins", [-1, 11, 5.5])
def test_create_last_frame_with_invalid_pins_in_third_throw_raises_error(pins):
    with pytest.raises(ValueError) as err:
        LastBowlingFrame(first_throw=10, second_throw=10, third_throw=pins)

    assert "Invalid number of pins" in str(err.value)


def test_create_last_frame_with_third_throw_after_no_strike_or_spare_raises_error():
    with pytest.raises(ValueError) as err:
        LastBowlingFrame(first_throw=1, second_throw=2, third_throw=10)

    expected = "Third throw not allowed without preceding strikes or spare"
    assert expected in str(err.value)


@pytest.mark.parametrize("pins", [None, -1, 11, 5.5])
def test_record_throw_raises_exception_with_invalid_pins_raises_error(pins):
    frame = LastBowlingFrame()

    with pytest.raises(ValueError) as err:
        frame.record_throw(pins)

    assert "Invalid number of pins" in str(err.value)


def test_record_single_throw_recorded_as_first_throw():
    frame = LastBowlingFrame()
    frame.record_throw(1)

    assert frame.first_throw == 1
    assert frame.second_throw == None


def test_record_second_throw_recorded_as_second():
    frame = LastBowlingFrame(first_throw=1)
    frame.record_throw(2)

    assert frame.second_throw == 2


def test_record_third_throw_recorded_as_third_with_preceding_strikes():
    frame = LastBowlingFrame(first_throw=10, second_throw=10)
    frame.record_throw(1)

    assert frame.third_throw == 1


def test_record_third_throw_recorded_as_third_with_preceding_spare():
    frame = LastBowlingFrame(first_throw=9, second_throw=1)
    frame.record_throw(1)

    assert frame.third_throw == 1


def test_record_third_throw_with_no_preceding_spare_or_strikes_raises_error():
    frame = LastBowlingFrame(first_throw=1, second_throw=2)

    with pytest.raises(ValueError) as err:
        frame.record_throw(1)

    expected_msg = "Third throw not allowed without preceding strikes or spare"
    assert expected_msg in str(err.value)


def test_is_complete_with_no_throws_returns_false():
    frame = LastBowlingFrame()

    assert frame.is_complete == False


def test_is_complete_with_one_throw_returns_false():
    frame = LastBowlingFrame(first_throw=10)

    assert frame.is_complete == False


def test_is_complete_with_two_throws_without_strikes_or_spare_returns_true():
    frame = LastBowlingFrame(first_throw=1, second_throw=1)

    assert frame.is_complete == True


def test_is_complete_with_two_throws_with_spare_returns_false():
    frame = LastBowlingFrame(first_throw=5, second_throw=5)

    assert frame.is_complete == False


def test_is_complete_with_two_throws_with_strikes_returns_false():
    frame = LastBowlingFrame(first_throw=10, second_throw=10)

    assert frame.is_complete == False


def test_is_complete_with_three_throws_with_spare_returns_true():
    frame = LastBowlingFrame(first_throw=5, second_throw=5, third_throw=10)

    assert frame.is_complete == True


def test_is_complete_with_three_throws_with_strikes_returns_true():
    frame = LastBowlingFrame(first_throw=10, second_throw=10, third_throw=10)

    assert frame.is_complete == True


def test_last_frame_equality_with_equivalent_objects_is_equal():
    frame1 = LastBowlingFrame(idx=1, first_throw=10, second_throw=10, third_throw=10)
    frame2 = LastBowlingFrame(idx=1, first_throw=10, second_throw=10, third_throw=10)

    assert frame1 == frame2


def test_last_frame_equality_with_non_equivalent_objects_is_not_equal():
    frame = LastBowlingFrame(idx=1, first_throw=10, second_throw=10, third_throw=10)

    assert not frame == "abc"
