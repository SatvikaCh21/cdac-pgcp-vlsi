"""d1={'Name': 'Satvika' , 'Age':21, 'Country':'India'}
d2={'Name': 'niharika' , 'Age':22, 'Salary': 200000 }
print(d1.get('Name'))
print(d1.get('Address'))

d1.update(d2)
print(d1)

d1.popitem()
print(d1)"""

d3={'Name': 'Satvika' , 'Age':(19,21) , 'Country':'India'}
print(d3.items())
print(list(d3.items())[1][1][1])

#print(list(d3.items())[2][1])
print(list(d3.keys()))
print(list(d3.values()))


list10=["Name","Address","Salary"]
list20=["King","Pune",40000]
dictnew=dict((zip(list10,list20)))
print(dictnew)