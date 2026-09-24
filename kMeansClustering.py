#README too!
#Overall in our KMeans Clustering data we can see the
#difference in clusters
#
#Cluster 0 prioritizes high Year To Date returns
#Expressing interest in __________ overall
#
#Cluster 1 is everything between the other two with 
#a more diverse array of ETFs. This may indicate that a 
#change in the k value should be considered
#
#Cluster 2 seems to hold the majority of high
#priced ETFs with high volume and stable day change

#Import necesarry packages
#Pandas allows for CSV interactability
import pandas as pd
#SciKit-Learn allows for the KMeans clustering to take place
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

#Input file with 25 ETFs
file = "ETF_Output.csv"
data = pd.read_csv(file)
#Rename the columns of file to relevant topics
data.columns = ["Ticker", "Name", "AssetClass", "Region", "AUM", "YTDReturn", "Volume", "Price", "DayChange"]

#Focused on coloumns
#Relevant to KMeans Clustering decision
columns = ["AUM", "YTDReturn", "Volume", "Price", "DayChange"]
#For each column make the data readable
#This is necessary since SciKit-Learn requires floats
for column in columns:
    temp = data[column].astype(str)
    temp2 = temp.str.replace(r"[\$,%]", "", regex=True)
    data[column] = temp2.astype(float)

#Using a Standard Scaler with Mean of 0 and Standard Deviation of 1
X = StandardScaler().fit_transform(data[columns])

#Number of clusters set to 3
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
#Call the predictions for the Data
data["Cluster"] = kmeans.fit_predict(X)

# Output DataFrame based on KMeans Clustering data
print(data[["Ticker", "Cluster"] + columns].sort_values("Cluster").to_string())

# Save DataFrame to csv based on KMeans data
data[["Ticker", "Cluster"] + columns].sort_values("Cluster").to_csv("ETF_KMeans_Clustering.csv")