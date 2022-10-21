class BowlingFrame:
    def __init__(self, idx=0, first_throw=None, second_throw=None):
        if first_throw is None and second_throw is not None:
            raise ValueError("Cannot initialize frame with second throw only")

        if first_throw == 10 and second_throw is not None:
            raise ValueError("Cannot initialize frame with second throw after strike")

        self._idx = idx
        self._first_throw = first_throw
        self._second_throw = second_throw

    @property
    def idx(self):
        return self._idx

    @property
    def first_throw(self):
        return self._first_throw

    @property
    def second_throw(self):
        return self._second_throw

    @property
    def is_complete(self):
        return self.is_strike or self.second_throw is not None

    @property
    def is_spare(self):
        return (
            self.first_throw is not None
            and self.second_throw is not None
            and self.first_throw + self.second_throw == 10
        )

    @property
    def is_strike(self):
        return self.first_throw == 10

    def record_throw(self, pins):
        if pins not in range(0, 11):  # include 10
            raise ValueError(f"Invalid number of pins: {pins}")

        if self._first_throw is None:
            self._first_throw = pins
        elif self._first_throw + pins > 10:
            raise ValueError(f"Total pins for frame cannot exceed 10")
        else:
            self._second_throw = pins

    def __eq__(self, other):
        if not isinstance(other, BowlingFrame):
            return False

        return (
            self.idx == other.idx
            and self.first_throw == other.first_throw
            and self.second_throw == other.second_throw
        )
