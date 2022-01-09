def solution(participant, completion):
    dic = {}
    for i in participant:
        if dic.get(i) == None:
            dic[i] = 1
        else: dic[i] += 1
    for i in completion:
        dic[i] += 1
    for i, j in dic.items():
        if i % 2 == 1:
            return j

        


print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))