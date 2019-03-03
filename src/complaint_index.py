import pandas as pd
import numpy as np
import import_ipynb

import base
from base import get_main_city_data, get_city_zip_data

import boroughs
from boroughs import get_borough_zipcodes

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
            borough_population_counter[borough] += zipcodes_population_table[zipcode]

if __name__ == "__main__":
    # Example for getting the main data in a dataframe
    main_data_df = get_main_city_data()
    zip_data_df = get_city_zip_data()

    borough_zipcodes = get_borough_zipcodes(main_data_df)

#     total_complaints_borough = get_main_city_data().groupby("Borough").size().to_dict()
#
# #### can be fixed
#
#
# complainer_totals = {
#         boroughs_list[0]: int(total_complaints_borough[boroughs_list[0]]),
#         boroughs_list[1]: int(total_complaints_borough[boroughs_list[1]]),
#         boroughs_list[2]: int(total_complaints_borough[boroughs_list[2]]),
#         boroughs_list[3]: int(total_complaints_borough[boroughs_list[3]]),
#         boroughs_list[4]: int(total_complaints_borough[boroughs_list[4]])
#         }
#
#
#
# brooklyn_populace = pd.DataFrame( ## brooklyn
#     {
#         "Borough": boroughs_list[0],
#         "Complainer Totals": complainer_totals[boroughs_list[0]],
#         "Population": count_nyc_people()[boroughs_list[0]],
#         "Complainer-Index": complainer_totals[boroughs_list[0]]/int(count_nyc_people()[boroughs_list[0]])
#     }, index={0}
# )
#
#
# queens_populace = pd.DataFrame( ## queens
#     {
#         "Borough": boroughs_list[1],
#         "Complainer Totals": complainer_totals[boroughs_list[1]],
#         "Population": count_nyc_people()[boroughs_list[1]],
#         "Complainer-Index": complainer_totals[boroughs_list[1]]/int(count_nyc_people()[boroughs_list[1]])
#
#
#     }, index={1}
# )
#
# bronx_populace = pd.DataFrame( ## bronx
#     {
#         "Borough": boroughs_list[2],
#         "Complainer Totals": complainer_totals[boroughs_list[2]],
#         "Population": count_nyc_people()[boroughs_list[2]],
#         "Complainer-Index": complainer_totals[boroughs_list[2]]/int(count_nyc_people()[boroughs_list[2]])
#
#     }, index={2}
# )
#
# si_populace = pd.DataFrame( ## staten island
#     {
#         "Borough": boroughs_list[3],
#         "Complainer Totals": complainer_totals[boroughs_list[3]],
#         "Population": count_nyc_people()[boroughs_list[3]],
#         "Complainer-Index": complainer_totals[boroughs_list[3]]/int(count_nyc_people()[boroughs_list[3]])
#
#     }, index={3}
# )
#
# manhattan_populace = pd.DataFrame( ## staten island
#     {
#         "Borough": boroughs_list[4],
#         "Complainer Totals": total_complaints_borough[boroughs_list[4]],
#         "Population": count_nyc_people()[boroughs_list[4]],
#         "Complainer-Index": complainer_totals[boroughs_list[4]]/int(count_nyc_people()[boroughs_list[4]])
#
#     }, index={4}
# )
#
#
# all_boroughs = brooklyn_populace.append([queens_populace, bronx_populace, si_populace, manhattan_populace])
#
# print(all_boroughs)
