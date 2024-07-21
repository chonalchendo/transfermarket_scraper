import pandas as pd
from dataclasses import dataclass, field
from collections.abc import Sequence

from ..abstract import Parser
from ..schemas import Team
from ..parsers.player import player_parsers
from ..config.settings import URL
from ._base import BaseScraper


@dataclass(kw_only=True)
class PlayerScraper(BaseScraper):
    team: Team
    year: int
    url: str = field(default=URL.PLAYER)
    parsers: Sequence[Parser] = field(default_factory=lambda: player_parsers)

    def __post_init__(self) -> None:
        self.url = self.url.format(name=self.team.name, id=self.team.id, year=self.year)
        print(f"Scraper initialized for: Team: {self.team.name}, Year: {self.year}")

    def run(self) -> pd.DataFrame:

        data = self.scrape()

        data["season"] = self.year
        data["team"] = self.team.name

        return data
