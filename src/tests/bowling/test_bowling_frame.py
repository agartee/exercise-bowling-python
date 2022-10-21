import pytest

from bowling.bowling_frame import BowlingFrame


def test_create_frame_with_second_throw_but_no_first():
    with pytest.raises(ValueError):
        BowlingFrame(second_throw=1)


def test_create_frame_with_second_throw_after_strike():
    with pytest.raises(ValueError):
        BowlingFrame(first_throw=10, second_throw=1)


@pytest.mark.parametrize("pins", [None, -1, 11, 5.5])
def test_record_throw_raises_exception_with_invalid_pins(pins):
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


def test_record_second_throw_exceeds_max_pins_in_frame_throws():
    frame = BowlingFrame(first_throw=9)

    with pytest.raises(ValueError):
        frame.record_throw(2)


def test_is_complete_when_second_throw_not_set_is_false():
    frame = BowlingFrame(first_throw=1)

    assert frame.is_complete == False


def test_is_complete_when_second_throw_set_is_true():
    frame = BowlingFrame(first_throw=1, second_throw=2)

    assert frame.is_complete == True


def test_is_complete_when_strike():
    frame = BowlingFrame(first_throw=10)

    assert frame.is_complete == True


def test_is_spare_with_no_throws():
    frame = BowlingFrame()

    assert frame.is_spare == False


def test_is_spare_with_one_throw():
    frame = BowlingFrame(first_throw=1)

    assert frame.is_spare == False


def test_is_spare_with_two_throws_but_not_10_pins():
    frame = BowlingFrame(first_throw=1, second_throw=2)

    assert frame.is_spare == False


def test_is_spare_with_two_throws_and_10_pins():
    frame = BowlingFrame(first_throw=9, second_throw=1)

    assert frame.is_spare == True


def test_is_strike_with_first_throw_10_pins():
    frame = BowlingFrame(first_throw=10)

    assert frame.is_strike == True


def test_is_strike_with_first_throw_not_10_pins():
    frame = BowlingFrame(first_throw=9)

    assert frame.is_strike == False


def test_frame_equality_with_equivalent_objects():
    frame1 = BowlingFrame(idx=1, first_throw=1, second_throw=1)
    frame2 = BowlingFrame(idx=1, first_throw=1, second_throw=1)

    assert frame1 == frame2


def test_frame_equality_with_non_equivalent_objects():
    frame = BowlingFrame(idx=1, first_throw=1, second_throw=1)

    assert not frame == "abc"
