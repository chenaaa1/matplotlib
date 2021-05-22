import requests
# 导入bar类和模块offline
from plotly.graph_objs import Bar
from plotly import offline

# 执行API调用并存储响应
# 存储API调用的URL
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# 要求使用第三版的github API版本
headers = {'Accept': 'application/vnd.github.v3+json'}
# 用requests调用API
# 调用get（）并将url传给它，再将响应对象赋给变量r
# 响应对象包含一个Status code的属性，指出请求是否成功（返回200为成功）
r = requests.get(url, headers=headers)
# 打印Status code
print(f"Status code: {r.status_code}")  # status_code是类属性
# 将API响应赋给一个变量
# API返回json格式的信息
# 所以用方法json（）将信息转换为python字典

# 处理结果
response_dict = r.json()
# 探索有关仓库的信息
repo_dicts = response_dict['items']
# 与items关联的值是列表，其中有很多字典，每个字典含一个仓库的信息,这里是存储字典列表
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:    # 遍历repo——dicts中的所有字典
    repo_name = repo_dict['name']
    # 提取项目的url并赋给临时变量repo_url
    repo_url = repo_dict['html_url']
    # 创建一个指向项目的链接，使用html标记</a>
    # 其格式为<a href='URL'>linktext</a>
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    # 提取每个项目的所有者和描述
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    # <br />是html中的换行符
    label = f"{owner}<br />{description}"
    labels.append(label)

# 可视化
data = [{       # 定义列表data,这里是列表里存字典\
    'type': 'bar',
    # 将列表用作图表的x值，这样就可以点击x值达到点击链接的作用
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {     # maker设置影响条形设计，选择一种自定义的蓝色
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]
# 使用字典定义图表的布局
my_layout = {
    'title': 'GitHub上最受欢迎的python项目',
     # 指定图表名称的字号
    'titlefont':{'size': 28},
    'xaxis': {
        'title': 'Repository',
        # 指定x轴标签字号
        'titlefont': {'size': 24},
        # 刻度标签字号
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')