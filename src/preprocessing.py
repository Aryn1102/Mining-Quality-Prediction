from pathlib import Path

import pandas as pd


class DataPreprocessor:

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe.copy()

    def convert_date(self) -> None:
        self.df["date"] = pd.to_datetime(self.df["date"])

    def convert_numeric_columns(self) -> None:

        numeric_columns = self.df.columns.drop("date")

        for column in numeric_columns:
            self.df[column] = (
                self.df[column]
                .astype(str)
                .str.replace(",", ".", regex=False)
            )

            self.df[column] = pd.to_numeric(
                self.df[column],
                errors="coerce"
            )

    def remove_duplicates(self) -> None:
        self.df.drop_duplicates(inplace=True)

    def get_dataframe(self) -> pd.DataFrame:
        return self.df

    def save_processed_data(self, output_path: str | Path) -> None:
        output_path = Path(output_path)

        output_path.parent.mkdir(parents=True, exist_ok=True)

        self.df.to_csv(output_path, index=False)