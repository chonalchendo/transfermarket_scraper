from collections.abc import Sequence
from dataclasses import dataclass
from rich import print
import pandas as pd
import time

from ..abstract import DataSaver
from .base import Base


@dataclass
class MultiScraper:
    """Scrape data from multiple scraping objects. For example,
    scrapers can be a list of PlayerScraper objects, each of which
    scrapes player data for a specific team. The MultiScraper
    will scrape data from each PlayerScraper object and concatenate
    the results into a single DataFrame.
    """
    scrapers: Sequence[Base]
    saver: DataSaver | None = None

    def scrape(self) -> pd.DataFrame:
        data = pd.concat(
            [self._compose(scraper) for scraper in self.scrapers]
        ).reset_index(drop=True)

        if self.saver is not None:
            self.saver.save(data)

        return data

    def _compose(self, scraper: Base) -> pd.DataFrame:
        time.sleep(5)
        data = scraper.scrape()
        print(data)
        return data
