import argparse

from Wetterballon_22_Analysis import plot, get_bool, print_args


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
    type=str,
    dest="out",
    default="out",
)
parser.add_argument(
    "-e",
    "--epoch",
    help="The epoch for the timestamps. ('ll be added to them)",
    type=float,
    dest="epoch",
    default=0,
)
parser.add_argument(
    "-ef",
    "--epoch-file",
    help="The epoch-file for the timestamps. ('ll be added to them)",
    type=str,
    dest="epoch_file",
    default=None,
)
parser.add_argument(
    "-d",
    "--data-label",
    help="The label for the data.",
    type=str,
    dest="dlabel",
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
    "-r",
    "--relational",
    help="Plots multiple columns from csv. NOTE: THIS IGNORES EVERY color-ARGUMENT!",
    type=get_bool,
    dest="relational",
    default=False,
)
parser.add_argument(
    "-m",
    "--marker",
    help="The marker for the plot.",
    type=str,
    dest="marker",
    default="x",
    choices=["1", "2", "3", "4", "+", "x", "|", "_", "o", "*"],
)
parser.add_argument(
    "-ms",
    "--marker-size",
    help="The size for the marker.",
    type=float,
    dest="markersize",
    default=None,
)
parser.add_argument(
    "-mw",
    "--marker-width",
    help="The width for the marker.",
    type=float,
    dest="markerwidth",
    default=None,
)
parser.add_argument(
    "-mc",
    "--marker-color",
    help="The color for the marker.",
    type=str,
    dest="markercolor",
    default="blue",
)
parser.add_argument(
    "-lw",
    "--line-width",
    help="The width for the line.",
    type=float,
    dest="linewidth",
    default=None,
)
parser.add_argument(
    "-lc",
    "--line-color",
    help="The color for the line.",
    type=str,
    dest="linecolor",
    default="red",
)
parser.add_argument(
    "--order",
    help="The order for the regression.",
    type=int,
    dest="order",
    default=1,
)
parser.add_argument(
    "--dpi",
    help="The DPI for the plot.",
    type=float,
    dest="dpi",
    default=None,
)
parser.add_argument(
    "-g",
    "--grid",
    help="Whether a grid should be visible in the plot or not.",
    type=get_bool,
    dest="grid",
    default=True,
)


args: argparse.Namespace = parser.parse_args()


print_args(**args.__dict__)


if args.epoch != 0 and args.epoch_file is not None:
    raise AttributeError("epoch and epoch-file cannot be set both!")
elif args.epoch_file:
    with open(args.epoch_file) as f:
        epoch = float(f.read())
else:
    epoch = args.epoch


plot(
    file=args.file,
    out=args.out,
    d_label=args.dlabel,
    x_label=args.xlabel,
    y_label=args.ylabel,
    x_scale=args.xscale,
    y_scale=args.yscale,
    relational=args.relational,
    marker=args.marker,
    marker_size=args.markersize,
    marker_width=args.markerwidth,
    marker_color=args.markercolor,
    line_width=args.linewidth,
    line_color=args.linecolor,
    order=args.order,
    dpi=args.dpi,
    grid=args.grid,
    epoch=epoch,
)
