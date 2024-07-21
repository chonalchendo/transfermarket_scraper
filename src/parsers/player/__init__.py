from collections.abc import Sequence
from ._ages import Ages
from ._countries import Countries
from ._current_clubs import CurrentClubs
from ._heights import Heights
from ._names import Names
from ._positions import Positions
from ._values import Values
from ._joined_dates import JoinedDate
from ._numbers import Numbers
from ._signing_info import SigningInfo
from ._tm_ids import TransfermarktId
from ._tm_names import TransfermarktName
from ._foots import Foot

from ...abstract import Parser

player_parsers: Sequence[Parser] = (
    Ages(),
    Countries(),
    CurrentClubs(),
    Heights(),
    Names(),
    Positions(),
    Values(),
    JoinedDate(),
    Numbers(),
    SigningInfo(),
    TransfermarktId(),
    TransfermarktName(),
    Foot(),
)

__all__ = [
    "player_parsers",
]
