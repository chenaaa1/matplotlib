# 将随机漫步的所有点绘制出来
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:

    # 创建一个RandomWalk实例
    rw = RandomWalk()
    rw.fill_walk()
    # 将所有点绘制出来
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9),)    # 注意后面有个字母s,figsize指定图表的尺寸
    point_numbers = range(rw.num_points)

    # 将随机漫步的x和y值传递给scatter，并选择合适的点尺寸
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
               edgecolors='none', s=15)
    # edgecolors='none'是删除每个点周围的轮廓

    # 突出起点和终点
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)   # 绘制起点
    ax.scatter(rw.x_values[-1],rw.y_values[-1], c='red', edgecolor='none', s=100)
    # 绘制终点

    # 隐藏坐标轴(没看懂这代码）
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk?(y,n)")
    if keep_running == 'n':
        break
