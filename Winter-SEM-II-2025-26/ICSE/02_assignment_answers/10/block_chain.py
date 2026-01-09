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
        encoded_str = (self.message + str(self.proofOfWork) + str(self.previousHashCode)).encode()
        return hashlib.sha256(encoded_str).digest()

    def __str__(self) -> str:
        return ("Message: " + str(self.message) + '\n'
                "Previous HashCode: " + str(self.previousHashCode) + '\n'
                "Proof Of Work: " + str(self.proofOfWork) + '\n')


def number_of_leading_zeros(block: Block) -> int:
    hash_bits = bytes_to_bits(block.hash())
    zero_count = 0
    for bit in hash_bits:
        if bit == '0':
            zero_count += 1
        if bit != '0':
            break
    return zero_count


def verify(block: Block, x: int) -> bool:
    if number_of_leading_zeros(block) == x:
        return True
    else:
        return False


def proof_of_work(block: Block, x: int) -> None:
    zero_count = number_of_leading_zeros(block)
    if zero_count == x:
        block.proofOfWork = zero_count


if __name__ == "__main__":
    block = Block("Message", b'test')
    print(block, verify(block, 16))
    proof_of_work(block, 16)
    print(block, verify(block, 16))
