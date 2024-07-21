from bs4 import BeautifulSoup
from ...abstract import Parser
import pandas as pd


class Info(Parser):
    def parse(self, soup: BeautifulSoup) -> pd.DataFrame:
        team_info = soup.find_all("td", {"class": "hauptlink no-border-links"})
        team_name = [td.find("a").get("href").split("/")[1] for td in team_info]
        team_id = [td.find("a").get("href").split("/")[4] for td in team_info]
        return pd.DataFrame({"team_name": team_name, "team_id": team_id})
