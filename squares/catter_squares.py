import matplotlib.pyplot as plt

x_values = range(1, 1001)   # 创建一个包含x值的列表
y_values = [x**2 for x in x_values]  # 这个表达式有点少见

plt.rcParams['font.sans-serif'] = ['SimHei'] # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False   # 这两行需要手动设置

# plt.style.use('seaborn')  # 这一步导致过无法显示中文，具体原因未查
fig, ax = plt.subplots()
# 用来创建 总画布/figure“窗口”的，有figure就可以在上边（或其中一个子网格/subplot上）作图了，（fig：是figure的缩写）
# 算是固定的一种使用用法吧

# scatter是一个方法，向它传递x和y坐标将绘制一个点
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# 使用参数cmap告诉pyplot使用哪个颜色映射
# 将输入列表和输出列表传递给scatter

# 设置图表标题并给坐标轴加上标签
ax.set_title("平方数", fontsize = 24)
ax.set_xlabel("值", fontsize = 14)
ax.set_ylabel("值的平方", fontsize = 14)

# 设置刻度标记的大小
ax.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
ax.axis([0, 1100, 0, 1100000])
# 方法axis提供4个值，x的最小值和最大值，y的最小值和最大值

plt.show()

# 自动保存图表
plt.savefig('squares_plot.png', bbox_inches='tight')
# bbox_inches =’tight’作用为‘不会忽略不可见的轴’