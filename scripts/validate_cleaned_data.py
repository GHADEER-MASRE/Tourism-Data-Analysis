import pandas as pd
import glob


def validate_data(file_path):

    df = pd.read_csv(file_path)

    print("\n" + "=" * 60)
    print("File:", file_path)
    print("=" * 60)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nShape:")
    print(df.shape)

    print("\nMissing values:")
    print(df.isna().sum())

    print("\nYear range:")
    print(df["Year"].min(), "-", df["Year"].max())

    print("\nYear data type:")
    print(df["Year"].dtype)

    print("\nValue data type:")
    print(df["Value"].dtype)

    print("\nDuplicate rows:")
    print(df.duplicated().sum())

    key_columns = [
        column for column in df.columns
        if column != "Value"
    ]

    print("\nDuplicate logical records:")
    print(df.duplicated(subset=key_columns).sum())


files = glob.glob(
    "C:/Users/LENOVO/OneDrive/Documents/Desktop/"
    "Tourism-Data-Analysis/data/cleaned/*.csv"
)


for file_path in files:
    validate_data(file_path)