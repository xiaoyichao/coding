import numpy as np

def sigmoid(z):
  """
  Sigmoid 函数
  """
  return 1.0 / (1.0 + np.exp(-z))

def model(X, W):
  """
  模型预测函数
  """
  return sigmoid(np.dot(X, W))

def cost(X, y, W):
  """
  损失函数
  """
  N = len(X)
  return -np.sum(y * np.log(model(X, W)) + (1 - y) * np.log(1 - model(X, W))) / N

# def gradient(X, y, W):
#   """
#   计算梯度
#   """
#   N = len(X)
#   return np.dot(X.T, (model(X, W) - y)) / N
def gradient(X, y, W):
  """
  计算梯度
  """
  N = len(X)
  y = y.reshape(X.shape[0], 1)  # Reshape y to match W's columns
  return np.dot(X.T, (model(X, W) - y)) / N

def descent(X, y, W, learning_rate, num_iters):
  """
  梯度下降算法
  """
  for i in range(num_iters):
    W -= learning_rate * gradient(X, y, W)

def accuracy(X, y, W):
  """
  计算精度
  """
  N = len(X)
  predictions = model(X, W)
  correct = np.sum(predictions == y)
  return correct / N

# 示例用法
X = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([0, 1, 1])
W = np.zeros((2, 1))

learning_rate = 0.1
num_iters = 1000

descent(X, y, W, learning_rate, num_iters)

print(accuracy(X, y, W))
