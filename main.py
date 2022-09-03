import csv
import json


with open("files/users.json", "r") as f:
    users_all_info = json.load(f)
    users = []

for elem in users_all_info:
    users.append({
        'name': elem['name'],
        'gender': elem['gender'],
        'address': elem['address'],
        'age': elem['age'],
        'books': []
    })

with open("files/books.csv", newline='') as f:
    books = list(csv.DictReader(f))
    for elem in books:
        del elem['Publisher']

j = 0
for i in range(len(books)):
    if j == len(users):
        j = 0
    users[j]['books'].append(books[i])
    j += 1


with open("result.json", "w") as f:
    reference = json.dumps(users, indent=4)
    f.write(reference)