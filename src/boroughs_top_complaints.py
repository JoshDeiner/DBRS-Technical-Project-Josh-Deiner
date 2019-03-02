import pandas as pd
import numpy as np
import import_ipynb
import Actions
from Actions import main_data_dataframe
from Actions import define_base_obj_to_use
from Actions import define_boroughs_tables
from Actions import boroughs_array


###### top file to check out

# helper variables, maybe move within module

popular_complaints = pd.Series(main_data_dataframe.groupby('Complaint Type').size().sort_values(ascending=False))
top_ten_pop_complaints = pd.Series(popular_complaints[:10])
complaints_tops_names = top_ten_pop_complaints.keys()

def create_borough_complaints_obj():
    empty_complaints_obj = define_base_obj_to_use()
    obj = {}
    for x in boroughs_array:
        obj[x] = empty_complaints_obj
    return obj


def nyc_complainers(): ### just tweak and build off this
    borough_obj = {boroughs_array[0]: create_borough_complaints_obj()[boroughs_array[0]], boroughs_array[1]: create_borough_complaints_obj()[boroughs_array[1]], boroughs_array[2] : create_borough_complaints_obj()[boroughs_array[2]], boroughs_array[3]: create_borough_complaints_obj()[boroughs_array[3]], boroughs_array[4]: create_borough_complaints_obj()[boroughs_array[4]] }
    range_length = len(boroughs_array)
    for iteration in range(range_length):
        for complaint in define_boroughs_tables()[iteration]["Complaint Type"]:
            if complaint not in complaints_tops_names:
                pass
            elif (complaint in borough_obj[boroughs_array[iteration]] and complaint in complaints_tops_names):
                borough_obj[boroughs_array[iteration]][complaint] +=1
            else:
                borough_obj[boroughs_array[iteration]][complaint] = 1
    return borough_obj


bronx_complainer_df = pd.DataFrame( #### consider mapping
     {'Borough': boroughs_array[0],
     complaints_tops_names[0]: nyc_complainers()['BRONX'][complaints_tops_names[0]],
     complaints_tops_names[1]: nyc_complainers()['BRONX'][complaints_tops_names[1]],
     complaints_tops_names[2]: nyc_complainers()['BRONX'][complaints_tops_names[2]],
     complaints_tops_names[3]: nyc_complainers()['BRONX'][complaints_tops_names[3]],
     complaints_tops_names[4]: nyc_complainers()['BRONX'][complaints_tops_names[4]],
     complaints_tops_names[5]: nyc_complainers()['BRONX'][complaints_tops_names[4]],
     complaints_tops_names[6]: nyc_complainers()['BRONX'][complaints_tops_names[6]],
     complaints_tops_names[7]: nyc_complainers()['BRONX'][complaints_tops_names[7]],
     complaints_tops_names[8]: nyc_complainers()['BRONX'][complaints_tops_names[8]],
     complaints_tops_names[9]: nyc_complainers()['BRONX'][complaints_tops_names[9]],
 }, index={0}
)

brooklyn_complainer_df = pd.DataFrame(

     {'Borough': boroughs_array[1],
     complaints_tops_names[0]: nyc_complainers()['BROOKLYN'][complaints_tops_names[0]],
     complaints_tops_names[1]: nyc_complainers()['BROOKLYN'][complaints_tops_names[1]],
     complaints_tops_names[2]: nyc_complainers()['BROOKLYN'][complaints_tops_names[2]],
     complaints_tops_names[3]: nyc_complainers()['BROOKLYN'][complaints_tops_names[3]],
     complaints_tops_names[4]: nyc_complainers()['BROOKLYN'][complaints_tops_names[4]],
     complaints_tops_names[5]: nyc_complainers()['BROOKLYN'][complaints_tops_names[4]],
     complaints_tops_names[6]: nyc_complainers()['BROOKLYN'][complaints_tops_names[6]],
     complaints_tops_names[7]: nyc_complainers()['BROOKLYN'][complaints_tops_names[7]],
     complaints_tops_names[8]: nyc_complainers()['BROOKLYN'][complaints_tops_names[8]],
     complaints_tops_names[9]: nyc_complainers()['BROOKLYN'][complaints_tops_names[9]],
 }, index={1}
)

manhattan_complainer_df = pd.DataFrame(
     {'Borough': boroughs_array[2],
     complaints_tops_names[0]: nyc_complainers()['MANHATTAN'][complaints_tops_names[0]],
     complaints_tops_names[1]: nyc_complainers()['MANHATTAN'][complaints_tops_names[1]],
     complaints_tops_names[2]: nyc_complainers()['MANHATTAN'][complaints_tops_names[2]],
     complaints_tops_names[3]: nyc_complainers()['MANHATTAN'][complaints_tops_names[3]],
     complaints_tops_names[4]: nyc_complainers()['MANHATTAN'][complaints_tops_names[4]],
     complaints_tops_names[5]: nyc_complainers()['MANHATTAN'][complaints_tops_names[4]],
     complaints_tops_names[6]: nyc_complainers()['MANHATTAN'][complaints_tops_names[6]],
     complaints_tops_names[7]: nyc_complainers()['MANHATTAN'][complaints_tops_names[7]],
     complaints_tops_names[8]: nyc_complainers()['MANHATTAN'][complaints_tops_names[8]],
     complaints_tops_names[9]: nyc_complainers()['MANHATTAN'][complaints_tops_names[9]],
 }, index={2}
)

queens_complainer_df = pd.DataFrame(
     {'Borough': boroughs_array[3],
     complaints_tops_names[0]: nyc_complainers()['QUEENS'][complaints_tops_names[0]],
     complaints_tops_names[1]: nyc_complainers()['QUEENS'][complaints_tops_names[1]],
     complaints_tops_names[2]: nyc_complainers()['QUEENS'][complaints_tops_names[2]],
     complaints_tops_names[3]: nyc_complainers()['QUEENS'][complaints_tops_names[3]],
     complaints_tops_names[4]: nyc_complainers()['QUEENS'][complaints_tops_names[4]],
     complaints_tops_names[5]: nyc_complainers()['QUEENS'][complaints_tops_names[4]],
     complaints_tops_names[6]: nyc_complainers()['QUEENS'][complaints_tops_names[6]],
     complaints_tops_names[7]: nyc_complainers()['QUEENS'][complaints_tops_names[7]],
     complaints_tops_names[8]: nyc_complainers()['QUEENS'][complaints_tops_names[8]],
     complaints_tops_names[9]: nyc_complainers()['QUEENS'][complaints_tops_names[9]],
 }, index={3}
)

staten_island_complainer_df = pd.DataFrame(
     {'Borough': boroughs_array[4],
     complaints_tops_names[0]: nyc_complainers()['STATEN ISLAND'][complaints_tops_names[0]],
     complaints_tops_names[1]: nyc_complainers()['STATEN ISLAND'][complaints_tops_names[1]],
     complaints_tops_names[2]: nyc_complainers()['STATEN ISLAND'][complaints_tops_names[2]],
     complaints_tops_names[3]: nyc_complainers()['STATEN ISLAND'][complaints_tops_names[3]],
     complaints_tops_names[4]: nyc_complainers()['STATEN ISLAND'][complaints_tops_names[4]],
     complaints_tops_names[5]: nyc_complainers()['STATEN ISLAND'][complaints_tops_names[4]],
     complaints_tops_names[6]: nyc_complainers()['STATEN ISLAND'][complaints_tops_names[6]],
     complaints_tops_names[7]: nyc_complainers()['STATEN ISLAND'][complaints_tops_names[7]],
     complaints_tops_names[8]: nyc_complainers()['STATEN ISLAND'][complaints_tops_names[8]],
     complaints_tops_names[9]: nyc_complainers()['STATEN ISLAND'][complaints_tops_names[9]],
 }, index={4}
)


borough_with_complaints = bronx_complainer_df.append([brooklyn_complainer_df, manhattan_complainer_df, queens_complainer_df, staten_island_complainer_df])

borough_with_complaints
