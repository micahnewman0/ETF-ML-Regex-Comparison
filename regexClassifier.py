#Import necesarry packages
#Pandas allows for CSV interactability
import pandas as pd
#Regular Expressions import, necessary for searching
#information within the DataFrame
import re

#Input file with 25 ETFs
file = "ETF_Output.csv"
data = pd.read_csv(file)
#Rename the columns of file to relevant topics
data.columns = ["Ticker", "Name", "AssetClass", "Region", "AUM", "YTDReturn", "Volume", "Price", "DayChange"]
print(data)

#Creation of common ETF categories
#______________________#
#Technology
#Growth
#Value
#Bonds
#S&P 500
#Dividend
#Mid-Cap
#Treasury
#Small-Cap
#Broad Market
#______________________#
str_data = data[["Ticker", "Name"]].to_string().split('\n')
classification_List = []
raw_Classification_List =[]
final_Classification_List =[]

#Technology classification
p_Technology = re.compile('[Tt]echnology|[Tt]ech|[Mm]achine|[Cc]omputer|[Gg]raphic|NASDAQ|nasdaq')
for etf in str_data:
    r_Technology = p_Technology.search(etf)
    if r_Technology:
        split = etf.split()
        ticker = split[1]
        new_point = ticker, "Technology"
        classification_List.append(new_point)

#Growth classification
p_Growth = re.compile('[Gg]row|[Rr]ise')
for etf in str_data:
    r_Growth = p_Growth.search(etf)
    if r_Growth:
        split2 = etf.split()
        ticker2 = split2[1]
        new_point2 = ticker2, "Growth"
        classification_List.append(new_point2)

#Value classification
p_Value = re.compile('[Vv]alue')
for etf in str_data:
    r_Value = p_Value.search(etf)
    if r_Value:
        split3 = etf.split()
        ticker3 = split3[1]
        new_point3 = ticker3, "Value"
        classification_List.append(new_point3)

#Bonds classification
p_Bonds = re.compile('[Bb]ond|[Ff]ixed( [Ii]ncome)?')
for etf in str_data:
    r_Bonds = p_Bonds.search(etf)
    if r_Bonds:
        split4 = etf.split()
        ticker4 = split4[1]
        new_point4 = ticker4, "Bonds"
        classification_List.append(new_point4)

#S&P classification (This accounts for anything that calculates
# the total stock market since top 500 make up majority. This can
# be changed to a different category if necessary)
p_SNP = re.compile('[Ss]&[Pp]( 500)?|[Tt]otal|[Aa]ll')
for etf in str_data:
    r_SNP = p_SNP.search(etf)
    if r_SNP:
        split5 = etf.split()
        ticker5 = split5[1]
        new_point5 = ticker5, "S&P 500"
        classification_List.append(new_point5)

#Dividend classification
p_Div = re.compile('[Dd]ividend|[Ii]ncome')
for etf in str_data:
    r_Div = p_Div.search(etf)
    if r_Div:
        split6 = etf.split()
        ticker6 = split6[1]
        new_point6 = ticker6, "Dividend"
        classification_List.append(new_point6)

#Mid-Cap classification
p_MC = re.compile('[Mm]id[- ]?[Cc]ap')
for etf in str_data:
    r_MC = p_MC.search(etf)
    if r_MC:
        split7 = etf.split()
        ticker7 = split7[1]
        new_point7 = ticker7, "Mid-Cap"
        classification_List.append(new_point7)

#Treasury classification
p_Treasury = re.compile('[Tt]reasur(y|ies)|[Tt]-[Bb]ill|[Tt]-[Nn]ote')
for etf in str_data:
    r_Treasury = p_Treasury.search(etf)
    if r_Treasury:
        split8 = etf.split()
        ticker8 = split8[1]
        new_point8 = ticker8, "Treasury"
        classification_List.append(new_point8)

#Small-Cap classification
p_SC = re.compile('[Ss]mall[- ]?[Cc]ap')
for etf in str_data:
    r_SC = p_SC.search(etf)
    if r_SC:
        split9 = etf.split()
        ticker9 = split9[1]
        new_point9 = ticker9, "Small-Cap"
        classification_List.append(new_point9)

#Broad Market classification
p_Broad = re.compile('[Bb]road|[Tt]otal [Mm]arket')
for etf in str_data:
    r_Broad = p_Broad.search(etf)
    if r_Broad:
        split10 = etf.split()
        ticker10 = split10[1]
        new_point10 = ticker10, "Broad Market"
        classification_List.append(new_point10)

#Hold the result of the output
result = []
#Go throught the list to find all duplicate Tickers and minimize the output
# to increase overall readability and efficiency
for c_Etf in classification_List:
    ticker = c_Etf[0]
    category = c_Etf[1:]

#Create an existing variable for if Ticker is represented
    existing = None
    for item in result:
        if item[0] == ticker:
            existing = item
            break

#Create the Ticker in result if not there
    if existing is None:
        #Create category placeholder
        new_categories = []
        for cat in category:
            if cat not in new_categories:
                #Append categories to Ticker
                new_categories.append(cat)
        #Append Ticker and Categories to result
        #Note that the categories can be added to
        result.append([ticker, new_categories])   
    #Add any other categories represented in dataa
    else:
        for cat in category:
            if cat not in existing[1]:
                existing[1].append(cat) 
#Add all lists in results to a tuple
#Append tuples to final_Classification_List for output
final_Classification_List = [tuple([item[0]] + item[1]) for item in result]

# Build DataFrame and pad rows so they're all equal length first
max_cats = max(len(row) - 1 for row in final_Classification_List)
rows = [[row[0]] + list(row[1:]) + [None] * (max_cats - len(row[1:])) for row in final_Classification_List]
columns = ["Ticker"] + [f"Category{i+1}" for i in range(max_cats)]

classified_data = pd.DataFrame(rows, columns=columns)
classified_data.to_csv("Regex_Classifications.csv", index=False)
print(classified_data)