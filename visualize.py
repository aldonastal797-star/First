import numpy as np
import matplotlib.pyplot as plt

# 1. 准备数据
# np.linspace(0, 10, 100) 意思是：在 0 到 10 之间，均匀地取 100 个点
# 这就像是在横坐标轴上打了 100 个刻度
x = np.linspace(0, 10, 100)

# 2. 计算对应的纵坐标
# 计算这 100 个点的正弦值 (sin) 和 余弦值 (cos)
y1 = np.sin(x)
y2 = np.cos(x)

# 3. 开始画图
# 设置画布大小
plt.figure(figsize=(10, 6))

# 画第一条线 (正弦)，颜色是蓝色，标签叫 'Sin'
plt.plot(x, y1, label='Sin Wave', color='blue', linewidth=2)

# 画第二条线 (余弦)，颜色是红色，虚线，标签叫 'Cos'
plt.plot(x, y2, label='Cos Wave', color='red', linestyle='--', linewidth=2)

# 4. 装饰一下图表 (让它看起来专业)
plt.title("My First AI Plot: Sin & Cos", fontsize=16) # 标题
plt.xlabel("Time (s)", fontsize=12)  # 横坐标名字
plt.ylabel("Value", fontsize=12)     # 纵坐标名字
plt.legend()  # 显示图例 (就是那个告诉你是哪条线的框框)
plt.grid(True) # 显示网格线 (方便读数)

# 5. 展示图片
print("正在生成图表，请看弹出的窗口...")
plt.show()