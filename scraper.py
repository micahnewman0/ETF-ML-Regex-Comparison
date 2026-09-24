#Import necesarry packages
#BeautifulSoup allows for easy access to source HTML
from bs4 import BeautifulSoup
#Pandas allows for CSV interactability
import pandas as pd
import requests 

all_etfs =[]
temp_etf =[]
new_etf_list=[]
page_num = 1

#Pull url requests from correct url
## Note that the scraper should only pull the first 25 ETFs
### Also note that this is scalable with a paid membership
### If the membership is made you can access far more data
### Alternatives can be used to pull more free data yet they are not as scalable
b_url = "https://etfdb.com/etfs/country/us/#etfs&sort_name=assets_under_management&sort_order=desc"

# If using with a membership with ETFdb simply change 
# page_num to the desired page number count :)
while page_num <2:
    #Identify and pull correct page based on f-string
    url = f"{b_url}&page={page_num}"

    print(url)  
    #Pull request
    page = requests.get(url)

    #Parses through info in html format
    soup = BeautifulSoup(page.text, 'html.parser')
    
    # print(soup.prettify())

    #Find all row elements in url
    rows = soup.find_all("tr")

    #For each row find all data in table 
    for row in rows:
        columns = row.find_all("td")

        #Columns instead of rows
        if columns:
                data = [
                    column.get_text(" ", strip=True)
                    for column in columns
                ]
                #Append ETF data
                all_etfs.append(data)

    for etf in all_etfs[:25]:
        #clear temp_etf
        temp_etf=[]
        #extend only relevant elements of etf
        temp_etf.extend(etf[:9])
        #add temp to actual list
        new_etf_list.append(temp_etf)

    #increment page and clear all_etfs
    all_etfs = []
    page_num+=1
    print("I have updated the page number to: " + str(page_num) + "!")

#Output data
print(new_etf_list)

#Create ETF DataFrame
page_data = pd.DataFrame(new_etf_list)

#Save the DataFrame to a CSV file
page_data.to_csv('ETF_Output.csv', index=False)