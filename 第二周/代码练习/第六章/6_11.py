# 创建字典
cities = {
    'beijing': {
        'country': 'china',
        'population': '1000000',
        'fact': 'capital',
        },
    'shanghai': {
        'country': 'china',
        'population': '123456',
        'fact': 'financial',
        },
    'wuhan': {
        'country': 'china',
        'population': '234567',
        'fact': 'little capital',
        },
    }

# 打印信息
for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    for x, y in city_info.items():
        print(f"\t{x.title()}: {y.title()}")