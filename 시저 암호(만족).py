def solution(s, n):
    re = ""
    for i in s:
        i = ord(i)
        if i == 32 or i == 9 or i == 10 or i == 11 or i == 12 or i == 13:
            re += chr(i)
            continue
        for j in range(n):
            if i == 90:
                i = 65
                continue
            elif i == 122:
                i = 97
                continue
            i += 1
        re += chr(i)
    return re
        
print(solution("AB", 1))