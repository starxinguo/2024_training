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

# 指出找到了一个更大的餐桌
print("\nI found a larger dining table.")
invited_persons.insert(0,'tian')
print(invited_persons)

invited_persons.insert(2,'gao')
invited_persons.append('di')
print(invited_persons)

# 打印邀请信息
print(f"\nDear {invited_persons[0].title()}, can you have dinner with me?")
print(f"Dear {invited_persons[1].title()}, can you have dinner with me?")
print(f"Dear {invited_persons[2].title()}, can you have dinner with me?")
print(f"Dear {invited_persons[3].title()}, can you have dinner with me?")
print(f"Dear {invited_persons[4].title()}, can you have dinner with me?")
print(f"Dear {invited_persons[5].title()}, can you have dinner with me?")
print(f"Dear {invited_persons[6].title()}, can you have dinner with me?")

# 删除元素
popped_person_1 = invited_persons.pop()
print(f"\nDear {popped_person_1.title()}, I am sorry that I cannot invite you to dinner.")

popped_person_2 = invited_persons.pop(0)
print(f"Dear {popped_person_2.title()}, I am sorry that I cannot invite you to dinner.")

popped_person_3 = invited_persons.pop(1)
print(f"Dear {popped_person_3.title()}, I am sorry that I cannot invite you to dinner.")

popped_person_4 = invited_persons.pop(2)
print(f"Dear {popped_person_4.title()}, I am sorry that I cannot invite you to dinner.")

popped_person_5 = invited_persons.pop(1)
print(f"Dear {popped_person_5.title()}, I am sorry that I cannot invite you to dinner.")

# 告知余下的两位
print(f"\nDear {invited_persons[0].title()}, you are still among the invitees.")
print(f"Dear {invited_persons[1].title()}, you are still among the invitees.")

# 将最后两位嘉宾从名单中删除
del invited_persons[0]
del invited_persons[0]
print(invited_persons)
print("\n我总共邀请的嘉宾数：")
print(len(invited_persons))