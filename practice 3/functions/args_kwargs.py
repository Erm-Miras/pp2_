# 1: шексиз сандар
def s(*a):print(sum(a))
s(1,2,3,4,5)
# 2: шексиз создиктер
def d(**k):
    for i in k:print(i,k[i])
d(id=1,baq="5")
# 3: аралас
def mix(a,*b,**c):print(a,b,c)
mix(0,1,2,x=9)
# 4: аргументти тарату
def taratu(a,b,c):print(a+b+c)
v=[1,2,3];taratu(*v)