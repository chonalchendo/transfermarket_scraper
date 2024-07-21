from ...abstract import Parser
from bs4 import BeautifulSoup
import pandas as pd


class Values(Parser):
    def parse(self, soup: BeautifulSoup) -> pd.Series:
        values = soup.find_all("td", {"class": "rechts hauptlink"})
        values = [td.find("a").text if td.find("a") else "€0" for td in values]
        return pd.Series(values, name="value")
