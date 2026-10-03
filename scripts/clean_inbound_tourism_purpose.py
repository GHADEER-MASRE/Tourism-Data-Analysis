import cleaning_functions
input_file="C:/Users/LENOVO/OneDrive/Documents/Desktop/Tourism-Data-Analysis/data/raw/Inbound Tourism-Purpose.csv"
df=cleaning_functions.load_file(input_file)

years_columns=cleaning_functions.get_years_columns()

df=cleaning_functions.add_country_column(df)

df["Indicator"]=df["Unnamed: 4"].ffill()
df["Purpose"]=df["Unnamed: 5"].fillna(df["Unnamed: 6"])
df=df[df["Purpose"].notna()]

df=cleaning_functions.reshape_years(df,
                                    ["Country","Indicator","Purpose","Units"],
                                     years_columns)

output_file="C:/Users/LENOVO/OneDrive/Documents/Desktop/Tourism-Data-Analysis/data/cleaned/inbound_tourism_purpose_cleaned.csv"
cleaning_functions.save_cleaned(df,output_file)

print("cleaning completed")

