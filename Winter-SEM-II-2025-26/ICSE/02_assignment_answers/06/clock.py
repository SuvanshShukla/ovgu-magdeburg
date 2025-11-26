class Clock:
    def __eq__(self, other: object) -> bool:
        # if self and other are of different, incompatible types, they are not equal
        if not isinstance(other, Clock):  
            return NotImplemented

        # TODO: Compare self and other

    # TODO: Add implementation


if __name__ == "__main__":
    pass

# TODO: Remove all lines, that contain "# TODO:"...