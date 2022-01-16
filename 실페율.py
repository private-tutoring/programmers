# import operator

# def solution(N, stages):
#     stages.sort()
#     users = len(stages)
#     l = [0 for _ in range(N+1)]

#     tempStages = set(stages)

#     if len(tempStages) == 1:
#         first = tempStages.pop()
#         result = [first] + [i for i in range(1, first)] + [i for i in range(first+1, N+1)]
#         return result

#     for i in range(1, N+1): # stage 번호 반복
#         for j in range(i-1, users): # i번째 stage기준으로 stages반복
#             if i <= stages[j]:
#                 l[i] = users - j
#                 break

#     result = dict()
#     for i in range(1, N+1):
#         result[i] = stages.count(i) / l[i]
    
#     result = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
#     result = list(map(lambda x: x[0], result))
#     return result
  
import operator

def solution(N, stages):
    stages.sort()
    total_user_length = len(stages) # 게임에 참여한 총 사용자

    rate_list = [[0, 0] for _ in range(N+1)]

    minus_user_length = 0
    same_stage_count = 1
    for i in range(0, total_user_length):
        if i != 0 and stages[i-1] == stages[i]:
            rate_list[stages[i]][0] += 1
        else:
            if stages[i] > N: break
            same_stage_count = 1
            user_length = total_user_length - minus_user_length # 총 사용자에서 스테이지에 도달한 사용자의 수 
            rate_list[stages[i]] = [same_stage_count, user_length]
        minus_user_length += 1

    result = dict()    
    for i in range(1, N+1):
        a, b = rate_list[i]
        if b == 0: result[i] = 0
        else: result[i] = a/b

    result = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
    result = list(map(lambda x: x[0], result))
    return result



