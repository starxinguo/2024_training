# 创建列表
invited_persons = ['he','wo','she','they']

# 打印邀请消息
print(f"Dear {invited_persons[0].title()}, can you have dinner with me?")
print(f"\nDear {invited_persons[1].title()}, can you have dinner with me?")
print(f"\nDear {invited_persons[2].title()}, can you have dinner with me?")
print(f"\nDear {invited_persons[3].title()}, can you have dinner with me?")

# 指出无法赴约的嘉宾
print(f"\nHowever, {invited_persons[0].title()} cannot come.")

# 将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名
invited_persons[0] = 'ni'

# 再次发出邀请
print(f"\nDear {invited_persons[0].title()}, can you have dinner with me?")
print(f"\nDear {invited_persons[1].title()}, can you have dinner with me?")
print(f"\nDear {invited_persons[2].title()}, can you have dinner with me?")
print(f"\nDear {invited_persons[3].title()}, can you have dinner with me?")