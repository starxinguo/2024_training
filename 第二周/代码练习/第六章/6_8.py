# 创建多个字典
a = {
    'type': 'dog',
    'host': 'guo xin',
    }
b = {
    'type': 'cat',
    'host': 'zhang hongyi',
    }
c = {
    'type': 'mouse',
    'host': 'ren jiayu',
    }

# 将字典存储在列表中
pets = [a, b, c]

# 遍历列表
for pet in pets:
    print(pet)