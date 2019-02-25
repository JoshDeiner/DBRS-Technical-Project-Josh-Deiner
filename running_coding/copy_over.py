import requests
import pandas as pd
import numpy as np
import csv

city_data_input_file = pd.read_excel("../../../downloads/tocopycitydata.xlsx")
zipcode_file = pd.read_excel("../../../downloads/Zips2010_90.xlsx")
csv_zip_file = zip_df.to_csv()

city_data_df = pd.DataFrame(
     {'Unique Key' : city_data_input_file["Unique Key"],
        'Created Date' : city_data_input_file["Created Date"],
        'Closed Date' : city_data_input_file["Closed Date"],
        'Complaint Type' : city_data_input_file["Complaint Type"],
        'Incident Zip' : city_data_input_file["Incident Zip"],
        'Status' : city_data_input_file["Status"],
        'Borough' : city_data_input_file["Borough"]
     })
city_data_input_file


# re_excelled_zip = zip_df.to_excel('re_excelled_zip.xlsx')
# re_excelled_city_data = city_data_df.to_excel('re_excelled_city_data.xlsx')
# zip_code_data_to_merge = pd.read_excel(re_excelled_zip)
# city_data_to_merge = pd.read_excel(re_excelled_city_data)

# city_data_to_merge
# zip_table = df.loc[df.Borough == 'BRONX']
# pd.merge(city_data_df, zip_df, on='Incident Zip', how='right') # try with just tables alone
# pd.merge(city_data_input_file, zipcode_file, how='right')

# df1.to_excel("output.xlsx")  # doctest: +SKIP
population_to_be_added = {}

# def population_finder():

def group_zips_by_borough(): # refactor
	endpoint = "https://data.cityofnewyork.us/resource/fhrw-4uyv.json?$where=incident_zip IS NOT NULL"
	response = requests.get(endpoint)
	print (response.json())
	borough_zips = {}

# 	# Get ditionary containing zip code population data
	populations = read_zip_population_data()
	populations


populations_df = pd.DataFrame(
    {
        'Incident Zip': zipcode_file['Incident Zips'],
        'Population': zipcode_file['Population']
    }
)

populations_df['Incident Zip']

populations = read_zip_population_data()
populations


def read_zip_population_data():

	populations = {}
#     incident_zips_column = zipcode_file[row]
#     population_column = zipcode_file[row]

for index, row in populations_df.iterrows():
    incident_zips_row_value = row['Incident Zip']
    population_row_value = row['Population']


#      print(index, row['delay'], row['distance'], row['origin'])

# for row in zipcode_file:
# # 		print(zipcode_file[row])

# 		print(zipcode_file)
#     for other
# 		key, value = row
# 		populations[key] = value
# 	return populations


def group_boroughs_by_zips():

    borough_list = ["BROOKLYN", "QUEENS", "BRONX", "STATEN ISLAND", "MANHATTAN"]

    borough_zips = {
    "BROOKLYN" : [],
    "QUEENS": [],
    "BRONX": [],
    "STATEN ISLAND": [],
    "MANHATTAN": []
}
    for index, row in city_data_input_file.iterrows():
        for borough in borough_list:
            if row["Borough"] == borough:
                borough_zips[borough].append(row['Incident Zip'])
                print (borough_zips)


group_boroughs_by_zips()



def define_pop_of_boroughs():
    borough_pop_dictionary = {}
    borough_list = ["BROOKLYN", "QUEENS", "BRONX", "STATEN ISLAND", "MANHATTAN"]
    print(borough_list)



    # x = pd.Series(brooklyn_zips)
# # x.sort(ascending=True, kind='mergesort', na_position='last', inplace=True)
# yy = brooklyn_zips.sort()
# yy
# sz = np.array(brooklyn_zips)
# #29 should go



first_zipcode_table = input_file.loc[input_file.Zip == '60629']
second_zipcode_table = input_file.loc[input_file.Zip == '79936']
third_zipcode_table = input_file.loc[input_file.Zip == '11368']
fourth_zipcode_table = input_file.loc[input_file.Zip == '90650']
fifth_zipcode_table = input_file.loc[input_file.Zip == '90011']
sixth_complainer_table = input_file.loc[input_file.Zip == '91331']
seventh_complainer_table = input_file.loc[input_file.Zip == '11226']
eighth_complainer_table = input_file.loc[input_file.Zip == '90201']
nine_complainer_table = input_file.loc[input_file.Zip == '11373']
ten_complainer_table = input_file.loc[input_file.Zip == '11220']



first_zipcode_table = deer.loc[deer.Zip == float(60629)]
second_zipcode_table = deer.loc[deer.Zip == float(79936)]
third_zipcode_table = deer.loc[deer.Zip == float(11368)]
fourth_zipcode_table = deer.loc[deer.Zip == float(90650)]
fifth_zipcode_table = deer.loc[deer.Zip == float(90011)]
sixth_complainer_table = deer.loc[deer.Zip == float(91331)]
seventh_complainer_table = deer.loc[deer.Zip == float(11226)]
eighth_complainer_table = deer.loc[deer.Zip == float(90201)]
nine_complainer_table = deer.loc[deer.Zip == float(11373)]
ten_complainer_table = deer.loc[deer.Zip == float(11220)]
