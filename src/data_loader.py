from pathlib import Path

import pandas as pd


class DataLoader:

    def __init__(self, file_path: str | Path):
        self.file_path = Path(file_path)

    def load_data(self) -> pd.DataFrame:
        if not self.file_path.exists():
            raise FileNotFoundError(
                f"Dataset not found: {self.file_path}"
            )

        return pd.read_csv(self.file_path)