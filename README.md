# DBRS-Technical-Project-Josh-Deiner



## Files Directory 

**complaintsbyborough.ipynb**
functional

Contains code intended parse data from xlsx sheet, store data in Pandas DataFrame Object,
develop dictionaries to be comprised of major complaints and their frequencies, belonging to a specific Borough.
DataFrames appended to construct full table
.


**Population.ipynb**

Non-functional file. 
Contains code intended parse data from xlsx sheet, store data in Pandas DataFrame Object,
develop dictionaries to be comprised of major complaints and their frequencies, belonging to a specific zip code.
 

**Actions.ipynb**
Description of functions used and not used.

functions

get_all_complain_types():

def get_entries_by_year(year):

def group_zips_by_borough():

get_most_popular_complain_types():

**main** 

if __name__ == "__main__":
	# Get all complaint types
	complaint_types = get_all_complain_types()

	# Get the number of occurences for each complaint type
	ct_series = pd.Index(complaint_types)

	# Sort the complaint types by descending order
	ct_dict = ct_series.value_counts()

	# Get top ten complaint types and store in array
	top_ten_complaints = ct_dict.keys()[:10]
	print(top_ten_complaints)

	# Get zip codes and population for each borough
	borough_zips = group_zips_by_borough()
	print(borough_zips)

	# Example of getting population for BROOKLYN
	brooklyn_population = 0
	for zip_code in borough_zips['BROOKLYN'].keys():
		brooklyn_population += int(borough_zips['BROOKLYN'][zip_code])
	print(brooklyn_population)

	# COMMENTED PRINT OUT FOR EASY READABILITY
	entries = get_entries_by_year(2017)
	e_df = pd.DataFrame(entries)
	# print(e_df)
