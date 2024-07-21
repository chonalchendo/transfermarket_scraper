from ...abstract import Parser
from bs4 import BeautifulSoup
import pandas as pd


class JoinedDate(Parser):
    def parse(self, soup: BeautifulSoup) -> pd.Series:
        stats = soup.find_all("td", {"class": "zentriert"})
        joined_date = [stat for stat in stats[6::8]]
        joined_date = [td.text if td.text else None for td in joined_date]
        return pd.Series(joined_date, name="joined_date")
