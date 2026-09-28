import pandas as pd 
input_file="C:/Users/LENOVO/OneDrive/Documents/Desktop/Tourism-Data-Analysis/data/raw/Domestic Tourism-Trips.csv"
df=pd.read_csv(input_file,encoding="latin1")

df["Country"]=df["Basic data and indicators"].where(df["S."].fillna(-1)==0)
df["Country"]=df["Country"].ffill()

df["Indicator"]=(
   df["Unnamed: 5"].fillna(df["Unnamed: 6"])
)

years_columns=[str(year) for year in range(1995,2023)]
df = df[df["Indicator"].notna()]
df=df.melt(
    id_vars=["Country","Indicator","Units"],
    value_vars=years_columns,
    var_name="Year",
    value_name="Value"
)

df["Value"]= pd.to_numeric(df["Value"],errors="coerce")
output_file="C:/Users/LENOVO/OneDrive/Documents/Desktop/Tourism-Data-Analysis/data/cleaned/domestic_tourism_trips_cleand.cvs" 
df.to_csv(output_file,index=False)
print("cleaning completed")

print(df[["Country", "Indicator", "Units"]].head(15).to_string())
print(df.shape)
print(df.columns.to_list())
print(df.iloc[:15, :12].to_string())