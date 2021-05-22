import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei'] # 显示中文标签,rcParams是变量
plt.rcParams['axes.unicode_minus'] = False   # 这两行需要手动设置

input_values = [1, 2, 3, 4, 5]  # plot()默认第一个输入值是0，这里重新提供了提供输入值
squares = [1, 4, 9, 16, 25]  # 平方序数列
# 变量fig表示整张图片，变量ax表示图片中的各个图表,这两个看起来是自己定义的变量
# 函数subplots()可在一张图片绘制一个或多个图表
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)  # linewidth决定plot（）绘制的线条粗细

#  设置图表标题并给坐标轴加上标签
# fontsize主要是指定图表中字体大小
ax.set_title("平方数", fontsize=24)  # 方法set_title给图标选定标题
# set_xlabel，set_ylabel让你为每条轴设置标题
ax.set_xlabel("值", fontsize=14)  # fontsize是字体大小
ax.set_ylabel("值的平方", fontsize=14)

# 设置刻度标记的大小
# tick_parms设置刻度的样式，axis='both'影响x和y轴上的刻度
# lablesize=14将刻度标记的字号设置为14
ax.tick_params(axis='both', labelsize=14)   # axis后面跟x，y或both
# ax.plot(squares)    # 调用方法plot

plt.show()  # 打开matplotlib查看器并显示绘制的图