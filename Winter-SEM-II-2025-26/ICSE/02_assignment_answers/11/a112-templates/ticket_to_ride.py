from typing import List


def matrix_multiply(mat_0: List[List[int]], mat_1: List[List[int]]) -> List[List[int]]:
    """Multiplies matrix `mat_0` with `mat_1`."""

    # Check that the matrixes have the right dimensions
    assert all([len(mat_0) == len(mat_0[i]) for i in range(len(mat_0))])
    assert all([len(mat_1) == len(mat_1[i]) for i in range(len(mat_1))])
    assert len(mat_0[0]) == len(mat_1)

    mat_3 = [[0 for _ in range(len(mat_0))] for _ in range(len(mat_1[0]))]

    for i in range(len(mat_3)):
        for j in range(len(mat_3[0])):
            for k in range(len(mat_0[0])):
                mat_3[i][j] += mat_0[i][k] * mat_1[k][j]

    return mat_3


class TicketToRide:
    def __init__(self) -> None:
        self.cities: List[str] = []
        self.adjacency_matrix: List[List[int]] = [[]]

        raise NotImplementedError()  # TODO: populate self.cities

    def create_city_array(self) -> None:
        raise NotImplementedError()  # TODO: implement

    def city_to_index(self, city: str) -> int:
        raise NotImplementedError()  # TODO: implement

    def index_to_city(self, index: int) -> str:
        raise NotImplementedError()  # TODO: implement

    def create_adjacency_matrix(self) -> None:
        raise NotImplementedError()  # TODO: implement

    def get_connection_length(self, cityA: str, cityB: str) -> int:
        raise NotImplementedError()  # TODO: implement

    def get_connections(self, city: str) -> List[str]:
        raise NotImplementedError()  # TODO: implement

    def get_cycles_count(self, city: str, length: int) -> int:
        raise NotImplementedError()  # TODO: implement

    def get_total_cycles_count(self, length: int) -> int:
        raise NotImplementedError()  # TODO: implement

if __name__ == "__main__":
    pass
