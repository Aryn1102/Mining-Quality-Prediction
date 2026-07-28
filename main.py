from src.data_loader import DataLoader


def main():
    loader = DataLoader(
        "data/raw/MiningProcess_Flotation_Plant_Database.csv"
    )

    df = loader.load_data()

    print("=" * 50)
    print("Dataset Loaded Successfully")
    print("=" * 50)

    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")


if __name__ == "__main__":
    main()