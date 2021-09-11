def solution(s, n):
    answer = ''
    f = n
    for i in s:
        # if i == " ":
        #     answer += " "
        #     continue
        n = f
        if i == "Z":
            n = n-1
            i = "A"
        elif i == "z":
            n = n-1
            i = "a"
        
        if i.islower():
            if 122 < ord(i)+n:
                i = chr(97+(ord(i)+n-122)-1)
                answer += chr(ord(i))
            elif 97 <= ord(i) <= 122:
                answer += chr(ord(i)+n)
                
        elif 90 < ord(i)+n < 97:
            i = chr(((65+(ord(i)+n-90)))-1)
            answer += chr(ord(i))
            
        
        elif 65 <= ord(i) <= 90:
            if ord(i)+n > 90:
                answer += chr(ord(i)+n - 91 +65)
            else:
                answer += chr(ord(i)+n)
            
        else:
            answer += i
    
    return answer

print(solution("X x y", 25))