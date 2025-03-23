d = {"banana": 3, "apple": 4, "pear": 1, "orange": 2}
keys = d.keys()
print(keys)


keys = sorted(keys)
print(keys)


for key in keys:
    print(key, d[key])



from collections import OrderedDict

d = {"banana": 3, "apple": 4, "pear": 1, "orange": 2}
new_d = OrderedDict(sorted(d.items()))
print(new_d)


for key in new_d:
    print(key, new_d[key])
