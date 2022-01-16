def solution(numbers, hand):
    result = ""
    left_hand_hight = [0,0]
    right_hand_hight = [0,2]
    left_number_list = [1,4,7]
    right_number_list = [3,6,9]
    TFEZ = {2:(3,1), 5:(2,1), 8:(1,1), 0:(0,1)}
    for i in numbers:
        if i in left_number_list:
            result += "L"
            if i == 1:
                left_hand_hight[0] = 3
                left_hand_hight[1] = 0
            elif i == 4:
                left_hand_hight[0] = 2
                left_hand_hight[1] = 0
            elif i == 7:
                left_hand_hight[0] = 1
                left_hand_hight[1] = 0
        elif i in right_number_list:
            result += "R"
            if i == 3:
                right_hand_hight[0] = 3
                right_hand_hight[1] = 2
            elif i == 6:
                right_hand_hight[0] = 2
                right_hand_hight[1] = 2
            elif i == 9:
                right_hand_hight[0] = 1
                right_hand_hight[1] = 2
        else:
            tfez = TFEZ[i]
            r = abs(tfez[0]-right_hand_hight[0]) + abs(tfez[1]-right_hand_hight[1])
            l = abs(tfez[0]-left_hand_hight[0]) + abs(tfez[1]-left_hand_hight[1])
            if r == l:
                if hand == "right":
                    result += "R"
                    right_hand_hight[0] = tfez[0]
                    right_hand_hight[1] = tfez[1]
                else: 
                    result += "L"
                    left_hand_hight[0] = tfez[0]
                    left_hand_hight[1] = tfez[1]
            elif r > l:
                result += "L"
                left_hand_hight[0] = tfez[0]
                left_hand_hight[1] = tfez[1]
            else:
                result += "R"
                right_hand_hight[0] = tfez[0]
                right_hand_hight[1] = tfez[1]
    return result
            

            

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))