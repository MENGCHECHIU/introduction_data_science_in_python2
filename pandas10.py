# Create a new column with a 1 if the country's % Renewable value is at or above the median 
# for all countries in the top 15, and a 0 if the country's % Renewable value is below the 
# median.

# This function should return a series named HighRenew whose index is the country name 
# sorted in ascending order of rank.

def answer_ten():
    df=answer_one()
    criteria=df["% Renewable"].median()
    df["HighRenew"]=df["% Renewable"].apply(lambda x:0 if x<criteria else 1)
    return df["HighRenew"]
answer_ten()
    # YOUR CODE HERE    
#     raise NotImplementedError()