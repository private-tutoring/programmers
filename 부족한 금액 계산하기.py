def solution(price, money, count):
    nom_price = price
    for i in range(2, count+1):
        price += nom_price * i
    if price < money:
        return 0
    return price - money




print(solution(3,20,4))