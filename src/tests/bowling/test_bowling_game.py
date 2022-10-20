import pytest
from bowling.bowling_game import BowlingGame


def test_record_throw_stores_pins():
    game = BowlingGame()
    game.record_throw(5)

    assert len(game.throws) == 1
    assert game.throws[0] == 5


@pytest.mark.parametrize("pins", [-1, 11, 5.5])
def test_record_throw_raises_exception_with_invalid_pins(pins):
    game = BowlingGame()

    with pytest.raises(ValueError) as err:
        game.record_throw(pins)

    assert "Invalid number of pins" in str(err.value)


def test_game_throws_cannot_be_mutated_outside_game():
    game = BowlingGame()
    game.record_throw(5)
    game.throws.append(1)

    assert len(game.throws) == 1
    assert game.throws[0] == 5
