import pandas as pd
import numpy as np
import import_ipynb

import base
from base import get_main_city_data, get_city_zip_data, get_top_complaints, get_key_complaints

import boroughs
from boroughs import get_borough_zipcodes

def get_zipcode_populations(zip_data_df, valid_zipcodes):
    zipcodes_table = {}
    zipcodes = zip_data_df.Zip
    populations = zip_data_df.Population

    for i in range (len(zip_data_df.Zip.keys())):
        if zipcodes[i] in valid_zipcodes:
            zipcodes_table[zipcodes[i]] = populations[i]
    return zipcodes_table

def get_most_populated_zipcodes(zipcodes_table, valid_zipcodes, count=10):
    all_valid_zipcodes = get_zipcode_populations(zip_data_df, valid_zipcodes)
    populated_zipcodes = pd.Series(all_valid_zipcodes).sort_values(ascending=False)[0:count]
    return populated_zipcodes

def get_zipcodes_table(main_data_df, zipcodes):
    zipcodes_table = {}
    for zipcode in zipcodes:
        zipcodes_table[zipcode] = main_data_df.loc[main_data_df.Zip == zipcode]
    return zipcodes_table

def calculate_zipcode_complainers(main_data_df, zipcodes, complaints):

    # Dict of all the boroughs and their raw data
    zipcode_table = get_zipcodes_table(main_data_df, zipcodes)

    # Dict of all the boroughs and their complaint counts
    zipcode_complaints = get_key_complaints(zipcodes, complaints)

    for zipcode in zipcodes:
        for complaint in zipcode_table[zipcode]["Complaint Type"]:
            # Skip any complaint not in our top ten
            if not complaint in complaints:
                continue
            zipcode_complaints[zipcode][complaint] +=1
    return zipcode_complaints

if __name__ == "__main__":
    main_data_df = get_main_city_data()
    zip_data_df = get_city_zip_data()

    # Get the top 10 complaints_count complaints
    top_complaints = get_top_complaints(main_data_df, count=10)
    top_ten_complaint_names = top_complaints.keys()

    borough_zips = get_borough_zipcodes(main_data_df)

    valid_zipcodes = []
    for borough in borough_zips:
        valid_zipcodes.extend(borough_zips[borough])

    top_populated_zipcodes = get_most_populated_zipcodes(zip_data_df, valid_zipcodes, count=10)
    zipcode_complainers = calculate_zipcode_complainers(main_data_df, top_populated_zipcodes.keys(), top_complaints)

    zipcode_complaints_dfs = []
    for zipcode in zipcode_complainers.keys():
        complainer_df = pd.DataFrame( #### consider mapping
             {
                'Zipcode'                   : zipcode,
                top_ten_complaint_names[0]  : zipcode_complainers[zipcode][top_ten_complaint_names[0]],
                top_ten_complaint_names[1]  : zipcode_complainers[zipcode][top_ten_complaint_names[1]],
                top_ten_complaint_names[2]  : zipcode_complainers[zipcode][top_ten_complaint_names[2]],
                top_ten_complaint_names[3]  : zipcode_complainers[zipcode][top_ten_complaint_names[3]],
                top_ten_complaint_names[4]  : zipcode_complainers[zipcode][top_ten_complaint_names[4]],
                top_ten_complaint_names[5]  : zipcode_complainers[zipcode][top_ten_complaint_names[4]],
                top_ten_complaint_names[6]  : zipcode_complainers[zipcode][top_ten_complaint_names[6]],
                top_ten_complaint_names[7]  : zipcode_complainers[zipcode][top_ten_complaint_names[7]],
                top_ten_complaint_names[8]  : zipcode_complainers[zipcode][top_ten_complaint_names[8]],
                top_ten_complaint_names[9]  : zipcode_complainers[zipcode][top_ten_complaint_names[9]],
            }, index={len(zipcode_complaints_dfs)+1}
        )
        zipcode_complaints_dfs.append(complainer_df)
        print(complainer_df)
