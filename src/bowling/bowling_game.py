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
            if frame.first_throw is None:
                scores.append(None)
                continue

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
