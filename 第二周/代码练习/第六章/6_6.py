# 创建列表
favorite_languages = {
    'a': 'python',
    'b': 'c',
    'c': 'c#',
    'd': 'php',
    }

# 创建调查人员名单
investigators = ['b', 'd', 'c', 'e']
for investigator in investigators:
    if investigator in favorite_languages.keys():
        print(f"{investigator.title()}, thank you for participating in our survey!")
    else:
        print(f"{investigator.title()}, can I invite you to participate in our survey?")