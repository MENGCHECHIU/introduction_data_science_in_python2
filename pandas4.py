# By how much had the GDP changed over the 10 year span for the country with the 6th largest
#  average GDP?

# This function should return a single number.

def answer_four():
    df=answer_one()
    df["avgGDP"]=df[["2006","2007","2008","2009","2010","2010","2011","2012","2013","2014","2015"]].mean(axis=1)
    df=df.sort_values(["avgGDP"],ascending=False)
    return df.iloc[5]["2015"]-df.iloc[5]["2006"]
    # YOUR CODE HERE
#     raise NotImplementedError()
answer_four()