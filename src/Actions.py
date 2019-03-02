import requests
import pandas as pd
import numpy as np

zipcode_file = '../resources/Zips2010_90.xlsx'  # Using the 2010 Zip Code Data.
zip_files_dataframe_one = pd.read_excel(zipcode_file)
city_data_file_read= pd.read_excel("../resources/tocopycitydata.xlsx")


main_data_dataframe = pd.DataFrame( # drop nas
     {"Unique Key":city_data_file_read["Unique Key"],
        "Created Date":city_data_file_read["Created Date"],
        "Closed Date":city_data_file_read["Closed Date"],
        "Complaint Type":city_data_file_read["Complaint Type"],
        "Zip" : city_data_file_read["Incident Zip"],
        "Status": city_data_file_read["Status"],
        "Borough":city_data_file_read["Borough"]
     }
)

zip_files_df = pd.DataFrame ({
    "Zip": zip_files_dataframe_one["Incident Zips"],
    "Population": zip_files_dataframe_one["Population"]
})


pop_zip_array = pd.Series([11385, 11209, 11215, 11216, 10456, 10453, 11226, 11213, 10467, 10452]) # ****
boroughs_array = pd.Series(main_data_dataframe['Borough'].dropna().unique())[:5]
popular_complaints = pd.Series(main_data_dataframe.groupby('Complaint Type').size().sort_values(ascending=False))
top_ten_pop_complaints = pd.Series(popular_complaints[:10])
top_ten_pop_complaints_keys = top_ten_pop_complaints.keys()
complaints_tops_names = top_ten_pop_complaints.keys()



def define_boroughs_tables(): #### change to borrough input
    obj = {}
    for x in range(5):
        obj[x] = main_data_dataframe.loc[main_data_dataframe.Borough == boroughs_array[x]]
        # obj[pop_zip_array[x]] = main_data_dataframe.loc[main_data_dataframe.Zip == float(pop_zip_array[x])]
    return obj



def zipcodes_population_obj(): # has of zip_code file
    obj= {}
    pops, zips = zip_files_df['Population'], zip_files_df['Zip']
    one_array, second_array = [], []
    for pop_value in pops:
        one_array.append(pop_value)
    for zip_value in zips:
        second_array.append(zip_value)
    for x in range(len(one_array)-1):
        once = one_array[x]
        twice = second_array[x]
        obj[twice] = once
    return obj



def new_group_boroughs_by_zips(): ####### five loops

    borough_list = ["BROOKLYN", "QUEENS", "BRONX", "STATEN ISLAND", "MANHATTAN"]
    borough_zips = {
    "BROOKLYN" : [],
    "QUEENS": [],
    "BRONX": [],
    "STATEN ISLAND": [],
    "MANHATTAN": []
}

    for zipcode in define_boroughs_tables()[4]['Zip']:
        (borough_zips['BRONX'].append(float(zipcode)))
    for zipcode in define_boroughs_tables()[2]['Zip']:
        borough_zips['MANHATTAN'].append(float(zipcode))
    for zipcode in define_boroughs_tables()[1]['Zip']:
        borough_zips['QUEENS'].append(float(zipcode))
    for zipcode in define_boroughs_tables()[3]['Zip']:
        borough_zips['STATEN ISLAND'].append(float(zipcode))
    for zipcode in define_boroughs_tables()[0]['Zip']:
        borough_zips['BROOKLYN'].append(float(zipcode))
    return(borough_zips)



def define_base_obj_to_use(): # change to borroughs instead of index
    starter_complaints_obj = {}
    for x in complaints_tops_names:
        starter_complaints_obj[x] = 0
    return starter_complaints_obj
