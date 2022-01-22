import typing


__all__ = (
    "str_to_dict",
    "get_bool",
)


# do I need this function?!
def str_to_dict(
    text: str,
    /,
    *keys: str,
    sep: str = ",",
) -> dict[str, str]:
    """
    Parameters
    ----------
    text: str
        The text which should be split into multiple values.
    keys: str
        The keys for the values.
    sep: str
        The separator for the values.

    Returns
    -------
    dict[str, str]
    """
    values = text.split(sep)
    return {key: value for key, value in zip(keys, values)}


def get_bool(
    raw: typing.Any,
    /,
) -> bool:
    """
    Parameters
    ----------
    raw: any
        The input to get the boolean from.

    Returns
    -------
    bool

    Raises
    ------
    ValueError
        If it's unclear what the boolean is.
    """
    if raw in ["True", "true", "t", "yes", "y", "1", 1, True]:
        return True
    if raw in ["False", "false", "f", "no", "n", "0", 0, False]:
        return False
    raise ValueError(f"Cannot assign {raw!r} to True or False!")
