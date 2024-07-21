from ...abstract import Parser
from bs4 import BeautifulSoup
import pandas as pd


class Heights(Parser):
    def parse(self, soup: BeautifulSoup) -> pd.Series:
        stats = soup.find_all("td", {"class": "zentriert"})
        heights = [stat for stat in stats[4::8]]
        heights = [td.text if td.text else None for td in heights]
        return pd.Series(heights, name="height")
