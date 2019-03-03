import pandas as pd
import numpy as np
import import_ipynb

import base
from base import get_main_city_data, get_key_complaints, get_top_complaints

def get_boroughs(main_data_df):
    return pd.Series(main_data_df['Borough'].dropna().unique())[:5]

def get_boroughs_table(main_data_df):
    borough_table = {}
    boroughs = get_boroughs(main_data_df)
    for borough in boroughs:
        borough_table[borough] = main_data_df.loc[main_data_df.Borough == borough].dropna()
    return borough_table

def get_borough_zipcodes(main_data_df):

    # Store dict of boroughs and their associated zip codes
    borough_zips = {}

    # Dict of all boroughs and their raw data
    boroughs_table = get_boroughs_table(main_data_df)

    for borough in boroughs_table.keys():
        for zipcode in boroughs_table[borough]['Zip']:
            if not borough in borough_zips.keys():
                borough_zips[borough] = []
            if not zipcode in borough_zips[borough]:
                borough_zips[borough].append(zipcode)
    return borough_zips

def calculate_borough_complainers(main_data_df, complaints): ### just tweak and build off this

    # Dict of all the boroughs and their raw data
    boroughs_table = get_boroughs_table(main_data_df)

    # Dict of all the boroughs and their complaint counts
    borough_complaints = get_key_complaints(boroughs_table.keys(), complaints)

    for borough in boroughs_table.keys():
        for complaint in boroughs_table[borough]["Complaint Type"]:
            # Skip any complaint not in our top ten
            if not complaint in complaints:
                continue
            borough_complaints[borough][complaint] +=1
    return borough_complaints

if __name__ == "__main__":

    # Example for getting the main data in a dataframe
    main_data_df = get_main_city_data()

    # Get the top 10 complaints_count complaints
    top_complaints = get_top_complaints(main_data_df, count=10)
    top_ten_complaint_names = top_complaints.keys()

    # Build hash with top complaints
    nyc_complainers = calculate_borough_complainers(main_data_df, top_complaints)

    borough_complaints_dfs = []
    for borough in nyc_complainers.keys():
        complainer_df = pd.DataFrame( #### consider mapping
             {
                'Borough'                   : borough,
                top_ten_complaint_names[0]  : nyc_complainers[borough][top_ten_complaint_names[0]],
                top_ten_complaint_names[1]  : nyc_complainers[borough][top_ten_complaint_names[1]],
                top_ten_complaint_names[2]  : nyc_complainers[borough][top_ten_complaint_names[2]],
                top_ten_complaint_names[3]  : nyc_complainers[borough][top_ten_complaint_names[3]],
                top_ten_complaint_names[4]  : nyc_complainers[borough][top_ten_complaint_names[4]],
                top_ten_complaint_names[5]  : nyc_complainers[borough][top_ten_complaint_names[4]],
                top_ten_complaint_names[6]  : nyc_complainers[borough][top_ten_complaint_names[6]],
                top_ten_complaint_names[7]  : nyc_complainers[borough][top_ten_complaint_names[7]],
                top_ten_complaint_names[8]  : nyc_complainers[borough][top_ten_complaint_names[8]],
                top_ten_complaint_names[9]  : nyc_complainers[borough][top_ten_complaint_names[9]],
            }, index={len(borough_complaints_dfs)+1}
        )
        borough_complaints_dfs.append(complainer_df)
        print(complainer_df)
