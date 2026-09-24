#Import necesarry packages
#Pandas allows for CSV interactability
import pandas as pd
#Regular Expressions import, necessary for searching
#information within the DataFrame
import re

#Load the two files for comparison
regex_File = "Regex_Classifications.csv"
regex_Data = pd.read_csv(regex_File)

cluster_File = "ETF_KMeans_Clustering.csv"
cluster_Data = pd.read_csv(cluster_File)

only_Clusters = []
only_Category1 = []
only_Category2 = []
compared_Data = []

# compared_Data.columns = ["Cluster", "Technology", "Growth", "Value", "Bonds", "S&P 500", 
#                         "Dividend", "Mid-Cap", "Treasury", "Small-Cap", "Broad Market"]

for cluster in cluster_Data["Cluster"]:
    only_Clusters.append(cluster)
for category in regex_Data["Category1"]:
    only_Category1.append(category)
for category in regex_Data["Category2"]:
    if category != None:
        only_Category2.append(category)

count = 0
for ticker in regex_Data["Ticker"]:
    new_point= []
    new_point.append(ticker)
    new_point.append(only_Clusters[count])
    new_point.append(only_Category1[count])
    if only_Category2 != None:
        new_point.append(only_Category2[count])
    tuple1 = tuple(new_point)
    compared_Data.append(tuple1)
    count+=1
print("")

#Use {} to make it a dictionary so .get(#) works
organized = {}

for data in compared_Data:
    if data[1] not in organized:
        organized[data[1]] = {}

    organized[data[1]][data[2]] = organized[data[1]].get(data[2], 0) + 1
    if str(data[3]) != "nan":
        organized[data[1]][data[3]] = organized[data[1]].get(data[3], 0) + 1

print(organized)