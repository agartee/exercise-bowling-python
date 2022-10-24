from bowling import MAX_PINS_PER_THROW


class BowlingFrame:
    def __init__(
        self, idx=0, first_throw=None, second_throw=None, updating_callback=None
    ):
        Guard.against_non_sequential_throws(first_throw, second_throw)
        Guard.against_second_throw_after_strike(first_throw, second_throw)
        if first_throw:
            Guard.against_invalid_pins(first_throw)
        if second_throw:
            Guard.against_invalid_pins(second_throw)
            Guard.against_exceeding_allowed_pins_for_frame(first_throw, second_throw)

        self._idx = idx
        self._first_throw = first_throw
        self._second_throw = second_throw
        self._updating_callback = updating_callback

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
            and self.first_throw + self.second_throw == MAX_PINS_PER_THROW
        )

    @property
    def is_strike(self):
        return self.first_throw == MAX_PINS_PER_THROW

    def record_throw(self, pins):
        Guard.against_invalid_pins(pins)

        if self._updating_callback:
            self._updating_callback(self.idx)

        if self.first_throw is None:
            self._first_throw = pins
        else:
            Guard.against_exceeding_allowed_pins_for_frame(self.first_throw, pins)
            self._second_throw = pins

    def __eq__(self, other):
        if not isinstance(other, BowlingFrame):
            return False

        return (
            self.idx == other.idx
            and self.first_throw == other.first_throw
            and self.second_throw == other.second_throw
        )


class Guard:
    def against_non_sequential_throws(first_throw, second_throw):
        if first_throw is None and second_throw is not None:
            raise ValueError("Cannot initialize frame without sequential throws")

    def against_second_throw_after_strike(first_throw, second_throw):
        if first_throw == MAX_PINS_PER_THROW and second_throw is not None:
            raise ValueError("Cannot initialize frame with second throw after strike")

    def against_invalid_pins(pins):
        if pins not in range(0, 11):  # include 10
            raise ValueError(f"Invalid number of pins: {pins}")

    def against_exceeding_allowed_pins_for_frame(first_throw, second_throw):
        total = sum(filter(None, [first_throw, second_throw]))

        if total > MAX_PINS_PER_THROW:
            raise ValueError(f"Total pins for frame cannot exceed {MAX_PINS_PER_THROW}")
