import numpy as np

np.random.seed(3)
p = 0.15  # 次品率
N = 30  # 初始样本大小
c = 3  # 可接受的次品数量
K = 10000  # 模拟次数
k_acc = 0
K_rej = 0
for i in range(K):
    # 进行抽样
    n = np.random.binomial(N, p)
    # 判断抽样结果
    if n < 4 :
        k_acc += 1
    else:
        K_rej += 1
# 输出结果
print(f"在{K}次模拟中：")
print(f"接受批次的次数: {k_acc}")
print(f"拒绝批次的次数: {K_rej}")
print(f"接受率: {k_acc / K}")
print(f"拒绝率: {K_rej / K}")