from ...abstract import Parser
from bs4 import BeautifulSoup
import pandas as pd


class Names(Parser):
    def parse(self, soup: BeautifulSoup) -> pd.Series:
        elements = soup.find_all("img", {"class": "bilderrahmen-fixed lazy lazy"})
        names = [td.get("title") if td.get("title") else None for td in elements]
        return pd.Series(names, name="name")
