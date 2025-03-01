import numpy as np
from sklearn.datasets import load_iris
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from skbio.diversity import beta_diversity
from skbio.stats.ordination import pcoa


def eucliDist(A,B):
    return np.sqrt(sum(np.power((A-B),2)))
X = np.array([1,2,3,4])
Y = np.array([0,1,2,3])
print(eucliDist(X,Y))

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

if __name__=="__main__":
    iris = load_iris()
    # print(type(iris))
    # generate random data
    x = iris.data #鸢尾花数据集整体数据
    y = iris.target #鸢尾花的种类数值标签
    d_m = np.zeros((150,150))
    for i in range(len(x)):
        for j in range(len(x)):
            if i==j:
                d_m[i][j]=0
            else:
                d_m[i][j]=eucliDist(x[i],x[j])
    # print(d_m)
    # Y = pca(d_m)
    # distance_matrix = beta_diversity('braycurtis',x)
    # print(distance_matrix)
    # print(type(distance_matrix))
    # print(distance_matrix.data)
    # bc_data=distance_matrix.data
    sklpca= PCA(n_components=2)
    sklpca.fit(d_m)
    sklpca_y = sklpca.transform(d_m)
    # pcoa_results = pcoa(d_m)
    # visualize the results
    # plt.scatter(Y[:, 0], Y[:, 1], c=y)
    plt.scatter(sklpca_y[:, 0], sklpca_y[:, 1], c=y)
    # plt.scatter(pcoa_results.samples['PC1'],pcoa_results.samples['PC2'],c=y)
    # print(pcoa_results.samples['PC1'])
    # print(pcoa_results.samples['PC1'][0])
    # print(pcoa_results.samples['PC2'])
    # result = np.zeros((150,2))
    # i=0
    # for item in pcoa_results.samples['PC1']:
    #     result[i][0] = item
    #     i+=1
    # i=0
    # for item in pcoa_results.samples['PC2']:
    #     result[i][1] = item
    #     i+=1
    # print(result)
    plt.title("error example")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.show()