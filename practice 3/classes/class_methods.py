# 1: жай метод
class K:
    def m(s):print("M!")
# 2: параметрмен метод
    def p(s,x):return x*2
# 3: селф колдану
    def s(s,ma):
        s.ma=ma
# 4: объект шакыру
obj=K()
obj.m()
print(obj.p(5))

obj.s()
print(obj.ma)