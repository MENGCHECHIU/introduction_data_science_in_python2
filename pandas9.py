# Create a column that estimates the number of citable documents per person. What is the 
# correlation between the number of citable documents per capita and the energy supply per
#  capita? Use the .corr() method, (Pearson's correlation).

# This function should return a single number.

# (Optional: Use the built-in function plot9() to visualize the relationship between Energy 
# Supply per Capita vs. Citable docs per Capita)

def answer_nine():
    # YOUR CODE HERE
    # raise NotImplementedError()
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    return Top15['Citable docs per Capita'].corr(Top15['Energy Supply per Capita'])
answer_nine()

def plot9():
    import matplotlib as plt
    %matplotlib inline
    
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])