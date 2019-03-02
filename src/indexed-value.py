# complainer- index

import pandas as pd #
import numpy as np #

import import_ipynb
import Actions
from Actions import boroughs_array

from Actions import zip_files_df # maybe don't need to be recreated this way
from Actions import new_group_boroughs_by_zips
from Actions import city_data_file_read

#### maybe make these not global or move around to other actions one

total_complaints_borough = city_data_file_read.groupby("Borough").size().to_dict()



def define_borough_zipcodes_obj(): ### check if worked
    si_zips = pd.Series(new_group_boroughs_by_zips()['STATEN ISLAND'])
    bronx_zips = pd.Series(new_group_boroughs_by_zips()['BRONX'])
    queens_zips = pd.Series(new_group_boroughs_by_zips()['QUEENS'])
    brooklyn_zips = pd.Series(new_group_boroughs_by_zips()['BROOKLYN'])
    manhattan_zips = pd.Series(new_group_boroughs_by_zips()['MANHATTAN'])

    borough_zipcodes_obj = {
    "BRONX": (bronx_zips).dropna().unique(),
    "QUEENS": (queens_zips).dropna().unique(),
    "MANHATTAN": (manhattan_zips).dropna().unique(),
    "BROOKLYN" : (brooklyn_zips).dropna().unique(),
    "STATEN ISLAND": (si_zips).dropna().unique()
    }

    return(borough_zipcodes_obj)


def count_nyc_people(): # could possibly make this loop smaller
    borough_obj_counter= {
        boroughs_array[0]: 0,
        boroughs_array[1]: 0,
        boroughs_array[2]: 0,
        boroughs_array[3]: 0,
        boroughs_array[4]: 0
        }

    range_length = len(boroughs_array) # 5
    for iteration in range(range_length):
        for x in define_borough_zipcodes_obj()[boroughs_array[iteration]]:
            borough_obj_counter[boroughs_array[iteration]] += zip_files_df['Zip'][x]
    return borough_obj_counter


#### can be fixed

complainer_totals = {
    'BROOKLYN': int(total_complaints_borough['BROOKLYN']),
    'QUEENS': int(total_complaints_borough['QUEENS']),
    'BRONX': int(total_complaints_borough['BRONX']),
    'STATEN ISLAND': int(total_complaints_borough['STATEN ISLAND']),
    'MANHATTAN': int(total_complaints_borough['MANHATTAN'])
}

brooklyn_populace = pd.DataFrame( ## brooklyn
    {
        "Borough": "BROOKLYN",
        "Complainer Totals": complainer_totals["BROOKLYN"],
        "Population": count_nyc_people()["BROOKLYN"],
        "Complainer-Index": complainer_totals["BROOKLYN"]/int(count_nyc_people()["BROOKLYN"])
    }, index={0}
)


queens_populace = pd.DataFrame( ## queens
    {
        "Borough": "QUEENS",
        "Complainer Totals": complainer_totals["QUEENS"],
        "Population": count_nyc_people()["QUEENS"],
        "Complainer-Index": complainer_totals["QUEENS"]/int(count_nyc_people()["QUEENS"])


    }, index={1}
)

bronx_populace = pd.DataFrame( ## bronx
    {
        "Borough": "BRONX",
        "Complainer Totals": complainer_totals["BRONX"],
        "Population": count_nyc_people()["STATEN ISLAND"],
        "Complainer-Index": complainer_totals["BRONX"]/int(count_nyc_people()["BRONX"])

    }, index={2}
)

si_populace = pd.DataFrame( ## staten island
    {
        "Borough": "STATEN ISLAND",
        "Complainer Totals": complainer_totals["STATEN ISLAND"],
        "Population": count_nyc_people()["STATEN ISLAND"],
        "Complainer-Index": complainer_totals["STATEN ISLAND"]/int(count_nyc_people()["STATEN ISLAND"])

    }, index={3}
)

manhattan_populace = pd.DataFrame( ## staten island
    {
        "Borough": "MANHATTAN",
        "Complainer Totals": total_complaints_borough["MANHATTAN"],
        "Population": count_nyc_people()["MANHATTAN"],
        "Complainer-Index": complainer_totals["MANHATTAN"]/int(count_nyc_people()["MANHATTAN"])

    }, index={4}
)

all_boroughs = brooklyn_populace.append([queens_populace, bronx_populace, si_populace, manhattan_populace])

all_boroughs
