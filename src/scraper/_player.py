import pandas as pd
from dataclasses import dataclass, field
from collections.abc import Sequence
from rich import print

from ..abstract import Parser
from ..schemas import Team
from ..parsers.player import player_parsers
from ..config.settings import URL
from .base import Base


@dataclass(kw_only=True)
class PlayerScraper(Base):
    team: Team
    year: int
    url: str = field(default=URL.PLAYER)
    parsers: Sequence[Parser] = field(default_factory=lambda: player_parsers)

    def __post_init__(self) -> None:
        self.url = self.url.format(name=self.team.name, id=self.team.id, year=self.year)
        print(f"Scraper initialized for: Team: {self.team.name}, Year: {self.year}")

    def scrape(self) -> pd.DataFrame:
        print(f"Scraping data for: Team: {self.team.name}, Year: {self.year}")

        data = super().scrape()

        data["season"] = self.year
        data["team"] = self.team.name

        return data
