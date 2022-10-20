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

    def record_throw(self, pins):
        if self._current_frame.is_complete:
            self._current_frame = self.frames[self._current_frame.idx + 1]

        self._current_frame.record_throw(pins)
