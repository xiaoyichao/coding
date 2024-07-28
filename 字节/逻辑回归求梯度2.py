import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def compute_cost_and_gradient(X, y, W, b):
    m = X.shape[0]  # 样本数量
    z = np.dot(X, W) + b  # 模型预测值
    h = sigmoid(z)  # 应用sigmoid函数
    
    # 计算损失函数
    epsilon = 1e-5  # 避免log(0)的情况
    cost = (-1 / m) * (np.dot(y.T, np.log(h + epsilon)) + np.dot((1 - y).T, np.log(1 - h + epsilon)))
    
    # 计算梯度
    dW = (1 / m) * np.dot(X.T, (h - y))
    db = (1 / m) * np.sum(h - y)
    
    return cost, dW, db

# 示例数据
X = np.array([[2, 3], [3, 4], [4, 5], [5, 6]])
y = np.array([0, 0, 1, 1])
W = np.array([0.5, -0.5])
b = 0.1

cost, dW, db = compute_cost_and_gradient(X, y, W, b)
print(f"Cost: {cost}")
print(f"Gradient dW: {dW}")
print(f"Gradient db: {db}")