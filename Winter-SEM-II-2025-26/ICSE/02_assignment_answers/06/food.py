class Food:
    def __init__(self):
        self.weight = -1
        self.amount = -1
        self.volume = -1

    def calories(self) -> int:
        raise NotImplementedError()

    def get_weight(self):
        raise NotImplementedError()

    def __eq__(self, other) -> bool:
        if not isinstance(other, Food):
            return NotImplemented
        if self.calories() == other.calories():
            return True
        else:
            return False

    def __lt__(self, other) -> bool:
        if not isinstance(other, Food):
            return NotImplemented
        cal1 = self.calories()
        cal2 = other.calories()
        if cal1 > cal2:
            return False
        else:
            return True


class Apples(Food):
    def __init__(self, amount):
        self.weight = 0
        self.amount = amount
        self.volume = -1

    def calories(self) -> int:
        return 108 * self.amount

    def get_weight(self):
        return 200 * self.amount


class Oranges(Food):
    def __init__(self, amount):
        self.weight = 0
        self.amount = amount
        self.volume = -1

    def calories(self) -> int:
        return 95 * self.amount

    def get_weight(self):
        return 200 * self.amount


class CookieDough(Food):
    def __init__(self, weight):
        self.weight = weight
        self.amount = 0
        self.volume = -1

    def calories(self) -> int:
        return int(389 * self.weight)

    def get_weight(self):
        return self.weight


class OrangeJuice(Food):
    def __init__(self, volume):
        self.weight = 0
        self.amount = 0
        self.volume = volume

    def calories(self) -> int:
        return int(42 * self.volume / 100)

    def get_weight(self):
        return 1.038 * self.volume


class Bread(Food):
    def __init__(self, amount):
        self.weight = -1
        self.amount = amount
        self.volume = -1

    def calories(self) -> int:
        return int(66 * self.amount)

    def get_weight(self):
        return 25 * self.amount


class Pizza(Food):
    def __init__(self, amount):
        self.weight = -1
        self.amount = amount
        self.volume = -1

    def calories(self) -> int:
        return int(200 * self.amount)

    def get_weight(self):
        return 200 * self.amount


if __name__ == "__main__":
    apple = Apples(1)
    apple2 = Apples(2)
    cal1 = apple2.calories
    cal2 = apple.calories
    assert apple < apple2
    orange = Oranges(1)
    orange2 = Oranges(1)
    assert orange == orange2
    oj = OrangeJuice(1)
    oj2 = OrangeJuice(1)
    assert oj2.get_weight() == (1.038 * 1)
    print("ALL TESTS PASSED!")
    pass

