class BowlingGame:
    def __init__(self):
        self._throws = []

    @property
    def throws(self):
        return self._throws.copy()

    def record_throw(self, pins):
        if pins not in range(0, 10):
            raise ValueError(f"Invalid number of pins: {pins}")

        self._throws.append(pins)
