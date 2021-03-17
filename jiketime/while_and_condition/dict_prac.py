d = {'name': 'json', 'dob': '2000-01-01', 'gender': 'male'}
for k in d:
    print(k)

for v in d.values():
    print(v)

for k, v in d.items():
    print('key:{}, value: {}'.format(k, v))

l = [1, 2, 3, 4, 5, 6, 7]
for index, item in enumerate(l):
    if index < 5:
        print(item)

# name_price: 产品名称(str)到价格(int)的映射字典
# name_color: 产品名字(str)到颜色(list of str)的映射字典
name_price = {}
name_color = {}
for name, price in name_price.items():
    if price < 1000:
        if name in name_color:
            for color in name_color[name]:
                if color != 'red':
                    print('name: {}, color: {}'.format(name, color))
        else:
            print('name: {}, color: {}'.format(name, 'None'))

for name, price in name_price.items():
    if price >= 1000:
        continue
    if name not in name_color:
        print('name: {}, color: {}'.format(name, 'None'))
        continue
    for color in name_color[name]:
        if color == 'red':
            continue
        print('name: {}, color: {}'.format(name, color))


