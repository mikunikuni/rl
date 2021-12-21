import numpy as np
import pandas as pd
import time


def value(K):
    # 计算每个赌博机输出结果（一定期望的高斯分布）
    value_table = np.array([[-0.1, 0.7],
                            [0.5, 0.9],
                            [0.6, 1],
                            [0.1, 2],
                            [-0.3, 0.7]])
    v = np.random.normal(
        loc=value_table[K][0], scale=value_table[K][1], size=None)
    return v

def update(K):
    # 更新选择策略Q表、选择次数表和当前获得的总奖励
    global reward
    v = value(K)
    Q[K] = (Q[K] * count[K] + v) / (count[K] + 1)
    count[K] = count[K] + 1
    reward += v


def rl():
    # 主程序，通过多次尝试学习赌博机来找到最优策略
    for i in range(Try):
        logical = np.random.rand() > eposion and np.any(Q == 0)     # 选择逻辑：当还有未知赌博机时，大概率探索，否则贪心
        if logical:
            select = np.random.randint(N_arm, size=None)
        else:
            select = np.argmax(Q)
        update(select)
        print("select = %d             " % select, end="")
        print("iter = %d               " % i, end="")
        print("Q_table = ", Q)
        time.sleep(0.1)

    print(reward)


N_arm = 5               # 赌博机个数
Q = np.zeros(5)         # Q价值表
count = np.zeros(5)     # 选择次数表
Try = 100               # 尝试次数
eposion = 0.1           # 贪心概率
reward = 0              # 总价值奖励
if __name__ == "__main__":
    rl()
