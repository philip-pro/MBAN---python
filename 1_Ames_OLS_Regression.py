    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 17:33:50 2018

@author: Philip Prohaska

Working Directory:
/Users/philip.prohaska/Desktop/

Purpose:
    To analyze the Ames, Iowa housing dataset and predict home prices.
"""

# Loading Libraries
import pandas as pd
import statsmodels.formula.api as smf # regression modeling
import seaborn as sns
import matplotlib.pyplot as plt


file = 'Ames_explored.xlsx'

housing = pd.read_excel(file)



"""
Prof. Chase:
    Building OLS linear regression models is not hard in Python.
    statsmodels.formula.api allows us to code a model similar to how we
    would code in R.
"""

###############################################################################
# Univariate Regression Analysis
###############################################################################

# Building a Regression Base
lm_price_qual = smf.ols(formula = """SalePrice ~ housing['Overall Qual']""",
                         data = housing)



# Fitting Results
results = lm_price_qual.fit()


# Printing Summary Statistics
print(results.summary())



print(f"""
Parameters:
{results.params.round(2)}

Summary Statistics:
R-Squared:          {results.rsquared.round(3)}
Adjusted R-Squared: {results.rsquared_adj.round(3)}
""")



print(f"""
Prof. Chase:
    Although the adjusted R-Squared of {results.rsquared_adj.round(3)} is
    less than optimal, this simple model has a few advantages:
        * It is easy to interpret.
        * It can act as a base when comparing more complex models.
    
    The low metric value also indicates that our model is not overfit.
""")



########################
# Working with Categorical Variables
########################

# One-Hot Encoding Qualitative Variables
street_dummies = pd.get_dummies(list(housing['Street']), drop_first = True)
lot_config_dummies = pd.get_dummies(list(housing['Lot Config']), drop_first = True)
neighborhod_dummies = pd.get_dummies(list(housing['Neighborhood']), drop_first = True)



# Concatenating One-Hot Encoded Values with the Larger DataFrame
housing_2 = pd.concat(
        [housing.loc[:,:],
         street_dummies, lot_config_dummies, neighborhod_dummies],
         axis = 1)

# See Footnote 0 for a more detailed explanation of the above code.


########################
# Full Model
########################

lm_full = smf.ols(formula = """SalePrice ~ housing_2['Lot Area'] +
                                           housing_2['Street'] +
                                           housing_2['Lot Config'] +
                                           housing_2['Neighborhood'] +
                                           housing_2['Overall Qual'] +
                                           housing_2['Overall Cond'] +
                                           housing_2['Mas Vnr Area'] +
                                           housing_2['Total Bsmt SF'] +
                                           housing_2['1st Flr SF'] +
                                           housing_2['2nd Flr SF'] +
                                           housing_2['Gr Liv Area'] +
                                           housing_2['Full Bath'] +
                                           housing_2['Half Bath'] +
                                           housing_2['Kitchen AbvGr'] +
                                           housing_2['TotRms AbvGrd'] +
                                           housing_2['Fireplaces'] +
                                           housing_2['Garage Cars'] +
                                           housing_2['Garage Area'] +
                                           housing_2['Porch Area'] +
                                           housing_2['Pool Area'] +
                                           housing_2['m_Mas Vnr Area'] +
                                           housing_2['m_Total Bsmt SF'] +
                                           housing_2['m_Garage Cars'] +
                                           housing_2['m_Garage Area'] +
                                           housing_2['out_Lot_Area'] +
                                           housing_2['out_Overall_Qual'] +
                                           housing_2['out_Overall_Cond'] +
                                           housing_2['out_Mas_Vnr_Area'] +
                                           housing_2['out_Total_Bsmt_SF'] +
                                           housing_2['out_ff_SF'] +
                                           housing_2['out_sf_SF'] +
                                           housing_2['out_Full_Bath'] +
                                           housing_2['out_Half_Bath'] +
                                           housing_2['out_Kitchen_AbvGr'] +
                                           housing_2['out_TotRms_AbvGrd'] +
                                           housing_2['out_Fireplaces'] +
                                           housing_2['out_Garage_Cars'] +
                                           housing_2['out_Garage_Area'] +
                                           housing_2['out_Porch_Area'] +
                                           housing_2['out_Pool_Area'] +
                                           housing_2['out_Gr_Liv_Area'] -1
                                           """,
                         data = housing_2)


# Fitting Results
results = lm_full.fit()



# Printing Summary Statistics
print(results.summary())



print(f"""
Summary Statistics:
R-Squared:          {results.rsquared.round(3)}
Adjusted R-Squared: {results.rsquared_adj.round(3)}
""")
    
    
"""
Prof. Chase:
    This is much better, but some of our variables have unacceptable p-values.
    Let's consider removing these variables.
"""


    
########################
# Significant Model
########################

lm_significant = smf.ols(formula = """SalePrice ~ housing_2['CulDSac'] +
                                                  housing_2['Inside'] +
                                                  housing_2['Blueste'] +
                                                  housing_2['BrDale'] +
                                                  housing_2['BrkSide'] +
                                                  housing_2['Edwards'] +
                                                  housing_2['GrnHill'] +
                                                  housing_2['IDOTRR'] +
                                                  housing_2['MeadowV'] +
                                                  housing_2['NAmes'] +
                                                  housing_2['NPkVill'] +
                                                  housing_2['NWAmes'] +
                                                  housing_2['NoRidge'] +
                                                  housing_2['NridgHt'] +
                                                  housing_2['OldTown'] +
                                                  housing_2['SWISU'] +
                                                  housing_2['Sawyer'] +
                                                  housing_2['Somerst'] +
                                                  housing_2['StoneBr'] +
                                                  housing_2['Timber'] +
                                                  housing_2['Overall Qual'] +
                                                  housing_2['Overall Cond'] +
                                                  housing_2['Mas Vnr Area'] +
                                                  housing_2['Total Bsmt SF'] +
                                                  housing_2['2nd Flr SF'] +
                                                  housing_2['Half Bath'] +
                                                  housing_2['Fireplaces'] +
                                                  housing_2['Garage Cars'] +
                                                  housing_2['Garage Area'] +
                                                  housing_2['Porch Area'] +
                                                  housing_2['Pool Area'] +
                                                  housing_2['out_Lot_Area'] +
                                                  housing_2['out_ff_SF'] +
                                                  housing_2['out_sf_SF'] +
                                                  housing_2['out_Full_Bath'] +
                                                  housing_2['out_Half_Bath'] +
                                                  housing_2['out_Kitchen_AbvGr'] +
                                                  housing_2['out_Garage_Area'] +
                                                  housing_2['out_Porch_Area'] +
                                                  housing_2['out_Pool_Area'] -1
                                                  """,
                                                  data = housing_2)


# Fitting Results
results = lm_significant.fit()



# Printing Summary Statistics
print(results.summary())



print(f"""
Summary Statistics:
R-Squared:          {results.rsquared.round(3)}
Adjusted R-Squared: {results.rsquared_adj.round(3)}
""")
    
    
"""
Prof. Chase:
    Amazing! Our Adjusted R_Squared is very high!
"""


"""
Prof. Chase:
    Our model predicts very well on data that it used to 'teach' itself.
    However, how would this model perform on data it's never seen before?
    In other words, does this model generalize well? Can we trust its
    predictions on new data?
"""



# Checking predicted sale prices v. actual sale prices
predict = results.predict()
y_hat   = pd.DataFrame(predict).round(2)
resids  = results.resid.round(2)



# Plotting residuals
residual_analysis = pd.concat(
        [housing.loc[:,'SalePrice'],
         y_hat,
         results.resid.round(2)],
         axis = 1)


residual_analysis.to_excel('Ames Residuals.xlsx')


sns.residplot(x = predict,
              y = housing.loc[:,'SalePrice'])


plt.show()



# We can find more functions available using the dir() command.
dir(results)



# Saving as a new dataset for future use.
housing_2.to_excel('Housing_Dummies.xlsx')



"""
###############################################################################
# Footnotes
###############################################################################
        
Footnote 0: Concatinating with pd.concat()

\"""
Prof. Chase:
    concat is short for concatenation. The purpose of this code is to
    concatenate the dummy variables with the original dataset. In other words,
    we are adding them as additional columns. When axis=1, it means the pandas
    operation is performed column-wise.
\"""


housing_2 = pd.concat(      # calling pd.concat
[housing.loc[:,:],          # on all columns and all rows of the original DataFrame 
street_dummies,             # and the these dummy variable columns
lot_config_dummies,
neighborhod_dummies],       # Notice that all columns (including the originals) are in a list as one argument
axis = 1)                   # Setting axis = 1 so that pandas operates column-wise 



*******************************************************************************
"""
