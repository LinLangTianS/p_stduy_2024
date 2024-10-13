import random

num_trial = 100000
exchange_win = 0
unexchange_win = 0
for k in range(num_trial):

    # 1. 随机将车子放在3个门后面，分别记为门1,门2,门3
    car = random.randint(1, 3)
    # print(car)

    # 2. 随机打开其中任何一扇门
    open1 = random.randint(1, 3)

    # 3. 主持打开其中一扇门
    # 如果open1打开的是有车的门，则主持人在剩下两扇门中任选一扇打开
    # 如果open1打开的是无车的门，则主持人必须打开另一扇无车的门
    while True:
        open2 = random.randint(1, 3)
        if open2 != open1 and open2 != car:
            break

    # 4.1 总是切换选择最后那扇没有打开的门。如果该门后有车的话则计数1次
    final = set([1, 2, 3]) - set([open1, open2])  # 用集合差运算求最后那扇门作为最终选择
    exchange_win += (car in final)

    # 4.2 直接根据第一次选择与有车的门是否一致进行判决
    if open1 == car:
        unexchange_win += 1

print('The win prob of exchanging the door is {0}'.format(exchange_win / num_trial))
print('The win prob of unexchanging the door is {0}'.format(unexchange_win / num_trial))

