#Cross Validation

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
import numpy as np
X,y = load_iris(return_X_y= True)
model = DecisionTreeClassifier()
scores = cross_val_score(model, X, y, cv = 5)
print(f"Scores: {scores}")
print(f"Average: {np.mean(scores)}")