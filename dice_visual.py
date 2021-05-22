from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# 创建1个D6和一个D10
die_1 = Die()   # 无参数默认为6
die_2 = Die(10)

# 掷几次骰子并将结果存储到一个列表中
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
# 两个骰子最小点数为2
for value in range(2, max_result+1):  # 后面加1是因为range的特性,计数到最后一个参数时停止
    frequency = results.count(value)    # count是统计字符串里某个字符串出现的个数
    frequencies.append(frequency)

# 对结果进行可视化
x_values = list(range(2, max_result+1))  # list将range的值转换为列表给plotly用
data = [Bar(x=x_values, y=frequencies)]  # Bar表示用于绘制条形图的数据集

# 设置坐标轴标签
x_axis_config = {'title': '结果', 'dtick':1}  # dtick键指定x轴显示的刻度间距
y_axis_config = {'title': '结果的频率'}
# 类Layout返回一个指定图表布局和配置的对象
my_layout = Layout(title='掷1个D6和一个D10 50000次的结果',
                   xaxis=x_axis_config, yaxis=y_axis_config)
# 函数offline.plot生成图表，文件名是保存位置，前两个是包含数据和布局对象的字典
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')


print(frequencies)