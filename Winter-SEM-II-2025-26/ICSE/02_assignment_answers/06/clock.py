class Clock:
    hours: int = 0
    minutes: int = 0

    def __init__(self, hours: int, minutes: int):
        if hours > 24:
            self.hours = hours % 24
        else:
            self.hours = hours

        if minutes > 60:
            self.minutes = minutes % 60
        else:
            self.minutes = minutes

    def __eq__(self, other: object) -> bool:
        # if self and other are of different, incompatible types, they are not equal
        if not isinstance(other, Clock):
            return NotImplemented

        if other.hours == self.hours and other.minutes == self.minutes:
            return True
        else:
            return False

    def __add__(self, other: "Clock") -> "Clock":
        if self == other:
            self.hours = (self.hours + other.hours) % 24
            total_min = self.minutes + other.minutes
            self.minutes = total_min % 60

            if total_min > 60:
                self.hours += total_min // 60

            return self
        else:
            return NotImplemented

    def add_minutes(self, minutes: int) -> "Clock":
        self.minutes += minutes

        if self.minutes > 60:
            self.hours += minutes // 60
            self.minutes = self.minutes % 60

        return self


if __name__ == "__main__":
    clock = Clock(23, 00)
    other_clock = Clock(23, 00)
    assert clock.__eq__(other_clock) is True
    assert clock.__add__(other_clock).__eq__(46, 00) is True
    assert clock.add_minutes(62) == Clock(1, 2)
    pass

# TODO: Remove all lines, that contain "# TODO:"...