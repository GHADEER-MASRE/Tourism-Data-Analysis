import pandas as pd
def load_file(input_file):
    return pd.read_csv(input_file,encoding="latin1")

def add_country_column(df):
    df["Country"]=df["Basic data and indicators"].where(
        df["S."].fillna(-1)==0
    )
    df["Country"]=df["Country"].ffill()
    return df

def get_years_columns():
    return[str(year) for year in range(1995,2023)]

def reshape_years(df,id_vars,years_columns):
    df=df.melt(
        id_vars=id_vars,
        value_vars=years_columns,
        var_name="Year",
        value_name="Value"
    )
    df["Value"]=pd.to_numeric(df["Value"],errors="coerce")
    return df

def save_cleaned(df,output_file):
    df.to_csv(output_file,index=False)