import matplotlib.pyplot as plt
import seaborn as sns

from io import TextIOWrapper


__all__ = ("plot",)


def plot(
    file: TextIOWrapper,
    out: TextIOWrapper,
    median_label: str,
    x_label: str,
    y_label: str,
    x_scale: str,
    y_scale: str,
    marker: str,
    order: int,
    dpi: float,
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

    plt.xlabel((x_label or keys[0]).title())
    plt.xscale(x_scale)

    plt.ylabel((y_label or keys[1]).title())
    plt.yscale(y_scale)

    sns.regplot(
        x=t,
        y=v,
        label=median_label,
        marker=marker,
        order=order,
        line_kws={"color": "red"},
    )
    plt.legend()

    out_file = out.name
    if not out_file.endswith(".png"):
        out_file += ".png"
    plt.savefig(out_file, dpi=dpi)
