from typing import final
from typing_extensions import Final


def solution(strings, n):
    x = set()
    y = []
    f = 0
    g = 0
    strings.sort(key=lambda x: x[n])
    for i in range(len(strings)):
        try:
            if strings[i][n] == strings[i-1][n]:
                final f = i
                x.add(i)
                x.add(i-1)
                
    
        except: break
            
            
            
    if len(x) >= 2:
        y = strings[min(x):max(x)+1]
        strings.remove(strings[i])
        strings.remove(strings[i-1])
        y.sort()
        for i in range(len(y)):
            strings.insert(min(x), y[i])
    print(x)

        
    return strings
print(solution(["abce", "abcd", "cdx", "agcf", "reab"], 2))