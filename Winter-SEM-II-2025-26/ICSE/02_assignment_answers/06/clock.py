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
        return Clock(self.hours, self.minutes + minutes)

    def __str__(self) -> str:
        if self.minutes < 10:
            min = f"0{self.minutes}"
        else:
            min = f"{self.minutes}"
        str = f"{self.hours}:{min}"
        return str


if __name__ == "__main__":
    clock_1 = Clock(23, 00)
    clock_2 = Clock(23, 00)
    clock_3 = Clock(23, 00)
    clock_4 = Clock(23, 00)
    clock_5 = Clock(00, 00)
    assert clock_1 == clock_2
    assert (clock_3 + clock_4) == Clock(22, 00)
    assert clock_5.add_minutes(2) == Clock(0, 2)
    assert str(Clock(1, 30)) == "1:30"
    pass
