# 定义5种简单的食品
menu = ("蔬菜沙拉", "燕麦粥", "牛肉卷饼", "水果拼盘", "明太子饭团")

# 用新的食品创建一个新的元组
new_menu = ("蔬菜沙拉", "燕麦粥", "鸡肉卷饼", "寿司拼盘", "烤鱼")

# 将新的元组赋值给原有变量
menu = new_menu

# 打印新的菜单
for item in menu:
    print(item)
# 使用for循环打印出这些食品
for item in new_menu:
    print(item)