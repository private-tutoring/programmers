def solution(seoul):
    for i in seoul:
        if i == "Kim":
            s = seoul.index("Kim")
            return "김서방은 "+str(s)+"에 있다"
solution(["Jane", "Kim"])