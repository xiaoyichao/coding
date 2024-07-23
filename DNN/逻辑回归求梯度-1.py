import numpy as np

def sigmoid(z):
    """
    计算 sigmoid 函数
    """
    return 1 / (1 + np.exp(-z))

def compute_cost(X, y, theta):
    """
    计算逻辑回归的代价函数
    """
    m = len(y)
    h = sigmoid(X @ theta)
    cost = (-1/m) * np.sum(y * np.log(h) + (1-y) * np.log(1-h))
    return cost

def compute_gradient(X, y, theta):
    """
    计算逻辑回归的梯度
    """
    m = len(y)
    h = sigmoid(X @ theta)
    gradient = (1/m) * X.T @ (h - y)
    return gradient

def gradient_descent(X, y, theta, alpha, num_iters):
    """
    执行梯度下降算法
    """
    m = len(y)
    J_history = []

    for i in range(num_iters):
        theta = theta - alpha * compute_gradient(X, y, theta)
        J_history.append(compute_cost(X, y, theta))
    
    return theta, J_history

# 主函数
def logistic_regression(X, y, alpha=0.01, num_iters=1000):
    """
    执行逻辑回归
    """
    m, n = X.shape
    X = np.hstack((np.ones((m, 1)), X))  # 添加偏置项
    theta = np.zeros(n + 1)

    theta, J_history = gradient_descent(X, y, theta, alpha, num_iters)

    return theta, J_history


# 生成一些示例数据
np.random.seed(0)
X = np.random.randn(100, 2)
y = (X[:, 0] + X[:, 1] > 0).astype(int)

# 运行逻辑回归
theta, J_history = logistic_regression(X, y)

print("最终的参数 theta:", theta)
print("最终的代价:", J_history[-1])

# 可以绘制代价函数的变化
import matplotlib.pyplot as plt
plt.plot(J_history)
plt.xlabel('迭代次数')
plt.ylabel('代价')
plt.title('代价函数随迭代的变化')
plt.show()