# -*- coding=utf-8 -*-
r"""

"""
import io
import warnings
import typing as t
from os import PathLike
from ..structures import Caption


def write_microdvd(captions: t.List[Caption], filename: t.Union[str, PathLike, t.TextIO], fps: int = None) -> None:
    stream = io.StringIO()

    if fps is None:
        warnings.warn("Missing fps specification for reading MicroDVD.\n"
                      "MicroDVD works with frames instead of timestamps. "
                      "Specify fps to convert frames to timestamps or set to 1 to keep.", RuntimeWarning)
        fps = 1

    for caption in captions:
        start = round(caption.start * fps)
        end = round(caption.end * fps)
        stream.write(f"{{{start}}}{{{end}}}{'|'.join(caption.lines)}\r\n")

    if isinstance(filename, (str, PathLike)):
        with open(filename, 'w') as file:
            file.write(stream.getvalue())
    else:
        filename.write(stream.getvalue())
