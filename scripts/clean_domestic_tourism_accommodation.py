import pandas as pd
import cleaning_functions
input_file="C:/Users/LENOVO/OneDrive/Documents/Desktop/Tourism-Data-Analysis/data/raw/Domestic Tourism-Accommodation.csv"
df=cleaning_functions.load_file(input_file)

years_columns=cleaning_functions.get_years_columns()

df=cleaning_functions.add_country_column(df)

df["Accommodation_Type"]=df["Unnamed: 5"].ffill()
df["Indicator"]=df["Unnamed: 6"]
df = df[df["Indicator"].notna()]

df=cleaning_functions.reshape_years(df,
                                 ["Country", "Accommodation_Type", "Indicator", "Units"]
                                 ,years_columns)

output_file="C:/Users/LENOVO/OneDrive/Documents/Desktop/Tourism-Data-Analysis/data/cleaned/domestic_tourism_accommodation_cleaned.csv" 
cleaning_functions.save_cleaned(df,output_file)

print("cleaning completed")