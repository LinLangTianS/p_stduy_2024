import numpy as np

# 设置随机种子以便复现
np.random.seed(0)

# 参数设置
p = 0.1  # 次品率
n1 = 10  # 初始样本大小
increment = 10  # 后续抽样增量
max_samples = 100  # 最大样本数
accept_limit = 1  # 可接受的次品数量
num_simulations = 1000  # 模拟次数
p_t = 0.15

# 统计接受和拒绝的次数
accept_count = 0
accept_samples = []
reject_count = 0
reject_samples = []

for _ in range(num_simulations):
    total_samples = n1  # 当前样本总数
    defective_count = 0  # 次品数量
    
    # 进行初始抽样
    initial_samples = np.random.binomial(total_samples, p_t)
    defective_count += initial_samples

    # 判断初始抽样结果
    if defective_count == 0:
        accept_count += 1
        accept_samples.append(total_samples)
    elif defective_count > accept_limit:
        reject_count += 1
        reject_samples.append(total_samples)
    else:
        # 进行后续抽样
        while defective_count <= accept_limit and total_samples < max_samples:
            # 增加样本
            additional_samples = increment
            new_defective = np.random.binomial(additional_samples, p_t)
            defective_count += new_defective
            total_samples += additional_samples
            
            if defective_count > accept_limit:
                reject_count += 1
                reject_samples.append(total_samples)
                break
            elif defective_count == 0:
                accept_count += 1
                accept_samples.append(total_samples)
                break
        else:
            # 如果达到最大样本数，判断结果
            if defective_count <= accept_limit:
                accept_count += 1
                accept_samples.append(total_samples)
            else:
                reject_count += 1
                reject_samples.append(total_samples)

# 输出结果
print(f"在{num_simulations}次模拟中：")
print(f"接受批次的次数: {accept_count}")
print(f"拒绝批次的次数: {reject_count}")
print(f"接受率: {accept_count / num_simulations:.2f}")
print(f"拒绝率: {reject_count / num_simulations:.2f}")
print(f"接受批次的平均样本数: {sum(accept_samples) / accept_count}")
print(f"拒绝批次的平均样本数: {sum(reject_samples) / reject_count}")
print(f"拒绝批次的平均样本数: {(sum(reject_samples)+sum(accept_samples)) / num_simulations}")