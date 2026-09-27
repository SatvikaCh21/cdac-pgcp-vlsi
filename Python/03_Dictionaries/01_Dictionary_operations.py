#convert  2 lists into dict
keys=['name','address','salary']
values=['Satvika','Hyderabad','50000']
d1=dict(zip(keys,values))
print(d1)

#merge 2 dicts into 1
d2={'Address': 'Vijayawada' , 'PRN':19, 'Country':'India'}
d3={'Name': 'niharika' , 'Age':22, 'Salary': 200000 }
merged=d2|d3
print(merged)

# initialize dict with default values
keys=['name','address','salary']
d=dict.fromkeys(keys,0)
print(d)

#create dict by extracting keys from given dict
original = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
selected_keys = ['a', 'c']
new_dict = {k: original[k] for k in selected_keys}
print(new_dict)

#delete list of keys from a dict
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys_to_delete = ['a', 'c']
for key in keys_to_delete:
    my_dict.pop(key, None)

print(my_dict)

#check if value exists in dict
my_dict = {'a': 1, 'b': 2, 'c': 3}
value_to_check = 2
if value_to_check in my_dict.values():
    print("Value exists")
else:
    print("Value does not exist")


