from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# 创建一个D6
die = Die()

# 掷几次骰子并将结果存储到一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides+1):  # 后面加1是因为range的特性,计数到最后一个参数时停止
    frequency = results.count(value)    # count是统计字符串里某个字符串出现的个数
    frequencies.append(frequency)

# 对结果进行可视化
x_values = list(range(1, die.num_sides+1))  # list将range的值转换为列表给plotly用
data = [Bar(x=x_values, y=frequencies)]  # Bar表示用于绘制条形图的数据集

# 设置坐标轴标签
x_axis_config = {'title': '结果'}
y_axis_config = {'title': '结果的频率'}
# 类Layout返回一个指定图表布局和配置的对象
my_layout = Layout(title='掷一个D6 1000次的结果',
                   xaxis=x_axis_config, yaxis=y_axis_config)
# 函数offline.plot生成图表，文件名是保存位置，前两个是包含数据和布局对象的字典
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')

print(frequencies)