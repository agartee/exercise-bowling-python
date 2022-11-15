import pytest

from bowling.bowling_frame import BowlingFrame


def test_create_frame_with_second_throw_but_no_first_raises_error():
    with pytest.raises(ValueError) as err:
        BowlingFrame(second_throw=1)

    assert "Cannot initialize frame without sequential throws" in str(err.value)


def test_create_frame_with_second_throw_after_strike_raises_error():
    with pytest.raises(ValueError) as err:
        BowlingFrame(first_throw=10, second_throw=1)

    assert "Cannot initialize frame with second throw after strike" in str(err.value)


@pytest.mark.parametrize("pins", [-1, 11, 5.5])
def test_create_frame_with_invalid_pins_in_first_throw_raises_error(pins):
    with pytest.raises(ValueError) as err:
        BowlingFrame(first_throw=pins)

    assert "Invalid number of pins" in str(err.value)


@pytest.mark.parametrize("pins", [-1, 11, 5.5])
def test_create_frame_with_invalid_pins_in_second_throw_raises_error(pins):
    with pytest.raises(ValueError) as err:
        BowlingFrame(first_throw=0, second_throw=pins)

    assert "Invalid number of pins" in str(err.value)


def test_create_frame_with_too_many_total_pins_raises_error():
    with pytest.raises(ValueError) as err:
        BowlingFrame(first_throw=9, second_throw=9)

    assert "Total pins for frame cannot exceed 10" in str(err.value)


@pytest.mark.parametrize("pins", [None, -1, 11, 5.5])
def test_record_throw_raises_exception_with_invalid_pins_raises_error(pins):
    frame = BowlingFrame()

    with pytest.raises(ValueError) as err:
        frame.record_throw(pins)

    assert "Invalid number of pins" in str(err.value)


def test_record_single_throw_recorded_as_first_throw():
    frame = BowlingFrame()
    frame.record_throw(1)

    assert frame.first_throw == 1
    assert frame.second_throw == None


def test_record_second_throw_recorded_as_second():
    frame = BowlingFrame(first_throw=1)
    frame.record_throw(2)

    assert frame.second_throw == 2


def test_record_second_throw_exceeds_max_pins_in_frame_raises_error():
    frame = BowlingFrame(first_throw=9)

    with pytest.raises(ValueError) as err:
        frame.record_throw(2)

    assert "Total pins for frame cannot exceed 10" in str(err.value)


def test_is_complete_when_second_throw_not_set_returns_false():
    frame = BowlingFrame(first_throw=1)

    assert frame.is_complete == False


def test_is_complete_when_second_throw_set_returns_true():
    frame = BowlingFrame(first_throw=1, second_throw=2)

    assert frame.is_complete == True


def test_is_complete_when_strike_returns_true():
    frame = BowlingFrame(first_throw=10)

    assert frame.is_complete == True


def test_is_spare_with_no_throws_returns_false():
    frame = BowlingFrame()

    assert frame.is_spare == False


def test_is_spare_with_one_throw_returns_false():
    frame = BowlingFrame(first_throw=1)

    assert frame.is_spare == False


def test_is_spare_with_two_throws_but_not_10_pins_returns_false():
    frame = BowlingFrame(first_throw=1, second_throw=2)

    assert frame.is_spare == False


def test_is_spare_with_two_throws_and_10_pins_returns_true():
    frame = BowlingFrame(first_throw=9, second_throw=1)

    assert frame.is_spare == True


def test_is_strike_with_first_throw_10_pins_returns_true():
    frame = BowlingFrame(first_throw=10)

    assert frame.is_strike == True


def test_is_strike_with_first_throw_not_10_pins_returns_false():
    frame = BowlingFrame(first_throw=9)

    assert frame.is_strike == False


def test_frame_equality_with_equivalent_objects_is_equal():
    frame1 = BowlingFrame(idx=1, first_throw=1, second_throw=1)
    frame2 = BowlingFrame(idx=1, first_throw=1, second_throw=1)

    assert frame1 == frame2


def test_frame_equality_with_non_equivalent_objects_is_not_equal():
    frame = BowlingFrame(idx=1, first_throw=1, second_throw=1)

    assert not frame == "abc"
