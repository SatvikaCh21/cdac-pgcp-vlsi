import csv

data = [['Name', 'Age'],['Alice', 30],['John', 25]]

with open('people.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Data written to people.csv successfully!")