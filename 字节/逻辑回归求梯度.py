import numpy as np

# 定义 sigmoid 函数
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# 定义逻辑回归模型类
class LogisticRegression:
    def __init__(self, learning_rate=0.01, num_iterations=1000):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.costs = []  # 用于存储每次迭代的成本值
    
    def fit(self, X, y):
        # 初始化参数
        self.m, self.n = X.shape
        self.w = np.zeros(self.n)
        self.b = 0
        
        # 梯度下降优化
        for i in range(self.num_iterations):
            self._gradient_descent(X, y)
            if i % 100 == 0 or i == self.num_iterations - 1:  # 每100次迭代打印一次成本值
                cost = self._compute_cost(X, y)
                self.costs.append(cost)
                print(f"Iteration {i}: Cost {cost}")
    
    def _gradient_descent(self, X, y):
        # 正向传播
        Z = np.dot(X, self.w) + self.b
        A = sigmoid(Z)
        
        # 反向传播（计算梯度）
        dw = (1 / self.m) * np.dot(X.T, (A - y))
        db = (1 / self.m) * np.sum(A - y)
        
        # 参数更新
        self.w -= self.learning_rate * dw
        self.b -= self.learning_rate * db
    
    def _compute_cost(self, X, y):
        Z = np.dot(X, self.w) + self.b
        A = sigmoid(Z)
        cost = - (1 / self.m) * np.sum(y * np.log(A) + (1 - y) * np.log(1 - A))
        return cost

    def predict(self, X):
        Z = np.dot(X, self.w) + self.b
        A = sigmoid(Z)
        return A >= 0.5

# 测试逻辑回归模型
if __name__ == "__main__":
    # 生成测试数据
    np.random.seed(1)
    X_train = np.random.randn(100, 2)
    y_train = (np.dot(X_train, [2, -1]) > 0).astype(int)
    
    # 创建逻辑回归模型
    model = LogisticRegression(learning_rate=0.1, num_iterations=1000)
    model.fit(X_train, y_train)
    
    # 预测
    predictions = model.predict(X_train)
    accuracy = np.mean(predictions == y_train)
    print(f"训练准确率: {accuracy * 100:.2f}%")