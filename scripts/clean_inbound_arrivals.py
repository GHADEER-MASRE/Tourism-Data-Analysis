import pandas as pd
import cleaning_functions 
input_file = "C:/Users/LENOVO/OneDrive/Documents/Desktop/Tourism-Data-Analysis/data/raw/Inbound Tourism-Arrivals.csv"
df=cleaning_functions.load_file(input_file)

years_columns=cleaning_functions.get_years_columns()

df=cleaning_functions.add_country_column(df)

df["Indicator"]=(
    df[["Unnamed: 5",
    "Unnamed: 6",
    "Unnamed: 7"]]
    .fillna("")
    .agg(" ".join,axis=1)
    .str.strip())
df=df[df["Indicator"]!=""]

df=df[["Country","Indicator","Units"]+years_columns]

df=cleaning_functions.reshape_years(df,
                                    ["Country","Indicator","Units"],
                                    years_columns)


output_file="C:/Users/LENOVO/OneDrive/Documents/Desktop/Tourism-Data-Analysis/data/cleaned/inbound_arrivals_cleaned.csv"
cleaning_functions.save_cleaned(df,output_file)

print("cleaning completed")

print(df.head(20))
print("\nYear range:", df["Year"].min(), "-", df["Year"].max())
print("Years:", sorted(df["Year"].unique()))
print("\nValue data type:", df["Value"].dtype)
print("Missing values:", df["Value"].isna().sum())
print("\nMissing countries:", df["Country"].isna().sum())
print("Missing indicators:", df["Indicator"].isna().sum())
print("Unique indicators:", df["Indicator"].unique())
print("\nDuplicate rows:", df.duplicated(subset=["Country", "Indicator", "Year"]).sum())
print("\nshape:",df.shape)