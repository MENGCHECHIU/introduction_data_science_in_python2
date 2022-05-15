# Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as these new % 
# Renewable bins. How many countries are in each of these groups?

# This function should return a Series with a MultiIndex of Continent, then the bins for %
#  Renewable. Do not include groups with no countries.

def answer_twelve():
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

    df=answer_one()
    df['Continent'] = pd.Series(ContinentDict)
    df["% Renewable"]=pd.cut(df["% Renewable"],5)
    return (df.reset_index().groupby(["Continent","% Renewable"])["Continent"].agg("size"))
    # YOUR CODE HERE
#     raise NotImplementedError()
answer_twelve()