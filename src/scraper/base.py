from dataclasses import dataclass, field
from collections.abc import Sequence
from bs4 import BeautifulSoup
import httpx
import pandas as pd

from ..abstract import Parser, DataSaver


@dataclass
class Base:
    """Scrape data from transfermarkt for a given url and year."""

    parsers: Sequence[Parser]
    url: str
    saver: DataSaver = field(default_factory=lambda: None)

    def scrape(self) -> pd.DataFrame:
        """Run the scraping process."""

        soup = self._get_soup_content(self.url)  # get html content from url

        return pd.concat(
            [parser.parse(soup) for parser in self.parsers], axis=1
        )  # concatenate parsers into a dataframe

    def _get_soup_content(self, url: str) -> BeautifulSoup:
        """Get the html content from a given Transfermarkt url."""
        resp = self._make_request(url)
        return BeautifulSoup(resp.content, "html.parser")

    def _make_request(self, url: str) -> httpx.Response:
        """Make a request to a given Transfermarkt url."""
        try:
            response = httpx.get(
                url,
                headers={
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:127.0) Gecko/20100101 Firefox/127.0"
                },
                timeout=60,
            )
            response.raise_for_status()
            print(f"Status code: {response.status_code}")
            return response

        except httpx.HTTPError as e:
            print(f"HTTP error occurred: {e}")
            raise e
