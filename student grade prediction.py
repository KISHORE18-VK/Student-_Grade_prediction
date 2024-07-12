import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_csv("student-mat.csv")

# Select relevant columns
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]
predict = "G3"

# Split data into features and target
x = np.array(data.drop([predict], axis=1))
y = np.array(data[predict])

# Split data into training and test sets
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2)

# Train the linear regression model
linear_regression = LinearRegression()
linear_regression.fit(xtrain, ytrain)

# Evaluate the model
accuracy = linear_regression.score(xtest, ytest)
print("Model accuracy:", accuracy)

# Make predictions
predictions = linear_regression.predict(xtest)
for i in range(len(predictions)):
    print(predictions[i], xtest[i], ytest[i])
