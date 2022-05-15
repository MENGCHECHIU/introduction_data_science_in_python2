What country has the maximum % Renewable and what is the percentage?

This function should return a tuple with the name of the country and the percentage.

def answer_six():
    df=answer_one()
    maxR=df["% Renewable"].sort_values(ascending=False)
    return (maxR.index[0],maxR.iloc[0])
    # YOUR CODE HERE
#     raise NotImplementedError()
answer_six()