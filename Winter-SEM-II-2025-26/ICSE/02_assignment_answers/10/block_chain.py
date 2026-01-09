from dataclasses import dataclass
import hashlib


def bytes_to_bits(arr: bytes,) -> str:
    """
    Converts a byte object to a string containing the individual bits.

    This function pads the resulting string with leading 0s.

        E.g. bytes_to_bits(b'\x11') == "0000000100000001"
    """
    return ''.join(format(byte, '08b') for byte in arr)


@dataclass
class Block:
    def __init__(self, message: str, previousHashCode: bytes) -> None:
        self.message = message
        self.previousHashCode = previousHashCode
        self.proofOfWork = 0

    def hash(self) -> bytes:
        return NotImplementedError()  # TODO

    def __str__(self) -> str:
        return NotImplementedError()  # TODO


def number_of_leading_zeros(block: Block) -> int:
    return NotImplementedError()  # TODO


def verify(block: Block, x: int) -> bool:
    return NotImplementedError()  # TODO


def proof_of_work(block: Block, x: int) -> None:
    return NotImplementedError()  # TODO


if __name__ == "__main__":
    block = Block("Message", b'test')
    print(block, verify(block, 16))
    proof_of_work(block, 16)
    print(block, verify(block, 16))
