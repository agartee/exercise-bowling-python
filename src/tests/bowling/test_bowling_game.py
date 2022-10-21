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


def test_frame_scores_with_no_throws():
    game = BowlingGame()

    result = game.frame_scores
    assert result == [None] * 10


def test_frame_scores_with_one_frame_and_no_bonus():
    game = BowlingGame()
    game.record_throw(1)
    game.record_throw(2)

    result = game.frame_scores
    assert result == [3] + [None] * 9


def test_total_score_with_one_frame_and_no_bonuses():
    game = BowlingGame()
    game.record_throw(1)
    game.record_throw(2)

    result = game.total_score
    assert result == 3


def test_frame_score_with_spare_and_no_following_throw():
    game = BowlingGame()
    game.record_throw(9)
    game.record_throw(1)

    result = game.frame_scores
    assert result == [None] * 10


def test_total_score_with_spare_and_no_following_throw():
    game = BowlingGame()
    game.record_throw(9)
    game.record_throw(1)

    result = game.total_score
    assert result == 0


def test_frame_score_with_spare_and_following_throw():
    game = BowlingGame()
    game.record_throw(9)
    game.record_throw(1)
    game.record_throw(2)  # incomplete frame

    result = game.frame_scores
    assert result == [12] + [None] * 9


def test_total_score_with_spare_and_following_throw():
    game = BowlingGame()
    game.record_throw(9)
    game.record_throw(1)
    game.record_throw(2)  # incomplete frame

    result = game.total_score
    assert result == 12
