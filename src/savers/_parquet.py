import pandas as pd
from ..abstract import DataSaver


class ParquetSaver(DataSaver):
    def save(self, data: pd.DataFrame) -> None:
        data.to_parquet(self.output_path)
        print(f"Data saved to {self.output_path}")
