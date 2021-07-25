def solution(absolutes, signs):
    result = 0
    for i in range(len(absolutes)):
        # if signs[i] == False:
        #     result -= absolutes[i]
        # else:result += absolutes[i]
        result += -absolutes[i] if not signs[i] else absolutes[i]
    return result

    bool result = 2<3 ? true : false
    result = true if 2<3 else false
    