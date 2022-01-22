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
> -m LABEL, --median-label LABEL

* type: str

The label for the median.

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
> -mk MARKER, --marker MARKER

* type: {1,2,3,4,+,x,|,\_,o,\*}

The marker for the plot.

---
> -ms SIZE, --maker-size SIZE

* type: float

The size for the marker.

---
> -or ORDER, --order ORDER

* type: int

The order for the regression.

---
> -d DPI, --dpi DPI

* type: int

The DPI for the plot.

---
> -g GRID, --grid GRID

* type: bool

Whether a grid should be visible in the plot or not.

---
