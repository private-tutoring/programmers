def solution(table, languages, preference):
    lang_dic = {}
    real_dic = {}
    for s in table:
        s = s.split(' ')
        lang_arr = s[1:]
        lang_dic[s[0]] = lang_arr

    for k, v in lang_dic.items():
        real_dic[k] = 0
        for i, l in enumerate(languages):
            if l in v:
               real_dic[k] += preference[i] * (5 - v.index(l))

    k, v = max(key=lambda x: x[1], *real_dic.items())
    real_list = []
    for k2, v2 in real_dic.items():
        if v == v2:
            real_list.append(k2)
    real_list.sort()
    return real_list[0]

solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5])