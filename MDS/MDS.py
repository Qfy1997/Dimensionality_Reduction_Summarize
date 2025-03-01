# 直接调用MDS的版本，每次运行的结果不一致，什么原因不清楚，manifold到底是什么意思，海贼王看多了啊？
import numpy as np
from sklearn.datasets import load_iris
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

if __name__=='__main__':
    iris = load_iris()
    x = iris.data
    y = iris.target
    X = MDS(n_components=2)
    X_transformed = X.fit_transform(x)
    print(X_transformed.shape)
    print(X_transformed)
    plt.scatter(X_transformed[:,0],X_transformed[:,1],c=y)
    plt.title("MDS example")
    plt.xlabel("MDS1")
    plt.ylabel("MDS2")
    plt.show()