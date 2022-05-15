# Use the following dictionary to group the Countries by Continent, then create a DataFrame 
# that displays the sample size (the number of countries in each continent bin), and the
#  sum, mean, and std deviation for the estimated population of each country.

# ContinentDict  = {'China':'Asia', 
#                   'United States':'North America', 
#                   'Japan':'Asia', 
#                   'United Kingdom':'Europe', 
#                   'Russian Federation':'Europe', 
#                   'Canada':'North America', 
#                   'Germany':'Europe', 
#                   'India':'Asia',
#                   'France':'Europe', 
#                   'South Korea':'Asia', 
#                   'Italy':'Europe', 
#                   'Spain':'Europe', 
#                   'Iran':'Asia',
#                   'Australia':'Australia', 
#                   'Brazil':'South America'}
# This function should return a DataFrame with index named Continent ['Asia', 'Australia', 
# 'Europe', 'North America', 'South America'] and columns ['size', 'sum', 'mean', 'std']

import numpy as np
def answer_eleven():
    # YOUR CODE HERE
    # raise NotImplementedError()
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}

    Top15 = answer_one()
    Top15['Energy Supply']=Top15['Energy Supply'].apply(pd.to_numeric)
    Top15['Energy Supply per Capita']=Top15['Energy Supply per Capita'].apply(pd.to_numeric)
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Continent'] = pd.Series(ContinentDict)
    return Top15.groupby('Continent')['PopEst'].agg([np.size,np.sum, np.mean, np.std])
answer_eleven()