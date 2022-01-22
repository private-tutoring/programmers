def solution(id_list, report, k):
    target_dic = dict()
    target_reporters_dic = dict()
    resceive_dic = dict()
    for i in id_list:
        target_reporters_dic[i] = []
        target_dic[i] = 0
        resceive_dic[i] = 0
    for r in report:
        reporter, target = r.split(' ')
        if reporter in target_reporters_dic[target]:
            continue
        target_dic[target] += 1
        target_reporters_dic[target].append(reporter)
    for i in id_list:
        if target_dic[i] >= k:
            for reporter in target_reporters_dic[i]:
                resceive_dic[reporter] += 1
    result = []
    for i in id_list:
        result.append(resceive_dic[i])
    return result

    

print(solution(["con", "ryan"],	["ryan con", "ryan con", "ryan con", "ryan con"],	3))