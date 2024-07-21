from ...abstract import Parser
from bs4 import BeautifulSoup
import pandas as pd


class Numbers(Parser):
    def parse(self, soup: BeautifulSoup) -> pd.Series:
        stats = soup.find_all("td", {"class": "zentriert"})
        numbers = [stat for stat in stats[0::8]]
        numbers = [
            (
                td.find("div", class_="rn_nummer").text.strip()
                if td.find("div", class_="rn_nummer")
                else None
            )
            for td in numbers
        ]
        return pd.Series(numbers, name="number")
