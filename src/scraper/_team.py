from collections.abc import Sequence
from dataclasses import dataclass, field
from rich import print
from .base import Base
from ..parsers.team import team_parsers
from ..config.settings import URL
from ..abstract import Parser, DataSaver


@dataclass(kw_only=True)
class TeamScraper(Base):
    league: str
    league_id: str
    year: int
    parsers: Sequence[Parser] = field(default_factory=lambda: team_parsers)
    url: str = field(default=URL.TEAM)
    saver: DataSaver = field(default_factory=lambda: None)

    def __post_init__(self) -> None:
        self.url = self.url.format(
            league=self.league, league_id=self.league_id, year=self.year
        )

        print(
            f"Scraper initialized for: League: {self.league}, ID: {self.league_id}, Year: {self.year}"
        )

    def scrape(self) -> None:
        print(
            f"Scraping data for: League: {self.league}, ID: {self.league_id}, Year: {self.year}"
        )
        
        data = super().scrape()
        print(data)

        if self.saver is not None:
            self.saver.save(data)
