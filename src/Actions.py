import requests
import pandas as pd
import numpy as np

def get_main_city_data(path='../resources/tocopycitydata.xlsx'):
    city_data = pd.read_excel(path)
    main_data_df = pd.DataFrame( # drop nas
         {
            "Unique Key"    : city_data["Unique Key"],
            "Created Date"  : city_data["Created Date"],
            "Closed Date"   : city_data["Closed Date"],
            "Complaint Type": city_data["Complaint Type"],
            "Zip"           : city_data["Incident Zip"],
            "Status"        : city_data["Status"],
            "Borough"       : city_data["Borough"]
         }
    )
    return main_data_df

def get_city_zip_data(path='../resources/Zips2010_90.xlsx'):
    zip_data = pd.read_excel(path)
    zip_df = pd.DataFrame(
        {
            "Zip"           : zip_data["Incident Zips"],
            "Population"    : zip_data["Population"]
        }
    )
    return zip_df

def get_boroughs(main_data_df):
    return pd.Series(main_data_df['Borough'].dropna().unique())[:5]

if __name__ == "__main__":

    # Example for getting the main data in a dataframe
    main_data_df = get_main_city_data()

    # Examle for getting the zip data in a dataframe
    zip_data_df = get_city_zip_data()

    print(main_data_df)

    print(zip_data_df)
#
# def zipcodes_population_obj(zip_df): # has of zip_code file
#     obj= {}
#     pops, zips = zip_files_df['Population'], zip_files_df['Zip']
#     one_array, second_array = [], []
#     for pop_value in pops:
#         one_array.append(pop_value)
#     for zip_value in zips:
#         second_array.append(zip_value)
#     for x in range(len(one_array)-1):
#         once = one_array[x]
#         twice = second_array[x]
#         obj[twice] = once
#     return obj
#
# def group_boroughs_by_zips(main_data_df):
#     borough_list = ["BROOKLYN", "QUEENS", "BRONX", "STATEN ISLAND", "MANHATTAN"]
#     borough_zips = {
#         "BROOKLYN" : [],
#         "QUEENS": [],
#         "BRONX": [],
#         "STATEN ISLAND": [],
#         "MANHATTAN": []
#     }
#
#     borough_table = get_boroughs_tables(main_data_df, borough_list)
#
#     for borough in borough_table.keys():
#         for zipcode in borough_table[borough]['Zip']:
#             borough_zips[borough].append(float(zipcode))
#
#     return borough_zips
#
# def get_populated_zips():
#     return pd.Series([11385, 11209, 11215, 11216, 10456, 10453, 11226, 11213, 10467, 10452])
