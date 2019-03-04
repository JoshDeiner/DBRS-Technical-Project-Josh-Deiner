import requests
import pandas as pd
import numpy as np

def get_main_city_data(path='../resources/311_data_nyc_open_data_year_2017.xlsx'):
    city_data = pd.read_excel(path).drop_duplicates(keep='first')
    main_data_df = pd.DataFrame( # drop nas
         {
            "Unique Key"    : city_data["Unique Key"],
            "Created Date"  : city_data["Created Date"],
            "Complaint Type": city_data["Complaint Type"],
            "Zip"           : city_data["Incident Zip"],
            "Borough"       : city_data["Borough"]
         }
    )
    return main_data_df

def get_city_zip_data(path='../resources/Zips2010_90.xlsx'):
    zip_data = pd.read_excel(path).drop_duplicates(keep='first')
    zip_df = pd.DataFrame(
        {
            "Zip"           : zip_data["Incident Zips"],
            "Population"    : zip_data["Population"]
        }
    )
    return zip_df

def get_top_complaints(main_data_df, count=10):
    popular_complaints = pd.Series(main_data_df.groupby('Complaint Type').size().sort_values(ascending=False))
    if count > len(popular_complaints):
        print("Count cannot be longer than the number of complaints")
        count = len(popular_complaints)
    if count == -1:
        return pd.Series(popular_complaints)
    else:
        return pd.Series(popular_complaints[:count])

def get_complaints_counter(complaints):
    complaints_counter = {}
    for complaint in complaints.keys():
        complaints_counter[complaint] = 0
    return complaints_counter

def get_key_complaints(list, complaints):
    complaints_table = {}
    for elem in list:
        complaints_table[elem] = get_complaints_counter(complaints)
    return complaints_table



if __name__ == "__main__":

    # Example for getting the main data in a dataframe
    main_data_df = get_main_city_data()

    # Examle for getting the zip data in a dataframe
    zip_data_df = get_city_zip_data()
