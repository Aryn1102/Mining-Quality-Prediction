from src.data_loader import DataLoader
from src.data_inspector import DataInspector
from src.preprocessing import DataPreprocessor


def main():

    loader = DataLoader(
        "data/raw/MiningProcess_Flotation_Plant_Database.csv"
    )

    df = loader.load_data()

    print("RAW DATA")
    inspector = DataInspector(df)
    inspector.summary()

    preprocessor = DataPreprocessor(df)

    preprocessor.convert_date()
    preprocessor.convert_numeric_columns()
    preprocessor.remove_duplicates()

    processed_df = preprocessor.get_dataframe()

    print("\n")
    print("=" * 60)
    print("AFTER PREPROCESSING")
    print("=" * 60)

    print(processed_df.dtypes)

    preprocessor.save_processed_data(
        "data/processed/mining_process_clean.csv"
    )


if __name__ == "__main__":
    main()