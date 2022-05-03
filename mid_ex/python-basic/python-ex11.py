on_off = 'led=on&motor=off&switch=off'

on_off = on_off.replace('=', ':')

on_off = on_off.split('&')

keys = []
values = []

for data in on_off:
    pair = data.split(':')
    keys.append(pair[0])
    values.append(pair[1])

dic = dict(zip(keys, values))
print(dic)