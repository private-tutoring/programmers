a = [
    {"id": 3},
    {"id": 6},
    {"id": 2},
    {"id": 0},
    {"id": 9}
]

a.sort(key=lambda x: x['id'])
print(a)