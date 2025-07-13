#Confusion Matrix

from sklearn.datasets import load_iris
data = load_iris()
X = data.data
Y = data.target

print(X.shape)
print(Y[:10])