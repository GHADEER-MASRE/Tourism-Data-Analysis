import pandas as pd 
import cleaning_functions
input_file="C:/Users/LENOVO/OneDrive/Documents/Desktop/Tourism-Data-Analysis/data/raw/Domestic Tourism-Trips.csv"
df=cleaning_functions.load_file(input_file)

years_columns=cleaning_functions.get_years_columns()
df=cleaning_functions.add_country_column(df)
df["Indicator"]=(
   df["Unnamed: 5"].fillna(df["Unnamed: 6"])
)
df = df[df["Indicator"].notna()]

df=cleaning_functions.reshape_years(df,
                                    ["Country","Indicator","Units"],
                                    years_columns)

df["Value"]= pd.to_numeric(df["Value"],errors="coerce")
output_file="C:/Users/LENOVO/OneDrive/Documents/Desktop/Tourism-Data-Analysis/data/cleaned/domestic_tourism_trips_cleaned.csv" 
df.to_csv(output_file,index=False)

print("cleaning completed")
