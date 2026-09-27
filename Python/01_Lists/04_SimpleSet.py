v_set={10,20,10,30}
print(v_set)
v_list=[10,20,30,10]
v_setlist=set(v_list)
print(v_setlist)

v_set10={100,200,300,400}
v_set20={100,200,300}

print(v_set10.union(v_set20))
print(v_set10.intersection(v_set20))
print(v_set20.difference(v_set10))

v_set20.update((40,))
print(v_set20)

v_set20.update([50])
print(v_set20)



