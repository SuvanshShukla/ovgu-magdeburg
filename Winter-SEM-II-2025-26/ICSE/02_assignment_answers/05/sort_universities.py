import random
from operator import attrgetter


class University:
    def __init__(self, name: str, founding_year: int, country: str) -> None:
        self.name = name
        self.founding_year = founding_year
        self.country = country

    def __repr__(self) -> str:
        return repr((self.name, self.founding_year, self.country))


if __name__ == "__main__":
    tmp_list = list(range(1000))
    random.shuffle(tmp_list)

    print(tmp_list.sort())
    print(sorted([5, 3, -2, 7, 6, 9, 1, -8, 4, 10, 2, 1, -1, 8]))

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

    # Sort universities by age
    print(sorted(universities, key=lambda university: university[1]))

    # Sort universities by name
    print(sorted(universities, key=lambda university: university[2]))
    print(universities)
    print('\n')
    # Stores the universities as `University` objects
    university_objects = [University(name=u[0], founding_year=u[1],
                                     country=u[2]) for u in universities]

    # Sort university_objects by age
    sorted(university_objects, key=attrgetter('founding_year'))

    # Sort university_objects by name
    sorted(university_objects, key=attrgetter('name'))
    print(university_objects)
