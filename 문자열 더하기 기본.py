def solution(s):
    if len(s) == 4 or len(s) == 6:
        try:
            s = int(s)
        except ValueError:
            return False
        return True
    else: return False