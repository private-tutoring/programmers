import re

def solution(new_id):
    new_id = new_id.lower()
    result = ""
    for i in new_id[:]:
        if i == "-" or i == "_" or i == '.' or i.isalpha() or i.isdecimal():
            result += i
    new_id = result
    new_id = re.sub("\.\.*", ".", new_id)
    if new_id[0] == ".":
        new_id = new_id[1:]
    if len(new_id) >= 1 and new_id[-1] == ".":
        new_id = new_id[:len(new_id)-1]
    if new_id == "":
        new_id = "a"
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:len(new_id)-1]
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1]
    print(new_id)
    return new_id

        
solution("=.=")