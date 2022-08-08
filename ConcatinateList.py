list1 = {1: 10, 2: 20}
list2 = {3: 30, 4: 40}

list3 = {}
for d in (list1, list2):
    list3.update(d)
    print(list3)
