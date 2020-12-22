# Importing the libraries
import pandas as pd
import pickle

dataset = pd.read_csv('hiring.csv')

X = dataset.iloc[:, :3]
y = dataset.iloc[:, -1]

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X, y)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# 第一步建模
# When run model.py, your model is now trained and your model gets saved in 
# the directory where your project files are stored in your local machine.
# Now that the model is ready and saved. It’s time we start building a flask model.