__all__ = (
    "print_args",
    "prepare_csv_from_STRATOFLIGHTS_LOG",
)


adjust_size = (
    lambda to_adjust, length: to_adjust + (length - len(to_adjust)) * " "
)  # noqa


def print_args(**kwargs) -> None:
    # constants
    up = down = "\033[36m{}\033[0m"
    left = "\033[36m* \033[0m"
    right = "\033[36m *\033[0m"
    sep = "\033[33m: \033[0m"

    l_length = sep_length = r_length = 2

    arg_form = "\033[32m{}\033[0m"
    val_form = "\033[34m{}\033[0m"

    arguments = []
    values = []

    to_print = ""

    # processing kwargs
    for k, v in kwargs.items():
        arguments.append(k)
        values.append(f"{v!r}")

    arg_length = max(len(_) for _ in arguments)
    val_length = max(len(_) for _ in values)

    length = l_length + arg_length + sep_length + val_length + r_length

    to_print += up.format(length * "*") + "\n"

    for arg, val in zip(arguments, values):
        arg = adjust_size(arg, arg_length)
        val = adjust_size(val, val_length)
        to_print += (
            left + arg_form.format(arg) + sep + val_form.format(val) + right + "\n"
        )

    to_print += down.format(length * "*") + "\n"

    print(to_print)


def prepare_csv_from_STRATOFLIGHTS_LOG(path: str) -> None:
    with open(path) as f:
        print(f.readline(), end="")
        for line in f.readlines():
            if line.startswith("$"):
                # every ``_`` is fairly uninteresting
                _, up_time, utc, _, sats_in_use, lat, lon, _, speed_kmh, course, altitude, temp_board, temp_ext, hum_board, hum_ext, press_hpa, _, _ = \
                    line.split(";")
