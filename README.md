# ETF Classification Project

# Overview
________
The aim of this project is to organize and analyze ETF data from ETFdb.com using regex and classification clustering.
The 2 methods will then be compared to analyze the accuracy and dependability of the data provided. 
ETFs are first organized into categories based on their characteristics. Then clustering is used to group ETFs based on numerical information. 
This includes things such as assets under management, YTD return, trading volume, price, and daily price change.


# Project Goals
_____________
The project is designed to:

* Organize ETFs into meaningful categories
* Identify ETFs that belong to multiple categories
* Detect similarities between different ETFs
* Use clustering to group ETFs based on numerical data provided by ETFdb.com
* Combine the classification and clustering results into one organized dataset
* Make it easier to compare ETFs and identify relationships between them


# Data
____
The relevant data which this project uses is as previously mentioned,
data that comes from ETFdb.com.

This data includes information such as:
* Ticker - ETF Ticker Symbol i.e. VOO 
* Name - ETF Name, i.e. Vanguard S&P 500 ETF
* Asset Class - Type of asset which the particular ETF invests in. i.e. Equity
* Region - Region which the company is in, for this specific showing of the project North America was
  exclusively selected, this can be changed just by selecting a different set of ETFs with the scraper. 
* AUM - Assets under management
* YTD Return - Year to date return
* Volume - Trading volume
* Price - Current price of the ETF
* Day Change - Daily price change of the ETF



# ETF Classification
__________________

The ETFs are manually organized into categories using regular expressions. They are organized into the current categories listed below:

* Technology
* Growth
* Value
* Bonds
* Treasury
* S&P 500
* Mid-Cap
* Small-Cap
* Dividend
* Total Market

It is important to note that an ETF can belong to more than one category. For example, QQQM may belong to both Growth and Technology.
This allows the project to preserve multiple classifications instead of forcing every ETF into only one category.
Allowing for more precise decision-making.


# Clustering
_____________

The project also uses clustering to group ETFs based on their numerical characteristics.
For example, the current clustering results place several large S&P 500 ETFs together like VOO, IVV, and SPY.

The cluster number itself does not represent a specific category. It is simply an identifier for the group created by the clustering algorithm.
Interpretation of these groups is up to the user.


# Combining the Data
__________________

The classification and clustering datasets are combined in comparison.py.
This makes it possible to analyze both the manually identified characteristics and the numerical similarities found through clustering.
This can improve decision making further by easing the comparison process for the user. 


# Technologies Used
_________________

The project currently uses Python and several Python libraries, including:
* Pandas - Reading and manipulating CSV data
* Regular Expressions - Searching ETF information and identifying categories
* SciKit-Learn - A machine learning clustering algorithm. In this project KMeans-clustering is used with a k value of 3.
  The number of clusters used can be expanded if thought to be necessary. 


# Future Improvements
___________________

Some possible improvements for the project include:
* Adding more ETFs to the dataset with the paid subscription of ETFdb.com or using a different website
* Add additional ETF categories in the regexClassifier
* Experiment with different clustering algorithms
* Create visualizations of the ETF clusters and comparisons
* Build a way to search and compare individual ETFs
