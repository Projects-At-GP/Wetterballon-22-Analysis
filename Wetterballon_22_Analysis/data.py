__all__ = ("str_to_dict",)


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
