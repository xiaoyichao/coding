import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def compute_cost_and_gradient(X, y, W, b):
    m = X.shape[0]  # 样本数量
    z = np.dot(X, W) + b  # 模型预测值
    h = sigmoid(z)  # 应用sigmoid函数
    
    # 计算损失函数
    cost = - (1 / m) * np.sum(y * np.log(h) + (1 - y) * np.log(1 - h))
    
    # 计算梯度
    dW = (1 / m) * np.dot(X.T, (h - y))
    db = (1 / m) * np.sum(h - y)
    
    # 如果需要在函数外部应用学习率，可以在这里返回原始梯度，然后在外部应用
    # 但通常这不是函数的一部分
    
    return cost, dW, db

# 示例数据
X = np.array([[2, 3], [3, 4], [4, 5], [5, 6]])
y = np.array([0, 0, 1, 1])
W = np.array([0.5, -0.5])
b = 0.1
epsilon = 1e-9  # 一个非常小的数，用于clip函数中
l_r = 1e-5

cost, dW, db = compute_cost_and_gradient(X, y, W, b, l_r)  # 注意：这里l_r实际上在函数内部没有被使用
print(f"Cost: {cost}")
print(f"Gradient dW: {dW}")
print(f"Gradient db: {db}")

# 如果你需要在外部使用学习率更新参数：
W -= l_r * dW
b -= l_r * db