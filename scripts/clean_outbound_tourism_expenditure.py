import cleaning_functions
input_file="C:/Users/LENOVO/OneDrive/Documents/Desktop/Tourism-Data-Analysis/data/raw/Outbound Tourism-Expenditure.csv"
df=cleaning_functions.load_file(input_file)

years_columns=cleaning_functions.get_years_columns()

df=cleaning_functions.add_country_column(df)

df["Indicator"]=df["Unnamed: 4"].ffill()
df["Expenditure Type"]=df["Unnamed: 5"]
df=df[df["Expenditure Type"].notna()]

df=cleaning_functions.reshape_years(df,
                                    ["Country","Indicator","Expenditure Type","Units"],
                                    years_columns)

output_file="C:/Users/LENOVO/OneDrive/Documents/Desktop/Tourism-Data-Analysis/data/cleaned/outbound_tourism_expenditure.csv"
cleaning_functions.save_cleaned(df,output_file)
print("cleaning completed")