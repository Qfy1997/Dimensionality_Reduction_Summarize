import numpy as np
from sklearn.cluster import KMeans
from scipy.linalg import svd
import math
import matplotlib.pyplot as plt


if __name__=='__main__':
    iris_mat=np.zeros((150,4))
    label2id={'setosa':0,'versicolor':1,'virginica':2}
    with open('../iris.data','r') as f:
        data = f.readlines()
    x1,x2,x3,x4,y=[],[],[],[],[]
    for i in range(1,len(data)):
        # print(data[i].strip().split(','))
        x1.append(data[i].strip().split(',')[0])
        x2.append(data[i].strip().split(',')[1])
        x3.append(data[i].strip().split(',')[2])
        x4.append(data[i].strip().split(',')[3])
        y.append(label2id[data[i].strip().split(',')[4]])
    for i in range(len(iris_mat)):
        iris_mat[i][0]=x1[i]
        iris_mat[i][1]=x2[i]
        iris_mat[i][2]=x3[i]
        iris_mat[i][3]=x4[i]
    # print(iris_mat)
    U, Sigma, VT = svd(iris_mat, full_matrices=False)
    k = 2
    U_k = U[:, :k]
    Sigma_k = np.diag(Sigma[:k])
    A_k = np.dot(U_k, Sigma_k)
    # print(Sigma_k)
    # visualize the results
    plt.scatter(A_k[:, 0], A_k[:, 1], c=y)
    # plt.scatter(sklpca_y[:, 0], sklpca_y[:, 1], c=y)
    plt.title("SVD with numpy")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.show()



