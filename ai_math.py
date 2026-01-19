import numpy as np

# 1. 创建两个矩阵 (数据块)
# 想象这是 AI 里的两层神经网络参数
matrix_a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

matrix_b = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])

print("--- 矩阵 A (形状: 2行3列) ---")
print(matrix_a)

print("\n--- 矩阵 B (形状: 3行2列) ---")
print(matrix_b)

# 2. 矩阵乘法 (这是 AI 计算的核心！)
# 如果不用 numpy，这就需要写 3 层复杂的循环
# 用了 numpy，一行代码搞定，速度快几十倍
print("\n--- 计算结果 (A 乘以 B) ---")
result = np.dot(matrix_a, matrix_b)
print(result)

# 3. 统计一下数据
print(f"\n计算结果中的最大值是: {np.max(result)}")