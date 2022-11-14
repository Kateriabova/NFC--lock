# -*- coding: UTF-8 -*Ы

with open('db/numbers.csv', 'r', encoding='windows-1251') as f:
    head = f.readline()
    data = [i.rstrip() for i in f.readlines()]
    titles = data[0].split(',')
    for i, elem in enumerate(data):
        for j, val in enumerate(elem.split(';')):
            print(val)

