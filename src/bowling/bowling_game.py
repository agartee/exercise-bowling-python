from bowling.bowling_frame import BowlingFrame


class BowlingGame:
    def __init__(self):
        self._frames = []
        for i in range(0, 10):
            self._frames.append(BowlingFrame(idx=i))

        self._current_frame = self.frames[0]

    @property
    def frames(self):
        return self._frames.copy()

    @property
    def frame_scores(self):
        scores = []
        for frame in self.frames:
            if not frame.is_complete:
                scores.append(None)
            elif frame.is_strike:
                scores.append(self._calculate_strike_frame_score(frame))
            elif frame.is_spare:
                scores.append(self._calculate_spare_frame_score(frame))
            else:
                scores.append(frame.first_throw + frame.second_throw)

        return scores

    @property
    def total_score(self):
        frame_scores = [0 if score is None else score for score in self.frame_scores]
        return sum(frame_scores)

    def record_throw(self, pins):
        if self._current_frame.is_complete:
            self._current_frame = self.frames[self._current_frame.idx + 1]

        self._current_frame.record_throw(pins)

    def _calculate_spare_frame_score(self, frame):
        next_throw = self.frames[frame.idx + 1].first_throw
        if next_throw is None:
            return None

        return frame.first_throw + frame.second_throw + next_throw

    def _calculate_strike_frame_score(self, frame):
        next_frame = self.frames[frame.idx + 1]
        next_throw = next_frame.first_throw

        if next_throw is None:
            return None

        subsequent_throw = (
            self.frames[frame.idx + 2].first_throw
            if next_frame.is_strike
            else next_frame.second_throw
        )

        if subsequent_throw is None:
            return None

        return frame.first_throw + next_throw + subsequent_throw
