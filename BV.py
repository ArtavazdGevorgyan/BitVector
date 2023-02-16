import numpy as np


class BitVector:
    def __init__(self, length: int):
        """
        Args:
            length (int): length of BitVector
        """
        self.__arr = np.zeros((length+63)//64, dtype=np.uint64)

    def __repr__(self) -> str:
        return f"{self.__arr[::-1]}"

    def set(self, index: int) -> None:
        """Changes index of a BitVector to 1

        Args:
            index (int): the index of BitVector to be modified
        """
        self.__arr[index // 64] |= np.uint64(1 << (index % 64))

    def reset(self, index: int) -> None:
        """Changes index of a BitVector to 0

        Args:
            index (int): the index of BitVector to be modified
        """
        self.__arr[index // 64] ^= np.uint64(1 << (index % 64))
