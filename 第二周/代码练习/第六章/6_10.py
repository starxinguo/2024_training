like_numbers = {
    'a': [1,2],
    'b': [2,3],
    'c': [3,4],
    'd': [4,5],
    'e': [5,6],
    }

# 打印
# 打印名字及喜欢的数字
for name, numbers in like_numbers.items():
    print(f"\n{name.title()} likes these numbers: ")
    for number in numbers:
        print(f"\t{number}")