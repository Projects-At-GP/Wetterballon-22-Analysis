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
    "-m",
    "--mode",
    help="The mode to process the data.",
    dest="mode",
    default="plot",
    choices=["plot"],
)


args: argparse.Namespace = parser.parse_args()


print(args)

if args.mode == "plot":
    plot(file=args.file)
