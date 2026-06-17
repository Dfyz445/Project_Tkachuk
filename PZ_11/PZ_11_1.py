#В последовательности на и целых элементов найти произведение элементов средней трети.

from math import prod
from typing import List, Optional

data: List[int] = [2, 5, 1, 8, 3, 9, 4, 7, 6, 10, 12, 15]

def middle_third_product(seq: List[int]) -> Optional[int]:
    n = len(seq)
    if n < 3:
        return None
    part_size = n // 3

    start = part_size
    end = n - part_size
    middle = [seq[i] for i in range(start, end)]

    return prod(middle)

print("Исходная последовательность:", data)
print("Произведение элементов средней трети:", middle_third_product(data))