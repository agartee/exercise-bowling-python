from bowling import MAX_PINS_PER_THROW


class LastBowlingFrame:
    def __init__(self, idx=0, first_throw=None, second_throw=None, third_throw=None):
        Guard.against_non_sequential_throws(first_throw, second_throw, third_throw)
        if first_throw:
            Guard.against_invalid_pins(first_throw)
        if second_throw:
            Guard.against_invalid_pins(second_throw)
        if third_throw:
            Guard.against_invalid_pins(third_throw)
            Guard.against_third_throw_if_not_allowed(first_throw, second_throw)

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

        return (
            third_throw_not_allowed(self._first_throw, self.second_throw)
            or self.third_throw is not None
        )

    def record_throw(self, pins):
        Guard.against_invalid_pins(pins)
        Guard.against_third_throw_if_not_allowed(self.first_throw, self.second_throw)

        if self.first_throw is None:
            self._first_throw = pins
        elif self.second_throw is None:
            self._second_throw = pins
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


class Guard:
    def against_non_sequential_throws(first_throw, second_throw, third_throw):
        if (first_throw is None and second_throw is not None) or (
            second_throw is None and third_throw is not None
        ):
            raise ValueError("Cannot initialize frame without sequential throws")

    def against_third_throw_if_not_allowed(first_throw, second_throw):
        if second_throw is not None and third_throw_not_allowed(
            first_throw, second_throw
        ):
            raise ValueError(
                "Third throw not allowed without preceding strikes or spare"
            )

    def against_invalid_pins(pins):
        if pins not in range(0, 11):  # include 10
            raise ValueError(f"Invalid number of pins: {pins}")


def third_throw_not_allowed(first_throw, second_throw):
    return first_throw + second_throw not in [
        MAX_PINS_PER_THROW,
        MAX_PINS_PER_THROW * 2,
    ]
