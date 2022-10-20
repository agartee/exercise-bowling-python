from bowling.bowling_game import BowlingGame
from bowling.bowling_frame import BowlingFrame


def test_record_throw_stores_pins():
    game = BowlingGame()
    game.record_throw(5)

    frame = game.frames[0]
    assert frame == BowlingFrame(first_throw=5)


def test_game_throws_cannot_be_mutated_outside_game():
    game = BowlingGame()
    initial_frame_count = len(game.frames)

    game.frames.append(BowlingFrame())

    assert len(game.frames) == initial_frame_count


def test_game_records_throw_on_next_frame_when_frame_is_complete():
    game = BowlingGame()
    game.record_throw(1)
    game.record_throw(2)
    game.record_throw(3)

    second_frame = game.frames[1]
    assert second_frame.first_throw == 3
