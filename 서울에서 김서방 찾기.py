def solution(seoul):
    f = 0 
    for i in seoul:
        if i == "Kim":
            f = seoul.index(i)
            break
    return "김서방은" + str(f) + "에 있다"



solution(["Jane", "Kim"])