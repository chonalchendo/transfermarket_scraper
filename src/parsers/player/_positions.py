from ...abstract import Parser
from bs4 import BeautifulSoup
import pandas as pd


class Positions(Parser):
    def parse(self, soup: BeautifulSoup) -> pd.Series:
        pos_soup = soup.find_all("td", {"class": "posrela"})
        positions = [
            td.find_all("tr")[1].find("td").text.strip() if td.find_all("tr") else None
            for td in pos_soup
        ]
        return pd.Series(positions, name="position")
