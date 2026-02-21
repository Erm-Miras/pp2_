# 1: шексиз сандар
def s(*a):
    print(sum(a))
s(1,2,3,4,5)
# 2: шексиз создиктер
def d(**k):
    for i in k:
        print(i,k[i])
k={"one":1,"two":2,"three":3}
d(**k)
# 3: аралас
def mix(a,b,c):
    print(a,b,c)
mix(0,1,2)