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

        # TODO: Compare self and other

    # TODO: Add implementation


if __name__ == "__main__":
    pass

# TODO: Remove all lines, that contain "# TODO:"...