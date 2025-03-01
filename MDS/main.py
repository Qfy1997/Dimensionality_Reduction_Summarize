import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt


def eucliDist(A,B):
    return np.sqrt(sum(np.power((A-B),2)))

def get_distance_matrix(data):
	expand_ = data[:, np.newaxis, :]
	repeat1 = np.repeat(expand_, data.shape[0], axis=1)
	repeat2 = np.swapaxes(repeat1, 0, 1)
	# print(repeat1)
	# print(repeat2)
	D = np.linalg.norm(repeat1 - repeat2, ord=2, axis=-1, keepdims=True).squeeze(-1)
	return D

def get_matrix_B(D):
	assert D.shape[0] == D.shape[1]
	DD = np.square(D)
	sum_ = np.sum(DD, axis=1) / D.shape[0]
	Di = np.repeat(sum_[:, np.newaxis], D.shape[0], axis=1)
	Dj = np.repeat(sum_[np.newaxis, :], D.shape[0], axis=0)
	Dij = np.sum(DD) / ((D.shape[0])**2) * np.ones([D.shape[0], D.shape[0]])
	B = (Di + Dj - DD- Dij) / 2
	return B

def MDS(data, D,n=2):
	# D = get_distance_matrix(data)
	B = get_matrix_B(D)
	B_value, B_vector = np.linalg.eigh(B)
	Be_sort = np.argsort(-B_value)
	B_value = B_value[Be_sort]               # 降序排列的特征值
	B_vector = B_vector[:,Be_sort]           # 降序排列的特征值对应的特征向量
	Bez = np.diag(B_value[0:n])
	Bvz = B_vector[:, 0:n]
	Z = np.dot(np.sqrt(Bez), Bvz.T).T
	return Z

if __name__=='__main__':
	iris = load_iris()
	x = iris.data
	y = iris.target
	d_m = np.zeros((150,150))
	for i in range(len(x)):
		for j in range(len(x)):
			if i==j:
				d_m[i][j]=0
			else:
				d_m[i][j]=eucliDist(x[i],x[j])
	print(d_m)
	
	B=get_matrix_B(d_m)
	Z=MDS(B,d_m)
	print(Z)
	# print(a_arr)
	# Dis_matrix = get_distance_matrix(a_arr)
	# print(Dis_matrix)
	plt.scatter(Z[:, 0], Z[:, 1], c=y)
	plt.title("MDS example")
	plt.xlabel("MDS1")
	plt.ylabel("MDS2")
	plt.show()