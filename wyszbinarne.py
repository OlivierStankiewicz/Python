import math


def wyszbin(t, n):
    l = 0
    p = len(t)-1
    i = 0
    while l <= p:
        i = math.floor((l+p)/2)
        if t[i] < n:
            l = i+1
        elif t[i] > n:
            p = i-1
        else:
            return i
    return None
