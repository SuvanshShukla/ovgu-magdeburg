import random


class University:
    def __init__(self, name: str, founding_year: int, country: str) -> None:
        self.name = name
        # TODO: Add the missing properties
        # ...

    def __repr__(self) -> str:
        return repr((self.name, self.founding_year, self.country))


if __name__ == "__main__":
    tmp_list = list(range(1000))
    random.shuffle(tmp_list)
    # TODO: Get familiar with pythons `sort` and `sorted`. Play around a bit
    # with list `tmp_list` and print the results.


    # Stores universities in the format (name, founding year, country)
    universities = [
        ("Otto-von-Guericke-Universität Magdeburg", 1993, "Germany"),
        ("Harvard University", 1636, "USA"),
        ("Technische Universität München", 1868, "Germany"),
        ("RWTH Aachen", 1870, "Germany"),
        ("京都大学", 1897, "Japan"),
        ("Massachusetts Institute of Technology", 1861, "USA"),
        ("Универзитет у Београду", 1808, "Serbia"),
        ("Eidgenössische Technische Hochschule", 1854, "Switzerland"),
        ("Indraprastha Institute of Information Technology", 2008, "India")
    ]

    # TODO: Sort universities by age

    # TODO: Sort universities by name


    # Stores the universities as `University` objects
    university_objects = [University(name=u[0], founding_year=u[1], country=u[2]) for u in universities]

    # TODO: Sort university_objects by age

    # TODO: Sort university_objects by name


