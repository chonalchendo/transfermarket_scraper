from abc import ABC, abstractmethod
import pandas as pd


class DataSaver(ABC):
    def __init__(self, output_path: str) -> None:
        super().__init__()
        self.output_path = output_path
        
    @abstractmethod
    def save(self, data: pd.DataFrame) -> None:
        pass
