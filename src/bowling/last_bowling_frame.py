class LastBowlingFrame:
    def __init__(self, idx=0, first_throw=None, second_throw=None, third_throw=None):
        if (first_throw is None and second_throw is not None) or (
            second_throw is None and third_throw is not None
        ):
            raise ValueError("Cannot initialize last frame without sequential throws")

        if (
            second_throw is not None
            and first_throw + second_throw not in [10, 20]
            and third_throw is not None
        ):
            raise ValueError(
                "Cannot initialize with third throw without preceding strikes or spare"
            )

        self._idx = idx
        self._first_throw = first_throw
        self._second_throw = second_throw
        self._third_throw = third_throw

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
    def third_throw(self):
        return self._third_throw

    @property
    def is_complete(self):
        if self.second_throw is None:
            return False

        return self.first_throw + self.second_throw not in [10, 20] or (
            self.first_throw + self.second_throw in [10, 20]
            and self.third_throw is not None
        )

    def record_throw(self, pins):
        if pins not in range(0, 11):  # include 10
            raise ValueError(f"Invalid number of pins: {pins}")

        if self._first_throw is None:
            self._first_throw = pins
        elif self._second_throw is None:
            self._second_throw = pins
        elif self._first_throw + self._second_throw not in [10, 20]:
            raise ValueError(
                "Cannot make third throw without preceding strikes or spare"
            )
        else:
            self._third_throw = pins

    def __eq__(self, other):
        if not isinstance(other, LastBowlingFrame):
            return False

        return (
            self.idx == other.idx
            and self.first_throw == other.first_throw
            and self.second_throw == other.second_throw
            and self.third_throw == other.third_throw
        )
