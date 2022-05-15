# Create a new column that is the ratio of Self-Citations to Total Citations. 
# What is the maximum value for this new column, and what country has the highest ratio?

# This function should return a tuple with the name of the country and the ratio.

def answer_seven():
    df=answer_one()
    df=df.assign(citation_ratio=df["Self-citations"]/df["Citations"]).sort_values(["citation_ratio"],ascending=False)
    return (df["citation_ratio"].index[0],df["citation_ratio"][0])
    # YOUR CODE HERE
#     raise NotImplementedError()
answer_seven()