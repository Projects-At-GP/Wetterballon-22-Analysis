import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime
from io import TextIOWrapper


__all__ = ("plot",)


def plot(
    file: TextIOWrapper,
    out: str,
    d_label: str,
    x_label: str,
    y_label: str,
    x_scale: str,
    y_scale: str,
    relational: bool,
    marker: str,
    marker_size: float,
    marker_width: float,
    marker_color: str,
    line_width: float,
    line_color: str,
    order: int,
    dpi: float,
    grid: bool,
    epoch: float,
) -> None:
    t, v = [], []

    print(f"reading {file.name!r}...")
    with file as f:
        keys = f.readline().removesuffix("\n").split(",")
        for line in f:
            res = line.removesuffix("\n").split(",")
            t.append(float(res[0]))
            if not relational:
                v.append(float(res[1]))
            else:
                v.append(list(map(float, res[1:])))

    if not out.endswith(".png"):
        out += ".png"
    print(f"creating {out!r}...")

    # time
    t_s, t_e = [datetime.fromtimestamp(t_ + epoch) for t_ in (t[0], t[-1])]
    plt.xlabel((x_label or keys[0]).title() + f" (from {t_s} to {t_e})")
    plt.xscale(x_scale)

    # value
    plt.ylabel((y_label or keys[1]).title())
    plt.yscale(y_scale)

    sns.regplot(
        x=t,
        y=v,
        label=d_label.title(),
        marker=marker,
        color=marker_color if not relational else None,
        order=order,
        line_kws={"color": line_color if not relational else None, "lw": line_width},
        scatter_kws={"s": marker_size, "lw": marker_width},
    )
    plt.legend()
    if grid:
        plt.grid()

    plt.savefig(out, dpi=dpi)
