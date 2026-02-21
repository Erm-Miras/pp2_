# 1: инитпен класс
class P:
    def __init__(s,n):s.n=n
# 2: еки параметр
class B:
    def __init__(s,a,b):s.a=a;s.b=b
# 3: дефолт ман
class C:
    def __init__(s,v=0):s.v=v
# 4: объекттер
p1=P("Ali");c1=C(10);print(p1.n,c1.v)