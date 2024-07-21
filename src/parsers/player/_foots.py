from ...abstract import Parser
from bs4 import BeautifulSoup
import pandas as pd


class Foot(Parser):
    def parse(self, soup: BeautifulSoup) -> pd.Series:
        stats = soup.find_all("td", {"class": "zentriert"})
        foots = [stat for stat in stats[5::8]]
        foots = [td.text if td.text else None for td in foots]
        return pd.Series(foots, name="foot")
