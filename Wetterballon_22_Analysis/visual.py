import matplotlib.pyplot as plt

from io import TextIOWrapper


__all__ = ("plot",)


def plot(
    file: TextIOWrapper,
) -> None:
    print(f"{file.name} was plotted...")
