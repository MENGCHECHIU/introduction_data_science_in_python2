# Load the energy data from the file assets/Energy Indicators.xls, which is a list of 
# indicators of energy supply and renewable electricity production from the United Nations 
# for the year 2013, and should be put into a DataFrame with the variable name of Energy.

# Keep in mind that this is an Excel file, and not a comma separated values file. Also, 
# make sure to exclude the footer and header information from the datafile. The first two 
# columns are unneccessary, so you should get rid of them, and you should change the column 
# labels so that the columns are:

# ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable]

# Convert Energy Supply to gigajoules (Note: there are 1,000,000 gigajoules in a petajoule).
# For all countries which have missing data (e.g. data with "...") make sure this is
# reflected as np.NaN values.

# Rename the following list of countries (for use in later questions):

# "Republic of Korea": "South Korea",
# "United States of America": "United States",
# "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
# "China, Hong Kong Special Administrative Region": "Hong Kong"

# There are also several countries with numbers and/or parenthesis in their name. Be sure 
# to remove these, e.g. 'Bolivia (Plurinational State of)' should be 'Bolivia'. 
# 'Switzerland17' should be 'Switzerland'.

# Next, load the GDP data from the file assets/world_bank.csv, which is a csv containing 
# countries' GDP from 1960 to 2015 from World Bank. Call this DataFrame GDP.

# Make sure to skip the header, and rename the following list of countries:

# "Korea, Rep.": "South Korea", 
# "Iran, Islamic Rep.": "Iran",
# "Hong Kong SAR, China": "Hong Kong"

# Finally, load the Sciamgo Journal and Country Rank data for Energy Engineering and Power 
# Technology from the file assets/scimagojr-3.xlsx, which ranks countries based on their 
# journal contributions in the aforementioned area. Call this DataFrame ScimEn.

# Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the 
# intersection of country names). Use only the last 10 years (2006-2015) of GDP data and 
# only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15).

# The index of this DataFrame should be the name of the country, and the columns should be 
# ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per 
# document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006'
# , '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015'].

# This function should return a DataFrame with 20 columns and 15 entries, and the rows of 
# the DataFrame should be sorted by "Rank".

def answer_one():
    import pandas as pd
    Energy = pd.read_excel('assets/Energy Indicators.xls',header = None,skiprows=18,skipfooter= 38,usecols=[2,3,4,5],names=['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'])
    Energy["Energy Supply"]=Energy["Energy Supply"]*1000000
    Energy['Country'] = Energy['Country'].str.replace(r" \(.*\)","")
    Energy['Country'] = Energy['Country'].str.replace(r"\d*","")
    Energy["Country"]=Energy["Country"].replace({"Republic of Korea": "South Korea","United States of America": "United States","United Kingdom of Great Britain and Northern Ireland": "United Kingdom","China, Hong Kong Special Administrative Region": "Hong Kong"})
    GDP=pd.read_csv("assets/world_bank.csv",skiprows=4)
    GDP["Country Name"]=GDP["Country Name"].replace({"Korea, Rep.": "South Korea","Iran, Islamic Rep.": "Iran","Hong Kong SAR, China": "Hong Kong"})
    ScimEn=pd.read_excel("assets/scimagojr-3.xlsx")
    criteria1=ScimEn["Rank"]<=15
    ScimEn=ScimEn[criteria1]
    merge1=pd.merge(ScimEn,Energy,how="inner",on="Country")
    GDP.rename(columns = {"Country Name":"Country"},inplace=True)
    GDP=GDP[["Country","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015"]]
    merge2 = pd.merge(merge1,GDP,how="inner",on="Country").set_index("Country")
    return(merge2)
# YOUR CODE HERE
#     raise NotImplementedError()
answer_one()