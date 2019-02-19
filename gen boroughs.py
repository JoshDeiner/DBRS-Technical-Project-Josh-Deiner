# Manahttan check for totals
import pandas as pd
from sodapy import Socrata

newDictionary = {} # oveerall complaints, sets dictionary.
#
otherdict = {}
api = pd.read_json('https://data.cityofnewyork.us/resource/fhrw-4uyv.json', orient='columns')
client = Socrata("'https://data.cityofnewyork.us/resource/fhrw-4uyv.json", "LOQNQRhAyAV9gvAB7w7JFdIa8")
results = client.get("https://data.cityofnewyork.us/resource/fhrw-4uyv.json", limit=2000)
complaints = api['complaint_type']
for x in complaints:
    if x in newDictionary:
        newDictionary[x]+=1
    else:
        newDictionary[x] = 1

print(newDictionary)


for x in newDictionary:
    print(x, newDictionary[x])

    newA = 'https://data.cityofnewyork.us/resource/fhrw-4uyv.json'
apii = pd.read_json(newA, orient='columns')
apii["complaint_type"]

newDictionary = {} # oveerall complaints, sets dictionary
otherdict = {}
for x in apii["complaint_type"]:
    if x in newDictionary:
        newDictionary[x]+=1
    else:
        newDictionary[x] = 1


for x in newDictionary: # print all borrough complaints
    print(x)


Boroughcomplaints = ''
listboroughcomplaints = []
for x in newDictionary:
    listboroughcomplaints.insert(0,x)
#     print(x,otherdict[x])
# print(listboroughcomplaints)
# listboroughcomplaints.append(10)
iterator= 0
while iterator < 10:
    iterator +=1
    print(listboroughcomplaints[iterator])


#value of top ten complaint, not accounting for year for bronx
value = 0
for x in newDictionary:
#     print(newDictionary[x])
    value += newDictionary[x]
    print(value)


apii['incident_zip'] # run condition for where a a zip code is in the array of zip codes. need to b matching on year. need to be mar
