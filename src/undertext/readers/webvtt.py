# -*- coding=utf-8 -*-
r"""

"""
import re
import typing as t
from pathlib import Path
from ..structures import Caption
from ..exceptions import *


HEAD_RE = re.compile(r"^WEBVTT ?")
TIME_RE = re.compile(r"(?:(?P<h>\d{2,}):)?(?P<m>\d{2}):(?P<s>\d{2}\.\d{3})")
RANGE_RE = re.compile(r"^(?P<start>(\d{2,}:)?\d{2}:\d{2}\.\d{3}) --> (?P<end>(\d{2,}:)?\d{2}:\d{2}\.\d{3})"
                      r"(?P<style> .*)?$")


def read_webvtt(fp: Path) -> t.List[Caption]:
    captions: t.List[Caption] = []

    with open(fp, 'r') as file:
        lines = (_.rstrip() for _ in iter(file))

        if HEAD_RE.match(next(lines, "")) is None:
            raise FormatException("Invalid webvtt header")

        for line in lines:
            if not line:  # empty line
                continue
            elif line.startswith(("STYLE", "NOTE")):
                while next(lines, ""):  # till empty line
                    pass  # discard
            else:
                id_ = None
                styles = {}

                match = RANGE_RE.fullmatch(line)
                if match is None:
                    id_ = line
                    line = next(lines, "")
                    match = RANGE_RE.fullmatch(line)

                if match is None:
                    raise FormatException(f"Missing or invalid time range ({line})")

                start = parse_time(match.group("start"))
                end = parse_time(match.group("end"))

                style: str = match.group("style")

                if style is not None:
                    for style in style.split():
                        key, sep, value = style.partition(":")
                        if sep is None:
                            raise FormatException(f"Bad style format ({style})")
                        if key not in {"line", "position", "size", "align"}:
                            raise KeyError(f"Invalid style: {key!r}")
                        styles[key] = value

                text_lines = []
                for text_line in lines:
                    if not text_line:
                        break
                    if text_line.startswith("- "):  # multiline
                        if text_lines:  # extend last line in text
                            text_lines[-1] += " " + text_line[2:]
                        else:  # text still empty. add as first
                            text_lines.append(text_line[2:])
                    else:  # next line should be empty but could also be '- *'
                        text_lines.append(text_line)

                captions.append(
                    Caption(start=start, end=end, text=text_lines, id=id_, styles=styles)
                )

    return captions


def parse_time(text: str) -> float:
    match = TIME_RE.fullmatch(text)
    if match is None:
        raise FormatException(f"Bad time format: {text!r}")

    hours = match.group("h")
    hours = 0 if hours is None else int(hours)
    minutes = int(match.group("m"))
    seconds = float(match.group("s"))
    return (hours * 3600) + (minutes * 60) + seconds
