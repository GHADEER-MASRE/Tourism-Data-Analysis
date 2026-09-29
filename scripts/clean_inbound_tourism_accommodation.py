import pandas as pd

input_file="C:/Users/LENOVO/OneDrive/Documents/Desktop/Tourism-Data-Analysis/data/raw/Inbound Tourism-Accommodation.csv"
df=pd.read_csv(input_file,encoding="latin1")

years_columns=[str(year) for year in range(1995,2023)]

df["Country"]=df["Basic data and indicators"].where(df["S."].fillna(-1)==0)
df["Country"]=df["Country"].ffill()

df["Accommodation Type"]=df["Unnamed: 5"].ffill()
df["Indicator"]=df["Unnamed: 6"]
df=df[df["Indicator"].notna()]

df=df.melt(
    id_vars=["Country","Accommodation Type","Indicator","Units"],
    value_vars=years_columns,
    var_name="Year",
    value_name="Value"
 )
df["Value"]=pd.to_numeric(df["Value"],errors="coerce")

output_file="C:/Users/LENOVO/OneDrive/Documents/Desktop/Tourism-Data-Analysis/data/cleaned/inbound_tourism_accommodation_cleaned.csv"
df.to_csv(output_file,index=False)
print("cleaning completed")
print(df.head(10))

