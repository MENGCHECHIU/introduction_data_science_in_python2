# Create a column that estimates the population using Energy Supply and Energy Supply per 
# capita. What is the third most populous country according to this estimate?

# This function should return the name of the country

def answer_eight():
    df=answer_one()
    df=df.assign(popular_country=df["Energy Supply"]/df["Energy Supply per Capita"]).sort_values(["popular_country"],ascending=False)
    return df.index[2]
    # YOUR CODE HERE
#     raise NotImplementedError()
answer_eight()