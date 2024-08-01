from ...abstract import Parser
from bs4 import BeautifulSoup
import pandas as pd


class SigningInfo(Parser):
    def parse(self, soup: BeautifulSoup) -> pd.Series:
        stats = soup.find_all("td", {"class": "zentriert"})
        signing_info = [stat for stat in stats[7::8]]

        signed_from = [
            td.find("a").get("title").split(": Ablöse ")[0] if td.find("a") else None
            for td in signing_info
        ]
        signing_fee = [
            td.find("a").get("title").split(": Ablöse ")[1] if td.find("a") else '€0'
            for td in signing_info
        ]
        return pd.DataFrame({"signed_from": signed_from, "signing_fee": signing_fee})
