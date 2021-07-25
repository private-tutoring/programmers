def solution(s):
    result = ""
    length = len(s)
    if length % 2 == 0:
        mid = length // 2
        pre = mid - 1
        result = s[pre] + s[mid]
    else:
        result = s[length // 2]
    return result