def solution(s):
    if len(s) % 2 == 0:
        return "%s%s" % (s[len(s)//2-1], s[len(s)//2])

    else:
        return "%s" % (s[len(s)//2])

print(solution("qwer"))
   