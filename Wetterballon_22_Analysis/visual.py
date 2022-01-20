import matplotlib.pyplot as plt

from io import TextIOWrapper
from .data import str_to_dict


__all__ = ("plot",)


def plot(
    file: TextIOWrapper,
) -> None:
    with file as f:
        keys = f.readline().removesuffix("\n").split(",")
        for _ in range(10):
            print(str_to_dict(f.readline().removesuffix("\n"), *keys))
