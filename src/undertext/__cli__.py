# -*- coding=utf-8 -*-
r"""

"""
import re
from pathlib import Path
from . import loads, dumps


def cmd_read(input_fp, after: float = None, before: float = None, **kwargs) -> None:
    input_fp = Path(input_fp)
    if not input_fp.is_file():
        raise FileNotFoundError(str(input_fp))

    for caption in loads(input_fp, **kwargs):
        if after and caption.start <= after:
            continue
        if before and caption.end >= before:
            continue
        print(f"{caption!r}")


def cmd_convert(input_fp: str, output_fp: str, overwrite: bool = False, **kwargs):
    input_fp = Path(input_fp)
    if not input_fp.is_file():
        raise FileNotFoundError(str(input_fp))
    output_fp = Path(output_fp)
    if output_fp.is_file():
        if not overwrite:
            raise FileExistsError(str(output_fp))
    elif output_fp.exists():
        raise RuntimeError(f"{output_fp!s} can't be overwritten")

    input_kwargs = {key[6:]: value for key, value in kwargs.items() if key.startswith("input_")}
    output_kwargs = {key[7:]: value for key, value in kwargs.items() if key.startswith("output_")}

    captions = loads(input_fp, **input_kwargs)
    dumps(captions, output_fp, **output_kwargs)


# -------------------------------------------------------------------------------------------------------------------- #


TIME_RE = re.compile(r"(?:(?:(?P<h>\d+):)?(?P<m>\d+):)?(?P<s>\d+(?:[.,]\d+)?)")


def parse_time(text: str) -> float:
    r"""
    [[hh+:]mm+:]ss+[{,.}mmm+]
    h:m:s.ms
    m:s.ms
    s.ms
    s
    """
    match = TIME_RE.fullmatch(text)
    if match is None:
        raise ValueError(f"Bad time format: {text!r}")

    hours = match.group("h")
    hours = 0 if hours is None else int(hours)
    minutes = match.group("m")
    minutes = 0 if minutes is None else int(minutes)
    seconds = float(match.group("s").replace(",", "."))
    return (hours * 3600) + (minutes * 60) + seconds
