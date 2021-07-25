def solution(s):
    result = []
    arr = s.split(" ")
    for s in arr:
        new_word = ""
        for i, al in enumerate(s):
            if i % 2 == 0:
                new_word += al.upper()
            else: new_word += al.lower()
        result.append(new_word)    
    print(" ".join(result))

    return 