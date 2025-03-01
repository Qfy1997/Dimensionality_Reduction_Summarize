import numpy as np
from sklearn.datasets import load_iris
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def pca(X):
    # 求每一个样本的均值
    Mean = np.mean(X,axis=0)
    # 去中心化
    X = np.subtract(X,Mean)
    # Step 1: 计算协方差矩阵
    cov_matrix = np.dot(X.T,X)
    # Step 2: 获取特征值和特征向量
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
    # Step 3: 取前k个特征
    # print(eigenvalues) #特征
    # print(eigenvectors)#特征向量
    sum_lambda = np.sum(eigenvalues)
    f = np.divide(eigenvalues,sum_lambda)
    print(f)
    e1 = eigenvectors.T[0]
    e2 = eigenvectors.T[1]
    z1 = np.dot(X,e1)
    z2 = np.dot(X,e2)
    RES = np.array([z1,z2])
    return RES.T

def pca_with_svd(X,k):
    m = np.mean(X,1)
    m = np.array([m])
    X = X-m.T
    C = np.dot(X.T,X)
    [eigValue,V] = np.linalg.eig(C)
    eigValue = abs(np.array([eigValue]))
    sinValue = np.sqrt(eigValue)
    temp = np.zeros([np.size(sinValue,1),np.size(sinValue,1)])
    for i in range(0,np.size(sinValue,1)):
        temp[i,i] = sinValue[0,i]
    sinValue = temp
    V = V/np.linalg.norm(V,axis=0)
    U = np.dot(X,np.linalg.inv(np.dot(sinValue,V.T)))
    U = U.T
    index = np.argsort(-eigValue)
    eigValue.tolist()[0].reverse()
    temp = U.copy()
    for i in range(0,np.size(U,0)):
        U[i,:] = temp[index[0][i],:]
    transMat = U[0:k,:]
    return np.real(transMat).T


if __name__=="__main__":
    iris = load_iris()
    # print(type(iris))
    # generate random data
    x = iris.data #鸢尾花数据集整体数据
    y = iris.target #鸢尾花的种类数值标签
    # apply PCA
    # k = 2
    # Y = pca(x)
    Y = pca_with_svd(x,2)
    print(Y)
    print(Y.shape)
    # print("======")
    # sklpca= PCA(n_components=2)
    # sklpca.fit(x)
    # sklpca_y = sklpca.transform(x)
    # print(sklpca_y)
    # visualize the results
    plt.scatter(Y[:, 0], Y[:, 1], c=y)
    # plt.scatter(sklpca_y[:, 0], sklpca_y[:, 1], c=y)
    plt.title("PCA with numpy")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.show()