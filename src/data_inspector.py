import pandas as pd


class DataInspector:

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def summary(self):
        print("\n" + "=" * 60)
        print("DATASET SUMMARY")
        print("=" * 60)

        print(f"Rows    : {self.df.shape[0]}")
        print(f"Columns : {self.df.shape[1]}")

        print("\nColumn Names:")
        print(list(self.df.columns))

        print("\nData Types:")
        print(self.df.dtypes)

        print("\nMissing Values:")
        print(self.df.isnull().sum())

        print("\nDuplicate Rows:")
        print(self.df.duplicated().sum())

        print("\nStatistical Summary:")
        print(self.df.describe())