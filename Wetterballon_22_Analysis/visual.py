import matplotlib.pyplot as plt

from io import TextIOWrapper


__all__ = ("plot",)


def plot(
    file: TextIOWrapper,
    out: TextIOWrapper,
) -> None:
    t, v = [], []

    print(f"reading {file.name!r}...")
    with file as f:
        keys = f.readline().removesuffix("\n").split(",")
        for line in f:
            res = line.removesuffix("\n").split(",")
            t.append(float(res[0]))
            v.append(float(res[1]))

    print(f"creating {out.name!r}...")

    plt.xlabel("Timestamp")
    plt.xscale("linear")

    plt.ylabel(keys[1].title())
    plt.yscale("linear")

    plt.plot(t, v)
    out_file = out.name
    if not out_file.endswith(".png"):
        out_file += ".png"
    plt.savefig(out_file)
