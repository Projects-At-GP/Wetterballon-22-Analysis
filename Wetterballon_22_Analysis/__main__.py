import argparse

from Wetterballon_22_Analysis import plot


parser = argparse.ArgumentParser()

parser.add_argument(
    "-s",
    "--source",
    help="The path to the source-file.",
    type=argparse.FileType(mode="r", encoding="utf-8"),
    dest="file",
    required=True,
)
parser.add_argument(
    "-o",
    "--out",
    help="The path for the output-file.",
    type=argparse.FileType(mode="w", encoding="utf-8"),
    dest="out",
    default="out",
)
parser.add_argument(
    "-m",
    "--mode",
    help="The mode to process the data.",
    dest="mode",
    default="plot",
    choices=["plot"],
)
parser.add_argument(
    "-ml",
    "--median-label",
    help="The label for the median.",
    type=str,
    dest="mlabel",
    required=True,
)
parser.add_argument(
    "-yl",
    "--y-label",
    help="The label for the y-axis.",
    type=str,
    dest="ylabel",
    default=None,
)
parser.add_argument(
    "-xl",
    "--x-label",
    help="The label for the x-axis.",
    type=str,
    dest="xlabel",
    default=None,
)
parser.add_argument(
    "-ys",
    "--y-scale",
    help="The scale for the y-axis.",
    type=str,
    dest="yscale",
    default="linear",
    choices=["linear", "log", "symlog", "logit"],
)
parser.add_argument(
    "-xs",
    "--x-scale",
    help="The scale for the x-axis.",
    type=str,
    dest="xscale",
    default="linear",
    choices=["linear", "log", "symlog", "logit"],
)
parser.add_argument(
    "-mk",
    "--marker",
    help="The marker for the plot.",
    type=str,
    dest="marker",
    default="x",
    choices=["1", "2", "3", "4", "+", "x", "|", "_", "o", "*"],
)
parser.add_argument(
    "-or",
    "--order",
    help="The order for the regression.",
    type=int,
    dest="order",
    default=1,
)
parser.add_argument(
    "-d",
    "--dpi",
    help="The DPI for the plot.",
    type=float,
    dest="dpi",
    default=None,
)


args: argparse.Namespace = parser.parse_args()


print(f"\n\033[36m{40*'*'}\033[0m")
for arg in args.__dict__:
    print(
        f"\033[36m* \033[32m{arg:10}\033[33m:", f"\033[34m{args.__dict__[arg]!r}\033[0m"
    )
print(f"\033[36m{40*'*'}\033[0m\n")


if args.mode == "plot":
    plot(
        file=args.file,
        out=args.out,
        median_label=args.mlabel,
        x_label=args.xlabel,
        y_label=args.ylabel,
        x_scale=args.xscale,
        y_scale=args.yscale,
        marker=args.marker,
        order=args.order,
        dpi=args.dpi,
    )
