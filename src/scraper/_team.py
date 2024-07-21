from collections.abc import Sequence
from dataclasses import dataclass, field
from ._base import BaseScraper
from ..parsers.team import team_parsers
from ..config.settings import URL
from ..abstract import Parser, DataSaver


@dataclass(kw_only=True)
class TeamScraper(BaseScraper):
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

    def run(self) -> None:
        data = self.scrape()
        print(data)

        if self.saver is not None:
            self.saver.save(data)
