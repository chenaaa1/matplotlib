import requests

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
response_dict = r.json()
# 打印与total_count相关联的值，指出共有多少个python仓库
print(f"Total respositories: {response_dict['total_count']}")

# 探索有关仓库的信息
repo_dicts = response_dict['items']
# 与items关联的值是列表，其中有很多字典，每个字典含一个仓库的信息,这里是存储字典列表
print(f"Repositories returned: {len(repo_dicts)}")
# 打印长度可知道含多少个仓库

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:    # 遍历repo——dicts中的所有字典
    # 打印项目名称
    print(f"Name: {repo_dict['name']}")
    # 因为项目所有者由字典表示，所以用键owner来访问表示所有者的字典
    # 再用键key来获取所有者的登录名
    print(f"Owner: {repo_dict['owner']['login']}")
    # 打印项目获得多少个星的评级
    print(f"Stars: {repo_dict['stargazers_count']}")
    # 打印该项目的url
    print(f"Repository: {repo_dict['html_url']}")
    # 显示项目创建时间和更新时间
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    # 打印仓库的描述
    print(f"Description: {repo_dict['description']}")

# # 研究第一个仓库
# repo_dict = repo_dicts[0]
# print("\nSelected information about first repository:")
# # 打印项目名称
# print(f"Name: {repo_dict['name']}")
# # 因为项目所有者由字典表示，所以用键owner来访问表示所有者的字典
# # 再用键key来获取所有者的登录名
# print(f"Owner: {repo_dict['owner']['login']}")
# # 打印项目获得多少个星的评级
# print(f"Stars: {repo_dict['stargazers_count']}")
# # 打印该项目的url
# print(f"Repository: {repo_dict['html_url']}")
# # 显示项目创建时间和更新时间
# print(f"Created: {repo_dict['created_at']}")
# print(f"Updated: {repo_dict['updated_at']}")
# # 打印仓库的描述
# print(f"Description: {repo_dict['description']}")


print(f"\nKeys: {len(repo_dicts)}")
# 打印字典所包含的键数
for key in sorted(repo_dict.keys()):
    # 打印这个字典的所有键
    print(key)

# 处理结果
# 打印response_dict中的键
print(response_dict.keys())