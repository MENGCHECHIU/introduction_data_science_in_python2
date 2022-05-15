# Convert the Population Estimate series to a string with thousands separator 
# (using commas). Use all significant digits (do not round the results).

# e.g. 12345678.90 -> 12,345,678.90

# This function should return a series PopEst whose index is the country name and whose 
# values are the population estimate string

def answer_thirteen():
    df=answer_one()
    df['Energy Supply']=df['Energy Supply'].apply(pd.to_numeric)
    df['Energy Supply per Capita']=df['Energy Supply per Capita'].apply(pd.to_numeric)
    df['PopEst'] = df['Energy Supply'] / df['Energy Supply per Capita']
    return df['PopEst'].apply('{:,}'.format)
    # YOUR CODE HERE
#     raise NotImplementedError()
answer_thirteen()