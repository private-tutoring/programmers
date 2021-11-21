def solution(dartResult):
    dartList = ["", "", ""]
    count = -1
    nextIndex = False

    for ii, c in enumerate(dartResult):
        if nextIndex:
            nextIndex = False
            continue
        if c.isnumeric():
            if dartResult[ii+1] == '0':
                c = "10"
                nextIndex = True
            for i, v in enumerate(dartList):
                if v == "":
                    dartList[i] = int(c)
                    count = count + 1
                    break
        else: 
            if c == "D":
                dartList[count] = dartList[count] ** 2
            elif c == "T":
                dartList[count] = dartList[count] ** 3
            elif c == "*":
                if count > 0:
                    dartList[count-1] = dartList[count-1] * 2
                dartList[count] = dartList[count] * 2
            elif c == "#":
                dartList[count] = dartList[count] * -1
    return sum(dartList)


print(solution('1D2S#10S'))