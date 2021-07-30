def solution(s):
    s = list(s)
    Ycount = 0
    Pcount = 0
    for i in range(len(s)):
        if s[i] == 'p' or s[i] == 'P':
            Pcount += 1
        if s[i] == 'y' or s[i] == 'Y':
            Ycount += 1
    if Pcount == Ycount or Pcount == 0 and Ycount == 0:
        return True
    else: return False



solution("pPoooyY")