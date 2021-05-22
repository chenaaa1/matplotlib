import json
import plotly.express as px
import pandas as pd

# 探索数据的结构
filename = 'eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)  # load是一个函数
    # json.load(f)将数据转为python能够处理的格式

all_eq_dicts = all_eq_data['features']  # 提取与键features相关联的数据

mags, titles, lons, lats = [], [], [], []   # 创建空列表
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    # ['properties']['mag']因为震级都存储在字典properties部分的mag键下
    title = eq_dict['properties']['title']
    # titles用于存储位置标题,提取字典properties里title键对应的值
    lon = eq_dict['geometry']['coordinates'][0]
    # 第一个参数是字典，第二个是列表，第三个是列表里的值,[0]代表第一个值
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(titles[:2])
print(lons[:5])
print(lats[:5])

print(len(all_eq_dicts))

# 将所有有关数据的信息以键值对的形式放在一个字典中
data = pd.DataFrame(
    data=zip(lons, lats, titles, mags), columns=['经度', '纬度', '位置', '震级']
)
data.head()

fig = px.scatter(
    data,
    # 下面标红的都是python内置函数
    x = '经度',
    y = '纬度',
    range_x = [-200, 200],
    range_y = [-90, 90],
    width = 800,
    height = 800,
    title = '全球地震散点图',
    size='震级',
    size_max=10,
    color='震级',
    hover_name='位置'
)
# write_html是一个类实例方法
fig.write_html('global_earthquakes.html')
fig.show()

readable_file = 'readable_eq_data.json'  # 创建一个文件
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)
    # json.dump接受一个json数据对象和一个文件对象，并将数据写入这个文件
    # indent=4让dump使用与数据结构匹配的缩进量来设置数据格式