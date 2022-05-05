from pathlib import Path


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
    p1 = "{},{}"
    p2 = "{},{},{}"

    Path("data").mkdir(exist_ok=True)
    with (
        open(Path(path)) as f,
        open(Path("data/1_sats_in_use.csv"), "w") as f1_sats_in_use,
        open(Path("data/1_lat.csv"), "w") as f1_lat,
        open(Path("data/1_lon.csv"), "w") as f1_lon,
        open(Path("data/2_lat_lon.csv"), "w") as f2_lat_lon,
        open(Path("data/1_speed_kmh.csv"), "w") as f1_speed_kmh,
        open(Path("data/1_course.csv"), "w") as f1_course,
        open(Path("data/1_altitude_nn.csv"), "w") as f1_altitude_nn,
        open(Path("data/1_temp_board.csv"), "w") as f1_temp_board,
        open(Path("data/1_temp_ext.csv"), "w") as f1_temp_ext,
        open(Path("data/2_temp_board_ext.csv"), "w") as f2_temp_board_ext,
        open(Path("data/1_hum_board.csv"), "w") as f1_hum_board,
        open(Path("data/1_hum_ext.csv"), "w") as f1_hum_ext,
        open(Path("data/2_hum_board_ext.csv"), "w") as f2_hum_board_ext,
        open(Path("data/1_press_hpa.csv"), "w") as f1_press_hpa,
        open(Path("data/2_altitude_press.csv"), "w") as f2_altitude_press,
    ):
        print("up_time,sats_in_use", file=f1_sats_in_use)
        print("up_time,lat", file=f1_lat)
        print("up_time,lon", file=f1_lon)
        print("up_time,lat,lon", file=f2_lat_lon)
        print("up_time,speed_kmh", file=f1_speed_kmh)
        print("up_time,course", file=f1_course)
        print("up_time,altitude_nn", file=f1_altitude_nn)
        print("up_time,temp_board", file=f1_temp_board)
        print("up_time,temp_ext", file=f1_temp_ext)
        print("up_time,temp_board,temp_ext", file=f2_temp_board_ext)
        print("up_time,hum_board", file=f1_hum_board)
        print("up_time,hum_ext", file=f1_hum_ext)
        print("up_time,hum_board,hum_ext", file=f2_hum_board_ext)
        print("up_time,press_hpa", file=f1_press_hpa)
        print("up_time,altitude_nn,press_hpa", file=f2_altitude_press)

        print(f.readline(), end="")
        for line in f.readlines():
            if line.startswith("$"):
                # every ``_`` is fairly uninteresting
                _, up_time, utc, _, sats_in_use, lat, lon, _, speed_kmh, course, altitude_nn, temp_board, temp_ext, hum_board, hum_ext, press_hpa, _, _ = \
                    line.split(";")
            else:
                continue

            print(p1.format(up_time, sats_in_use), file=f1_sats_in_use)
            print(p1.format(up_time, lat), file=f1_lat)
            print(p1.format(up_time, lon), file=f1_lon)
            print(p2.format(up_time, lat, lon), file=f2_lat_lon)
            print(p1.format(up_time, speed_kmh), file=f1_speed_kmh)
            print(p1.format(up_time, course), file=f1_course)
            print(p1.format(up_time, altitude_nn), file=f1_altitude_nn)
            print(p1.format(up_time, temp_board), file=f1_temp_board)
            print(p1.format(up_time, temp_ext), file=f1_temp_ext)
            print(p2.format(up_time, temp_board, temp_ext), file=f2_temp_board_ext)
            print(p1.format(up_time, hum_board), file=f1_hum_board)
            print(p1.format(up_time, hum_ext), file=f1_hum_ext)
            print(p2.format(up_time, hum_board, hum_ext), file=f2_hum_board_ext)
            print(p1.format(up_time, press_hpa), file=f1_press_hpa)
            print(p2.format(up_time, altitude_nn, press_hpa), file=f2_altitude_press)
