def solution(n):
    s = 0
    def sol(y, q):
        rev_base = ''

        while y > 0:
            y, mod = divmod(y, q)
            rev_base += str(mod)

        return rev_base 
    s = int(sol(n, 3), 3)

    return s