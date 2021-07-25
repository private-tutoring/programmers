def solution(s):
    arr = list(s)
    arr.sort(key=lambda x: ord(x), reversed=True)
    
    return "".join(arr)