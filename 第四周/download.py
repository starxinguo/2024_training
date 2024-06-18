import requests

# 指定要下载的文件URL
url = 'https://bj.bcebos.com/apollo-air/v2-2022-01-08/single-vehicle-side-example_16213950939799552.zip?authorization=bce-auth-v1%2F62ff93831d5840338d0fcc9585430b3a%2F2024-06-18T08%3A10%3A14Z%2F604800%2F%2Fb6e9563f9f028306e6a34d867cca72b312bbd0620aed5c8b3a080dc13030efac'

# 发送GET请求并获取响应
response = requests.get(url)

# 将响应内容保存到文件中
with open('data.zip', 'wb') as f:
    f.write(response.content)