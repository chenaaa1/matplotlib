import csv
from datetime import datetime

import matplotlib.pyplot as plt

# filename = 'sitka_weather_07-2018_simple.csv'
# filename = 'sitka_weather_2018_simple.csv'
filename = 'death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)  # reader是一个函数
    # reader处理文件中以逗号分隔的第一行数据，
    # 并将每项数据作为一个元素存储到列表中
    header_row = next(reader)     # next是函数，reader是变量
    # next会返回文件中的下一行

    # 从文件中获取日期，最高温度和最低温度
    dates, highs, lows = [], [], []
    for row in reader:  # 遍历文件中余下的各行
        # 将包含日期信息的数据转化为datetime对象，'%Y-%m-%d'是模块datetime的内置实参
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])  # 因为文件以字符串形式存储，所以要化为int
            # 文件索引5处是温度
            low = int(row[5])
        except ValueError:  # 出现空异常则打印信息,然后再进行循环
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

print(highs)

# 根据最高温度和最低温度绘制图形
plt.style.use('seaborn')    # use是函数
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)  # 将日期和最高温度传给plot
ax.plot(dates, lows, c='blue', alpha=0.5)  # alpha指定颜色的透明度
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# fill_between接受一个x值系列和2个y值系列，实参facecolor指定填充区域的颜色
# 后面的alpha=0.1为了让颜色不太显眼

# 设置图形的格式
title = "2018年每日最高温度和最低温度\n 美国加利福尼亚州死亡谷"
ax.set_title(title, fontsize = 20)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate()
# 调用fig.autofmt_xdate来绘制倾斜的日期标签
ax.set_ylabel("温度 (F)", fontsize = 16)
ax.tick_params(axis='both', which = 'major', labelsize = 16)

# 中文显示，放在上面似乎不可以
plt.rcParams['font.sans-serif'] = ['SimHei'] # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False   # 这两行需要手动设置

plt.show()
