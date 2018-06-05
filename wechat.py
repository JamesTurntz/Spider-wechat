import itchat
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False
male = female = other = 0
x1 = ['男', '女', 'unknow']
y1 = []
itchat.login()
friends = itchat.get_friends(update=True)[0:]

# 0是自己，从1开始忽略自己
for friend in friends[1:]:
    sex = friend["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1

y1.append(male)
y1.append(female)
y1.append(other)

plt.figure(1)
plt.bar(x1, y1)


def get_var(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable


NickName = get_var("NickName")
Sex = get_var('Sex')
Province = get_var('Province')
City = get_var('City')
Signature = get_var('Signature')

# 保存到CSV文件
'''
data = {'NickName': NickName, 'Sex': Sex, 'Province': Province,
        'City': City, 'Signature': Signature}
frame = DataFrame(data)
frame.to_csv('data.csv', index=True)
'''
cities = set(Province)
cities = list(cities)
n = len(cities)
m1 = int(n / 3)
m2 = 2 * m1

y2 = []
x2 = []
for i in range(m1):
    if (cities[i] == ''):
        x2.append('unknow')
    else:
        x2.append(cities[i])
    y2.append(Province.count(cities[i]))
plt.figure(2)
plt.bar(x2, y2)

y2 = []
x2 = []
for i in range(m1, m2):
    if (cities[i] == ''):
        x2.append('unknow')
    else:
        x2.append(cities[i])
    y2.append(Province.count(cities[i]))

plt.figure(3)
plt.bar(x2, y2)

y2 = []
x2 = []
for i in range(m2, n):
    if (cities[i] == ''):
        x2.append('unknow')
    else:
        x2.append(cities[i])
    y2.append(Province.count(cities[i]))

plt.figure(4)
plt.bar(x2, y2)

plt.show()
