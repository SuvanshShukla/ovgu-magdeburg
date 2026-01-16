# create class polymorphie

class Robot:

    def __init__(self, name: str):
        self.name = name

    def info(self):
        print("This a Robot with name: ", self.name)


class Pet:

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    def details(self):
        print("This is a ", self.type, "it's name is: ", self.name)


class Agent(Robot):

    def info(self):
        print("This is an Agent with name: ", self.name)


class RoboDog(Robot, Pet):

    def __init__(self, name, type):
        Robot.__init__(self, name)
        Pet.__init__(self, name, type)

    def details(self):
        return super().details()


class Animal:

    def __init__(self, genus: str):
        self.genus = genus

    def get_genus(self):
        print("The genus is: ", self.genus)


class Catlike(Animal):

    def __init__(self, genus):
        super().__init__(genus)
        self.has_claws = True

    def has_claws(self):
        return True


class Cat(Animal, Catlike):

    def __init__(self, genus):
        super().__init__(genus)


if __name__ == "__main__":
    rob = RoboDog("larry", "robot dog")
    rob.details()
    ag = Agent("name")
    ag.info()
