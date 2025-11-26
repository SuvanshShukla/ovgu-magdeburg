class Clock:
    hours: int = 0
    minutes: int = 0

    def __init__(self, hours: int, minutes: int):
        total_min = (hours * 60) + minutes

        self.hours = (total_min // 60) % 24
        self.minutes = total_min % 60

    def __eq__(self, other: object) -> bool:
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

    def __str__(self) -> str:
        return f"{self.hours}:{self.minutes}"


if __name__ == "__main__":
    clock = Clock(23, 00)
    other_clock = Clock(23, 00)
    assert clock.__eq__(other_clock) is True
    assert clock.__add__(other_clock).__eq__(46, 00) is True
    assert clock.add_minutes(62) == Clock(1, 2)
    assert Clock(1, 30).__str__ == "1:30"
    pass

# TODO: Remove all lines, that contain "# TODO:"...