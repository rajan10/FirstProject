from typing import Callable

def square(num: int) -> int:
    return num ** 2
def my_map(funct: Callable[[int], int], numbers: list[int]) -> list[int]:
    return [funct(num) for num in numbers]


print(my_map(funct=square, numbers=[1, 2, 3, 4, 5]))