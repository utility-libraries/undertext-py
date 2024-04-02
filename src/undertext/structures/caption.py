# -*- coding=utf-8 -*-
r"""

"""
import typing as t
from datetime import timedelta


T_TIME: t.TypeAlias = t.Union[int, float, timedelta]
T_LINES = t.Iterable[str]
T_TEXT: t.TypeAlias = t.Union[str, T_LINES]
T_STYLE: t.TypeAlias = t.Dict[str, str]


class Caption:
    _start: float
    _end: float
    _lines: t.List[str]
    _id: t.Optional[str]
    _styles: t.Optional[T_STYLE]

    def __init__(self, start: T_TIME, end: T_TIME, text: T_TEXT,
                 id: t.Optional[str] = None, styles: t.Optional[T_STYLE] = None) -> None:
        self._lines = []

        self.start = start
        self.end = end
        self.text = text
        self.id = id
        self.styles = styles

    def __repr__(self) -> str:
        return f"<{self._format_ts(self.start)} -> {self._format_ts(self.end)}> {self.text!r}"

    @staticmethod
    def _format_ts(ts: float) -> str:
        r""" internal usage only """
        seconds = ts % 60
        minutes = int((ts / 60) % 60)
        hours = int(ts / 3600)

        return f"{hours:0>2}:{minutes:0>2}:{format(seconds, '.3f'):0>6}"

    @property
    def start(self) -> float:
        return self._start

    @start.setter
    def start(self, value: T_TIME) -> None:
        if isinstance(value, timedelta):
            self._start = value.total_seconds()
        else:
            self._start = float(value)

    @property
    def end(self) -> float:
        return self._end

    @end.setter
    def end(self, value: T_TIME) -> None:
        if isinstance(value, timedelta):
            self._end = value.total_seconds()
        else:
            self._end = float(value)

    @property
    def lines(self) -> t.List[str]:
        return self._lines

    @lines.setter
    def lines(self, lines: T_LINES) -> None:
        self._lines.clear()
        self._lines.extend(lines)

    @property
    def text(self) -> str:
        return "\n".join(self.lines)

    @text.setter
    def text(self, value: T_TEXT) -> None:
        if isinstance(value, str):
            self.lines = value.splitlines(keepends=False)
        else:
            self.lines = value

    @property
    def id(self) -> t.Optional[str]:
        return self._id

    @id.setter
    def id(self, value: t.Optional[str]) -> None:
        self._id = value if value is None else str(value)

    @property
    def styles(self) -> t.Optional[T_STYLE]:
        return self._styles

    @styles.setter
    def styles(self, value: t.Optional[T_STYLE]) -> None:
        self._styles = value
