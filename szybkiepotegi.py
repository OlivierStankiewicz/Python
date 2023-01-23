def potega(x,n):
    if n==0:
        return 1
    if n%2==1:
        return x*potega(x,n-1)
    else:
        a=potega(x,n/2)
    return a**2

print(potega(2,6))
