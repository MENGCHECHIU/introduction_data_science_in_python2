# What are the top 15 countries for average GDP over the last 10 years?

# This function should return a Series named avgGDP with 15 countries and their average GDP
#  sorted in descending order.

def answer_three():
    df=answer_one()
    avgGDP=df[["2006","2007","2008","2009","2010","2010","2011","2012","2013","2014","2015"]].mean(axis=1).sort_values(ascending=False)
    return avgGDP
    # YOUR CODE HERE
#     raise NotImplementedError()
answer_three()