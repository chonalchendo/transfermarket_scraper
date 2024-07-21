from collections.abc import Sequence

from ...abstract import Parser
from ._info import Info

team_parsers: Sequence[Parser] = (Info(),)

__all__ = ["team_parsers"]
