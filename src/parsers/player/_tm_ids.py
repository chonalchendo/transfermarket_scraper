from ...abstract import Parser
from bs4 import BeautifulSoup
import pandas as pd


class TransfermarktId(Parser):
    def parse(self, soup: BeautifulSoup) -> pd.Series:
        links = soup.find_all("td", {"class": "hauptlink"})
        tm_id = [
            link.find("a")["href"].split("/")[4] if link.find("a") else None
            for link in links[::2]
        ]
        return pd.Series(tm_id, name="tm_id")
