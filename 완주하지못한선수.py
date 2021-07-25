def solution(participant, completion):
    dic = {}
    for p in participant:
        if dic.get(p) == None:
            dic[p] = 1
        else: dic[p] += 1
    for c in completion:
        dic[c] += 1
    for k, v in dic.items():
        if v % 2 == 1:
            return k

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))