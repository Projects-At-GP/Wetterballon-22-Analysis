# Basic

```bash
python -m Wetterballon_22_Analysis ARGUMENTS
```

## Arguments

- [required](#required)
- [optional](#optional)

> -h, --help

shows the help message


### Required

---
> -s FILE, --source FILE

* type: path (to file)

The path to the source-file.

---
> -d LABEL, --data-label LABEL

* type: str

The label for the data.

---

### Optional

---
> -o OUT, --out OUT

* type: path

The path for the output-file.

---
> -e EPOCH, --epoch EPOCH

* type: float

**OR**

> -ef FILE, --epoch-file FILE

* type: path (to file containing a float)

The epoch for the timestamps. ('ll be added to them)

---
> -yl LABEL, --y-label LABEL

* type: str

The label for the y-axis.

---
> -xl LABEL, --x-label LABEL

* type: str

The label for the x-axis.

---
> -ys MODE, --y-scale MODE

* type: {linear,log,symlog,logit}

The scale for the y-axis.

---
> -xs MODE, --x-scale MODE

* type: {linear,log,symlog,logit}

The scale for the x-axis.

---
> -r RELATIONAL, --relational RELATIONAL
* tpye: bool

Whether multiple columns from csv should be plotted or not.

Notes:
* This will ignore every color-argument.
* Plotted values may be on the same height (Y), but don't have to share the same value since the are distributed between their min and max.
  Example: max(A) = 200, min(A) = 100; The marker in the middle will have the value 150.

---
> -m MARKER, --marker MARKER

* type: {1,2,3,4,+,x,|,\_,o,\*}

The marker for the plot.

---
> -ms SIZE, --marker-size SIZE

* type: float

The size for the marker.

---
> -mw WIDTH, --marker-width WIDTH

* type: float

The width for the marker.

---
> -mc COLOR, --marker-color COLOR

* type: str

The color for the marker.

---
> -lw WIDTH, --line-width WIDTH

* type: float

The line for the line.

---
> -lc COLOR, --line-color COLOR

* type: str

The color for the line.

---
> --order ORDER

* type: int

The order for the regression.

---
> --dpi DPI

* type: int

The DPI for the plot.

---
> -g GRID, --grid GRID

* type: bool

Whether a grid should be visible in the plot or not.

---
