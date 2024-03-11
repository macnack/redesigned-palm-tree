from typing import List
import numpy as np
import pandas as pd

# @profile
def get_data() -> pd.DataFrame:
    url = "https://zenodo.org/record/2826939/files/Folsom_irradiance.csv?download=1"
    return pd.read_csv(url)

@profile
def create_new_timestamp(df: pd.DataFrame) -> List[str]:
    """
    Funkcja zmieniająca format znacznika czasu z YYYY-MM-DD hh:mm:ss na YYYYmmdd_HHMMSS
    np. 2014-01-02 08:00:00 -> 20140102_080000
    """
    print('Creating new timestamp')
    new_time_stamps = []

    for idx in range(len(df)):
        timestamp = df.iloc[idx]['timeStamp']
        year = timestamp[:4]
        month = timestamp[5:7]
        day = timestamp[8:10]
        hour = timestamp[11:13]
        minute = timestamp[14:16]
        second = timestamp[17:19]
        new_time_stamp = year + month + day + '_' + hour + minute + second
        new_time_stamps.append(new_time_stamp)
        
    return new_time_stamps

@profile
def get_max_ghi_date(df):
    """
    Funkcja znajdująca największą wartość GHI (Global Horizontal Irradiance) 
    oraz czas, w którym ta wartość została zarejestrowana
    """
    print('Getting max GHI date')
    max_val = df['ghi'].values.max()
    idx = df['ghi'].values.tolist().index(max_val)
    ghi = df["ghi"].values[idx]
    date = df["new_timestamp"].values[idx]
    print(f'Max GHI was equal {ghi} on {date} UTC')
    

def main():
    df = get_data()
    df['new_timestamp'] = create_new_timestamp(df)
    get_max_ghi_date(df)
    
    
if __name__ == '__main__':
    main()