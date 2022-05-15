# The previous question joined three datasets then reduced this to just the top 15 entries. 
# When you joined the datasets, but before you reduced this to the top 15 items, how many 
# entries did you lose?

# This function should return a single number.

def answer_two():
    import pandas as pd
    Energy = pd.read_excel('assets/Energy Indicators.xls',na_values=["..."],header = None,skiprows=18,skipfooter= 38,usecols=[2,3,4,5],names=['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'])
    Energy["Energy Supply"]=Energy["Energy Supply"]*1000000
    Energy['Country'] = Energy['Country'].str.replace(r" \(.*\)","")
    Energy['Country'] = Energy['Country'].str.replace(r"\d*","")
    Energy["Country"]=Energy["Country"].replace({"Republic of Korea": "South Korea","United States of America": "United States","United Kingdom of Great Britain and Northern Ireland": "United Kingdom","China, Hong Kong Special Administrative Region": "Hong Kong"})
    GDP=pd.read_csv("assets/world_bank.csv",skiprows=4)
    GDP["Country Name"]=GDP["Country Name"].replace({"Korea, Rep.": "South Korea","Iran, Islamic Rep.": "Iran","Hong Kong SAR, China": "Hong Kong"})
    ScimEn=pd.read_excel("assets/scimagojr-3.xlsx")
    inner1=pd.merge(ScimEn,Energy,how="inner",on="Country")

    GDP.rename(columns = {"Country Name":"Country"},inplace=True)
    GDP=GDP[["Country","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015"]]
    inner2 = pd.merge(inner1,GDP,how="inner",on="Country").set_index("Country")
    outer1 = pd.merge(ScimEn,Energy,how="outer",on="Country")
    outer2 = pd.merge(outer1,GDP,how="outer",on="Country").set_index("Country")

    return(len(outer2)-len(inner2))
# YOUR CODE HERE
#     raise NotImplementedError()
answer_two()