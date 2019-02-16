# DBRS-Technical-Project-Josh-Deiner
Focus: Data sourcing, cleaning, and exploration
## Pandas and Jupyter

# Jupiter is environment. Pandas is similar to library. Have JJ display values 

### Assumptions 

Consider only the 10 most common overall complaint types

Interepreting this phrase as 10 most common complaints over the entire dataset, ie time period. 

Considering all complaint types. 
Which boroughs are the biggest "complainers" relative to the size of the population in 2017?
    =>  Meaning, calculate a complaint-index that adjusts for population of the borough.
    is this an index or percentage? 
    whether to aggregate all the number of complaints together based on boroughs. 
    
    
outline 
setup Socrata, sodapy, pandas for api/data usage

Consider only the 10 most common overall complaint types. For each borough, how many of each of those 10 types were there in 2017?
two ways to approach question. figure way to iterate through data to understand most common complaints
isolate by B, list complaints in 2017

Consider only the 10 most common overall complaint types.  For the 10 most populous zip codes, how many of each of those 10 types were there in 2017?

aggregate zip code totals. 
aggregate all the complaints 
check the complaints for the top ten zip code totals 

Considering all complaint types. Which boroughs are the biggest "complainers" relative to the size of the population in 2017? Meaning, calculate a complaint-index that adjusts for population of the borough.
* calculcate percentage of complainers. 
* aggregate complaints per B/ population. 

-- 
finall instructions 

Notes/hints:

 

*For the #311 data, programmatically source the data:
    Use the Socrata Open Data API https://dev.socrata.com/foundry/data.cityofnewyork.us/fhrw-4uyv.
*For population by #zip code you can use https://blog.splitwise.com/2013/09/18/the-2010-us-census-population-by-zip-code-totally-free/. You can just pretend ZCTA == zip and it's ok that it's 2010 census data
*Feel free to use other datasets if you find the need. For example, is there a way to clean up "Unspecified" Boroughs?

-- 


