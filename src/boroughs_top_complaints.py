import pandas as pd
import numpy as np
import import_ipynb
import Actions
from Actions import get_main_city_data, get_boroughs

def get_top_complaints(main_data_df, count=10):
    popular_complaints = pd.Series(main_data_df.groupby('Complaint Type').size().sort_values(ascending=False))
    if count > len(popular_complaints):
        print("Count cannot be longer than the number of complaints")
        count = len(popular_complaints)
    return pd.Series(popular_complaints[:count])

def get_complaint_counter(complaints):
    complaints_counter = {}
    for complaint in complaints:
        complaints_counter[complaint] = 0
    return complaints_counter

def create_borough_complaints(complaints, boroughs):
    borough_complaints = {}
    complaints_counter = get_complaint_counter(complaints)
    for borough in boroughs:
        borough_complaints[borough] = complaints_counter
    return borough_complaints

def get_boroughs_tables(main_data_df, boroughs):
    borough_table = {}
    for borough in boroughs:
        borough_table[borough] = main_data_df.loc[main_data_df.Borough == borough]
    return borough_table

def get_nyc_complainers(boroughs_table, complaints): ### just tweak and build off this
    borough_obj = {}

    borough_complaints = create_borough_complaints(complaints, boroughs_table.keys())

    for borough in boroughs_table.keys():
        borough_obj[borough] = borough_complaints[borough]
        for complaint in boroughs_table[borough]["Complaint Type"]:
            # Skip any complaint not in our top ten
            if not complaint in complaints:
                continue
            elif complaint in borough_obj[borough].keys():
                borough_obj[borough][complaint] +=1
    return borough_obj

if __name__ == "__main__":

    # Example for getting the main data in a dataframe
    main_data_df = get_main_city_data()

    # Get top 10 complaints
    top_ten_complaints = get_top_complaints(main_data_df, count=10)

    # Get the names of the top 10 top_ten_complaint_names
    top_ten_complaint_names = top_ten_complaints.keys()
    boroughs_list = get_boroughs(main_data_df)
    borough_table = get_boroughs_tables(main_data_df, boroughs_list)
    nyc_complainers = get_nyc_complainers(borough_table, top_ten_complaint_names)

    bronx_complainer_df = pd.DataFrame( #### consider mapping
         {
            'Borough'                   : boroughs_list[0],
            top_ten_complaint_names[0]  : nyc_complainers['BRONX'][top_ten_complaint_names[0]],
            top_ten_complaint_names[1]  : nyc_complainers['BRONX'][top_ten_complaint_names[1]],
            top_ten_complaint_names[2]  : nyc_complainers['BRONX'][top_ten_complaint_names[2]],
            top_ten_complaint_names[3]  : nyc_complainers['BRONX'][top_ten_complaint_names[3]],
            top_ten_complaint_names[4]  : nyc_complainers['BRONX'][top_ten_complaint_names[4]],
            top_ten_complaint_names[5]  : nyc_complainers['BRONX'][top_ten_complaint_names[4]],
            top_ten_complaint_names[6]  : nyc_complainers['BRONX'][top_ten_complaint_names[6]],
            top_ten_complaint_names[7]  : nyc_complainers['BRONX'][top_ten_complaint_names[7]],
            top_ten_complaint_names[8]  : nyc_complainers['BRONX'][top_ten_complaint_names[8]],
            top_ten_complaint_names[9]  : nyc_complainers['BRONX'][top_ten_complaint_names[9]],
        }, index={0}
    )

    brooklyn_complainer_df = pd.DataFrame(
         {
            'Borough'                   : boroughs_list[1],
            top_ten_complaint_names[0]  : nyc_complainers['BROOKLYN'][top_ten_complaint_names[0]],
            top_ten_complaint_names[1]  : nyc_complainers['BROOKLYN'][top_ten_complaint_names[1]],
            top_ten_complaint_names[2]  : nyc_complainers['BROOKLYN'][top_ten_complaint_names[2]],
            top_ten_complaint_names[3]  : nyc_complainers['BROOKLYN'][top_ten_complaint_names[3]],
            top_ten_complaint_names[4]  : nyc_complainers['BROOKLYN'][top_ten_complaint_names[4]],
            top_ten_complaint_names[5]  : nyc_complainers['BROOKLYN'][top_ten_complaint_names[4]],
            top_ten_complaint_names[6]  : nyc_complainers['BROOKLYN'][top_ten_complaint_names[6]],
            top_ten_complaint_names[7]  : nyc_complainers['BROOKLYN'][top_ten_complaint_names[7]],
            top_ten_complaint_names[8]  : nyc_complainers['BROOKLYN'][top_ten_complaint_names[8]],
            top_ten_complaint_names[9]  : nyc_complainers['BROOKLYN'][top_ten_complaint_names[9]],
        }, index={1}
    )

    manhattan_complainer_df = pd.DataFrame(
         {
            'Borough'                   : boroughs_list[2],
            top_ten_complaint_names[0]  : nyc_complainers['MANHATTAN'][top_ten_complaint_names[0]],
            top_ten_complaint_names[1]  : nyc_complainers['MANHATTAN'][top_ten_complaint_names[1]],
            top_ten_complaint_names[2]  : nyc_complainers['MANHATTAN'][top_ten_complaint_names[2]],
            top_ten_complaint_names[3]  : nyc_complainers['MANHATTAN'][top_ten_complaint_names[3]],
            top_ten_complaint_names[4]  : nyc_complainers['MANHATTAN'][top_ten_complaint_names[4]],
            top_ten_complaint_names[5]  : nyc_complainers['MANHATTAN'][top_ten_complaint_names[4]],
            top_ten_complaint_names[6]  : nyc_complainers['MANHATTAN'][top_ten_complaint_names[6]],
            top_ten_complaint_names[7]  : nyc_complainers['MANHATTAN'][top_ten_complaint_names[7]],
            top_ten_complaint_names[8]  : nyc_complainers['MANHATTAN'][top_ten_complaint_names[8]],
            top_ten_complaint_names[9]  : nyc_complainers['MANHATTAN'][top_ten_complaint_names[9]],
        }, index={2}
    )

    queens_complainer_df = pd.DataFrame(
         {
            'Borough'                   : boroughs_list[3],
            top_ten_complaint_names[0]  : nyc_complainers['QUEENS'][top_ten_complaint_names[0]],
            top_ten_complaint_names[1]  : nyc_complainers['QUEENS'][top_ten_complaint_names[1]],
            top_ten_complaint_names[2]  : nyc_complainers['QUEENS'][top_ten_complaint_names[2]],
            top_ten_complaint_names[3]  : nyc_complainers['QUEENS'][top_ten_complaint_names[3]],
            top_ten_complaint_names[4]  : nyc_complainers['QUEENS'][top_ten_complaint_names[4]],
            top_ten_complaint_names[5]  : nyc_complainers['QUEENS'][top_ten_complaint_names[4]],
            top_ten_complaint_names[6]  : nyc_complainers['QUEENS'][top_ten_complaint_names[6]],
            top_ten_complaint_names[7]  : nyc_complainers['QUEENS'][top_ten_complaint_names[7]],
            top_ten_complaint_names[8]  : nyc_complainers['QUEENS'][top_ten_complaint_names[8]],
            top_ten_complaint_names[9]  : nyc_complainers['QUEENS'][top_ten_complaint_names[9]],
        }, index={3}
    )

    staten_island_complainer_df = pd.DataFrame(
         {
            'Borough'                   : boroughs_list[4],
            top_ten_complaint_names[0]  : nyc_complainers['STATEN ISLAND'][top_ten_complaint_names[0]],
            top_ten_complaint_names[1]  : nyc_complainers['STATEN ISLAND'][top_ten_complaint_names[1]],
            top_ten_complaint_names[2]  : nyc_complainers['STATEN ISLAND'][top_ten_complaint_names[2]],
            top_ten_complaint_names[3]  : nyc_complainers['STATEN ISLAND'][top_ten_complaint_names[3]],
            top_ten_complaint_names[4]  : nyc_complainers['STATEN ISLAND'][top_ten_complaint_names[4]],
            top_ten_complaint_names[5]  : nyc_complainers['STATEN ISLAND'][top_ten_complaint_names[4]],
            top_ten_complaint_names[6]  : nyc_complainers['STATEN ISLAND'][top_ten_complaint_names[6]],
            top_ten_complaint_names[7]  : nyc_complainers['STATEN ISLAND'][top_ten_complaint_names[7]],
            top_ten_complaint_names[8]  : nyc_complainers['STATEN ISLAND'][top_ten_complaint_names[8]],
            top_ten_complaint_names[9]  : nyc_complainers['STATEN ISLAND'][top_ten_complaint_names[9]],
        }, index={4}
    )


    borough_with_complaints = bronx_complainer_df.append([brooklyn_complainer_df, manhattan_complainer_df, queens_complainer_df, staten_island_complainer_df])
