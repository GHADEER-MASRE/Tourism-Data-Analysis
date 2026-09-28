import pandas as pd
input_file = "C:/Users/LENOVO/OneDrive/Documents/Desktop/Tourism-Data-Analysis/data/raw/Inbound Tourism-Arrivals.csv"
df=pd.read_csv(input_file, encoding="latin1")
print(df.shape)
print(df.columns.to_list())
print(df.iloc[:15, :12].to_string())
years_columns=[str(year) for year in range(1995,2023)]
df["country"]=df["Basic data and indicators"].where(df["S."].fillna(-1)==0)
df["country"]=df["country"].ffill()
indicators_columns=["Unnamed: 5",
    "Unnamed: 6",
    "Unnamed: 7"]
df["Indicator"]=(df[indicators_columns].fillna("").agg(" ".join,axis=1).str.strip())
df=df[df["Indicator"]!=""]
df=df[["country","Indicator","Units"]+years_columns]
df = df.rename(columns={
    "country": "Country"
})
df=df.melt(
    id_vars=["Country","Indicator","Units"],
    value_vars=years_columns,
    var_name="Year",
    value_name="Value"
)
df["Value"]=(
    df["Value"].astype(str).str.replace(",","",regex=False)
)
df["Value"]=pd.to_numeric(df["Value"],errors="coerce")
print(df["Country"].value_counts().head(20))
output_file="C:/Users/LENOVO/OneDrive/Documents/Desktop/Tourism-Data-Analysis/data/cleaned/inbound_arrivals_cleaned.cvs"
df.to_csv(output_file,index=False)
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