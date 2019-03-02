# complainer- index

import pandas as pd
import numpy as np

import import_ipynb
import Actions
from Actions import define_base_obj_to_use
from Actions import zipcodes_population_obj


# from Actions import main_data_dataframe, pop_zip_array # maybe don't need to be recreated this way
from Actions import main_data_dataframe
from Actions import pop_zip_array
from Actions import zip_files_df
from Actions import boroughs_array


popular_complaints = pd.Series(main_data_dataframe.groupby('Complaint Type').size().sort_values(ascending=False))
top_ten_pop_complaints = pd.Series(popular_complaints[:10])
complaints_tops_names = top_ten_pop_complaints.keys()

def define_zipcode_tables():
    obj = {}
    for x in range(10):
        obj[x] = main_data_dataframe.loc[main_data_dataframe.Zip == pop_zip_array[x]]
        # obj[pop_zip_array[x]] = main_data_dataframe.loc[main_data_dataframe.Zip == float(pop_zip_array[x])]
    return obj



def nyc_top_complainers():  #****#
    # obj = {}
    obj = {
    (pop_zip_array[0]): define_base_obj_to_use(),
    pop_zip_array[1]: define_base_obj_to_use(),
    pop_zip_array[2]: define_base_obj_to_use(),
    pop_zip_array[3]: define_base_obj_to_use(),
    pop_zip_array[4]: define_base_obj_to_use(),
    pop_zip_array[5]: define_base_obj_to_use(),
    pop_zip_array[6]: define_base_obj_to_use(),
    pop_zip_array[7]: define_base_obj_to_use(),
    pop_zip_array[8]: define_base_obj_to_use(),
    pop_zip_array[9]: define_base_obj_to_use()
    }


    zip_obj = {}
    for index in range(10): ############# could make helper function
        zip_obj[pop_zip_array[index]] =  define_zipcode_tables()[index]["Complaint Type"]
        # obj[pop_zip_array[x]] = define_base_obj_to_use()

    # ends loops

    complainers_obj = define_base_obj_to_use()
    for yy in range(10):
        for x in define_zipcode_tables()[yy]["Complaint Type"]:
            if x not in complaints_tops_names:
                pass
            elif (x in complainers_obj):
                obj[pop_zip_array[yy]][x] += 1
            else:
                obj[pop_zip_array[yy]][x] = 1
    return(obj)



### zip_code-complaints data frames

first_complainer_df = pd.DataFrame(  #### map
     { "Zip": pop_zip_array[0],
     complaints_tops_names[0]: nyc_top_complainers()[pop_zip_array[0]][complaints_tops_names[0]],
     complaints_tops_names[1]: nyc_top_complainers()[pop_zip_array[0]][complaints_tops_names[1]],
     complaints_tops_names[2]: nyc_top_complainers()[pop_zip_array[0]][complaints_tops_names[2]],
     complaints_tops_names[3]: nyc_top_complainers()[pop_zip_array[0]][complaints_tops_names[3]],
     complaints_tops_names[4]: nyc_top_complainers()[pop_zip_array[0]][complaints_tops_names[4]],
     complaints_tops_names[5]: nyc_top_complainers()[pop_zip_array[0]][complaints_tops_names[4]],
     complaints_tops_names[6]: nyc_top_complainers()[pop_zip_array[0]][complaints_tops_names[6]],
     complaints_tops_names[7]: nyc_top_complainers()[pop_zip_array[0]][complaints_tops_names[7]],
     complaints_tops_names[8]: nyc_top_complainers()[pop_zip_array[0]][complaints_tops_names[8]],
     complaints_tops_names[9]: nyc_top_complainers()[pop_zip_array[0]][complaints_tops_names[9]],

 }, index={0}
)

second_complainer_df = pd.DataFrame(
     { "Zip": pop_zip_array[1],
     complaints_tops_names[0]: nyc_top_complainers()[pop_zip_array[1]][complaints_tops_names[0]],
     complaints_tops_names[1]: nyc_top_complainers()[pop_zip_array[1]][complaints_tops_names[1]],
     complaints_tops_names[2]: nyc_top_complainers()[pop_zip_array[1]][complaints_tops_names[2]],
     complaints_tops_names[3]: nyc_top_complainers()[pop_zip_array[1]][complaints_tops_names[3]],
     complaints_tops_names[4]: nyc_top_complainers()[pop_zip_array[1]][complaints_tops_names[4]],
     complaints_tops_names[5]: nyc_top_complainers()[pop_zip_array[1]][complaints_tops_names[4]],
     complaints_tops_names[6]: nyc_top_complainers()[pop_zip_array[1]][complaints_tops_names[6]],
     complaints_tops_names[7]: nyc_top_complainers()[pop_zip_array[1]][complaints_tops_names[7]],
     complaints_tops_names[8]: nyc_top_complainers()[pop_zip_array[1]][complaints_tops_names[8]],
     complaints_tops_names[9]: nyc_top_complainers()[pop_zip_array[1]][complaints_tops_names[9]],

 }, index={1}
)


third_complainer_df = pd.DataFrame(
     { "Zip": pop_zip_array[2],
     complaints_tops_names[0]: nyc_top_complainers()[pop_zip_array[2]][complaints_tops_names[0]],
     complaints_tops_names[1]: nyc_top_complainers()[pop_zip_array[2]][complaints_tops_names[1]],
     complaints_tops_names[2]: nyc_top_complainers()[pop_zip_array[2]][complaints_tops_names[2]],
     complaints_tops_names[3]: nyc_top_complainers()[pop_zip_array[2]][complaints_tops_names[3]],
     complaints_tops_names[4]: nyc_top_complainers()[pop_zip_array[2]][complaints_tops_names[4]],
     complaints_tops_names[5]: nyc_top_complainers()[pop_zip_array[2]][complaints_tops_names[4]],
     complaints_tops_names[6]: nyc_top_complainers()[pop_zip_array[2]][complaints_tops_names[6]],
     complaints_tops_names[7]: nyc_top_complainers()[pop_zip_array[2]][complaints_tops_names[7]],
     complaints_tops_names[8]: nyc_top_complainers()[pop_zip_array[2]][complaints_tops_names[8]],
     complaints_tops_names[9]: nyc_top_complainers()[pop_zip_array[2]][complaints_tops_names[9]],

 }, index={2}
)


fourth_complainer_df = pd.DataFrame(
     {"Zip": pop_zip_array[3],
     complaints_tops_names[0]: nyc_top_complainers()[pop_zip_array[3]][complaints_tops_names[0]],
     complaints_tops_names[1]: nyc_top_complainers()[pop_zip_array[3]][complaints_tops_names[1]],
     complaints_tops_names[2]: nyc_top_complainers()[pop_zip_array[3]][complaints_tops_names[2]],
     complaints_tops_names[3]: nyc_top_complainers()[pop_zip_array[3]][complaints_tops_names[3]],
     complaints_tops_names[4]: nyc_top_complainers()[pop_zip_array[3]][complaints_tops_names[4]],
     complaints_tops_names[5]: nyc_top_complainers()[pop_zip_array[3]][complaints_tops_names[4]],
     complaints_tops_names[6]: nyc_top_complainers()[pop_zip_array[3]][complaints_tops_names[6]],
     complaints_tops_names[7]: nyc_top_complainers()[pop_zip_array[3]][complaints_tops_names[7]],
     complaints_tops_names[8]: nyc_top_complainers()[pop_zip_array[3]][complaints_tops_names[8]],
     complaints_tops_names[9]: nyc_top_complainers()[pop_zip_array[3]][complaints_tops_names[9]],

 }, index={3}
)


fifth_complainer_df = pd.DataFrame(
     {"Zip": pop_zip_array[4],
     complaints_tops_names[0]: nyc_top_complainers()[pop_zip_array[4]][complaints_tops_names[0]],
     complaints_tops_names[1]: nyc_top_complainers()[pop_zip_array[4]][complaints_tops_names[1]],
     complaints_tops_names[2]: nyc_top_complainers()[pop_zip_array[4]][complaints_tops_names[2]],
     complaints_tops_names[3]: nyc_top_complainers()[pop_zip_array[4]][complaints_tops_names[3]],
     complaints_tops_names[4]: nyc_top_complainers()[pop_zip_array[4]][complaints_tops_names[4]],
     complaints_tops_names[5]: nyc_top_complainers()[pop_zip_array[4]][complaints_tops_names[4]],
     complaints_tops_names[6]: nyc_top_complainers()[pop_zip_array[4]][complaints_tops_names[6]],
     complaints_tops_names[7]: nyc_top_complainers()[pop_zip_array[4]][complaints_tops_names[7]],
     complaints_tops_names[8]: nyc_top_complainers()[pop_zip_array[4]][complaints_tops_names[8]],
     complaints_tops_names[9]: nyc_top_complainers()[pop_zip_array[4]][complaints_tops_names[9]],

 }, index={4}
)


sixth_complainer_df = pd.DataFrame(
     {"Zip": pop_zip_array[5],
     complaints_tops_names[0]: nyc_top_complainers()[pop_zip_array[5]][complaints_tops_names[0]],
     complaints_tops_names[1]: nyc_top_complainers()[pop_zip_array[5]][complaints_tops_names[1]],
     complaints_tops_names[2]: nyc_top_complainers()[pop_zip_array[5]][complaints_tops_names[2]],
     complaints_tops_names[3]: nyc_top_complainers()[pop_zip_array[5]][complaints_tops_names[3]],
     complaints_tops_names[4]: nyc_top_complainers()[pop_zip_array[5]][complaints_tops_names[4]],
     complaints_tops_names[5]: nyc_top_complainers()[pop_zip_array[5]][complaints_tops_names[4]],
     complaints_tops_names[6]: nyc_top_complainers()[pop_zip_array[5]][complaints_tops_names[6]],
     complaints_tops_names[7]: nyc_top_complainers()[pop_zip_array[5]][complaints_tops_names[7]],
     complaints_tops_names[8]: nyc_top_complainers()[pop_zip_array[5]][complaints_tops_names[8]],
     complaints_tops_names[9]: nyc_top_complainers()[pop_zip_array[5]][complaints_tops_names[9]],

 }, index={5}
)

seventh_complainer_df = pd.DataFrame(
     {"Zip": pop_zip_array[6],
     complaints_tops_names[0]: nyc_top_complainers()[pop_zip_array[6]][complaints_tops_names[0]],
     complaints_tops_names[1]: nyc_top_complainers()[pop_zip_array[6]][complaints_tops_names[1]],
     complaints_tops_names[2]: nyc_top_complainers()[pop_zip_array[6]][complaints_tops_names[2]],
     complaints_tops_names[3]: nyc_top_complainers()[pop_zip_array[6]][complaints_tops_names[3]],
     complaints_tops_names[4]: nyc_top_complainers()[pop_zip_array[6]][complaints_tops_names[4]],
     complaints_tops_names[5]: nyc_top_complainers()[pop_zip_array[6]][complaints_tops_names[4]],
     complaints_tops_names[6]: nyc_top_complainers()[pop_zip_array[6]][complaints_tops_names[6]],
     complaints_tops_names[7]: nyc_top_complainers()[pop_zip_array[6]][complaints_tops_names[7]],
     complaints_tops_names[8]: nyc_top_complainers()[pop_zip_array[6]][complaints_tops_names[8]],
     complaints_tops_names[9]: nyc_top_complainers()[pop_zip_array[6]][complaints_tops_names[9]],

 }, index={6}
)

eighth_complainer_df = pd.DataFrame(
     {
     "Zip": pop_zip_array[7],
     complaints_tops_names[0]: nyc_top_complainers()[pop_zip_array[7]][complaints_tops_names[0]],
     complaints_tops_names[1]: nyc_top_complainers()[pop_zip_array[7]][complaints_tops_names[1]],
     complaints_tops_names[2]: nyc_top_complainers()[pop_zip_array[7]][complaints_tops_names[2]],
     complaints_tops_names[3]: nyc_top_complainers()[pop_zip_array[7]][complaints_tops_names[3]],
     complaints_tops_names[4]: nyc_top_complainers()[pop_zip_array[7]][complaints_tops_names[4]],
     complaints_tops_names[5]: nyc_top_complainers()[pop_zip_array[7]][complaints_tops_names[4]],
     complaints_tops_names[6]: nyc_top_complainers()[pop_zip_array[7]][complaints_tops_names[6]],
     complaints_tops_names[7]: nyc_top_complainers()[pop_zip_array[7]][complaints_tops_names[7]],
     complaints_tops_names[8]: nyc_top_complainers()[pop_zip_array[7]][complaints_tops_names[8]],
     complaints_tops_names[9]: nyc_top_complainers()[pop_zip_array[7]][complaints_tops_names[9]],

 }, index={7}
)

nineth_complainer_df = pd.DataFrame(
     {"Zip": pop_zip_array[8],
     complaints_tops_names[0]: nyc_top_complainers()[pop_zip_array[8]][complaints_tops_names[0]],
     complaints_tops_names[1]: nyc_top_complainers()[pop_zip_array[8]][complaints_tops_names[1]],
     complaints_tops_names[2]: nyc_top_complainers()[pop_zip_array[8]][complaints_tops_names[2]],
     complaints_tops_names[3]: nyc_top_complainers()[pop_zip_array[8]][complaints_tops_names[3]],
     complaints_tops_names[4]: nyc_top_complainers()[pop_zip_array[8]][complaints_tops_names[4]],
     complaints_tops_names[5]: nyc_top_complainers()[pop_zip_array[8]][complaints_tops_names[4]],
     complaints_tops_names[6]: nyc_top_complainers()[pop_zip_array[8]][complaints_tops_names[6]],
     complaints_tops_names[7]: nyc_top_complainers()[pop_zip_array[8]][complaints_tops_names[7]],
     complaints_tops_names[8]: nyc_top_complainers()[pop_zip_array[8]][complaints_tops_names[8]],
     complaints_tops_names[9]: nyc_top_complainers()[pop_zip_array[8]][complaints_tops_names[9]],
     "Zip": pop_zip_array[8]
 }, index={8}
)

tenth_complainer_df = pd.DataFrame(
     {'Zip': pop_zip_array[9],
     complaints_tops_names[0]: nyc_top_complainers()[pop_zip_array[9]][complaints_tops_names[0]],
     complaints_tops_names[1]: nyc_top_complainers()[pop_zip_array[9]][complaints_tops_names[1]],
     complaints_tops_names[2]: nyc_top_complainers()[pop_zip_array[9]][complaints_tops_names[2]],
     complaints_tops_names[3]: nyc_top_complainers()[pop_zip_array[9]][complaints_tops_names[3]],
     complaints_tops_names[4]: nyc_top_complainers()[pop_zip_array[9]][complaints_tops_names[4]],
     complaints_tops_names[5]: nyc_top_complainers()[pop_zip_array[9]][complaints_tops_names[4]],
     complaints_tops_names[6]: nyc_top_complainers()[pop_zip_array[9]][complaints_tops_names[6]],
     complaints_tops_names[7]: nyc_top_complainers()[pop_zip_array[9]][complaints_tops_names[7]],
     complaints_tops_names[8]: nyc_top_complainers()[pop_zip_array[9]][complaints_tops_names[8]],
     complaints_tops_names[9]: nyc_top_complainers()[pop_zip_array[9]][complaints_tops_names[9]],
 }, index={9}
)

zipcodes_with_top_complaints = first_complainer_df.append([second_complainer_df, third_complainer_df, fourth_complainer_df, fifth_complainer_df, sixth_complainer_df, seventh_complainer_df, eighth_complainer_df, nineth_complainer_df, tenth_complainer_df])

zipcodes_with_top_complaints
