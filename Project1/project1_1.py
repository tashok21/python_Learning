import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


heart=pd.read_csv("heart1.csv")   #Read the data

#Correlation matrix
corr_mat=heart.corr().abs()
print("The Correlation matrix is:")
print(corr_mat)

# To sort correlation matrix
corr_unstack=corr_mat.unstack()
print("The sorted correlation matrix:", corr_unstack)
print(type(corr_unstack))
corr_unstack_copy = corr_unstack.copy()
corr_unstack_copy.sort_values(inplace=True, ascending=False)

#Covariance matrix 
cov_mat = heart.cov().abs()
cov_mat*= np.tri(*cov_mat.values.shape, k=-1).T #Printing the upper triangle
print("The Covariance matrix is:")
print(cov_mat)

#Sorting the covariance matrix
cov_unstack=cov_mat.unstack()
cov_unstack_copy = cov_unstack.copy()
cov_unstack_copy.sort_values(inplace=True,ascending = False)
print ("The Sorted covariance matrix:")
print(cov_unstack_copy)

#To plot the pairplot

sns.set(style='whitegrid', context='notebook')
sns.pairplot(heart,height=1)
plt.show()

