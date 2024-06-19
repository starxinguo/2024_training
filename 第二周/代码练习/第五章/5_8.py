# 创建用户名列表
users = ['admin', '1', '2', '3', '4']

# 遍历列表并打印相应的消息
for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?\n")
    else:
        print(f"Hello {user}, thank you for logging in again.")