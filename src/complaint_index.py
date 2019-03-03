import pandas as pd
import numpy as np
import import_ipynb

import base
from base import get_main_city_data, get_city_zip_data, get_top_complaints

import boroughs
from boroughs import get_borough_zipcodes, calculate_borough_complainers

import zipcodes
from zipcodes import get_zipcode_populations

def count_borough_population(zip_data_df, borough_zips): # could possibly make this loop smaller
    borough_population_counter = {}

    valid_zipcodes = []
    for borough in borough_zips:
        valid_zipcodes.extend(borough_zips[borough])

    zipcodes_population_table = get_zipcode_populations(zip_data_df, valid_zipcodes)

    for borough in borough_zips.keys():
        if not borough in borough_population_counter.keys():
            borough_population_counter[borough] = 0
        for zipcode in borough_zips[borough]:
            if not zipcode in zipcodes_population_table.keys():
                continue
            borough_population_counter[borough] += zipcodes_population_table[zipcode]

    return borough_population_counter

if __name__ == "__main__":
    # Example for getting the main data in a dataframe

    main_data_df = get_main_city_data()
    zip_data_df = get_city_zip_data()

    # Get population of each borough
    borough_zipcodes = get_borough_zipcodes(main_data_df)
    borough_populations = count_borough_population(zip_data_df, borough_zipcodes)
    print(borough_populations)

    # Get all the complaint types
    complaints = get_top_complaints(main_data_df, count=-1)
    top_ten_complaint_names = complaints.keys()
    borough_complainers = calculate_borough_complainers(main_data_df, complaints)

    # Get the number of all complaints per borough
    all_borough_complaints = {}
    for borough in borough_complainers.keys():
        all_borough_complaints[borough] = 0
        for complaint in borough_complainers[borough]:
            all_borough_complaints[borough] += int(borough_complainers[borough][complaint])
    print(all_borough_complaints)

    complaint_index = {}
    for borough in borough_complainers.keys():
        total_borough_size = float(borough_populations[borough])
        total_borough_complaints = float(all_borough_complaints[borough])
        complaint_index[borough] = float(total_borough_complaints / total_borough_size)
    print(pd.Series(complaint_index).sort_values(ascending=False))
