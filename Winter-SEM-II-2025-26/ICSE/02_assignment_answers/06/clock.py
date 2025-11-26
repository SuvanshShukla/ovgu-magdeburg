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
        if not isinstance(other, Clock):
            return NotImplemented

        return Clock(self.hours + other.hours,
                     self.minutes + other.minutes)

    def add_minutes(self, minutes: int) -> "Clock":
        total_min = (self.hours * 60) + minutes
        self.hours = (total_min // 60) % 24
        self.minutes = total_min % 60

    def __str__(self) -> str:
        if self.minutes < 10:
            min = f"0{self.minutes}"
        else:
            min = f"{self.minutes}"
        str = f"{self.hours}:{min}"
        return str


if __name__ == "__main__":
    clock = Clock(23, 00)
    other_clock = Clock(23, 00)
    assert clock.__eq__(other_clock) is True
    assert clock.__add__(other_clock).__eq__(46, 00) is True
    assert clock.add_minutes(62) == Clock(1, 2)
    assert Clock(1, 30).__str__ == "1:30"
    pass

# TODO: Remove all lines, that contain "# TODO:"...