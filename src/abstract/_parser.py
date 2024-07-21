from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import pandas as pd


class Parser(ABC):
    """ABC Protocol class for parsing data from transfermarkt."""

    @abstractmethod
    def parse(self, soup: BeautifulSoup) -> pd.DataFrame | pd.Series | tuple:
        pass
