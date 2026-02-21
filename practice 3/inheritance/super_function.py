# 1: супер инит
class X:
    def __init__(s,n):s.n=n
class Y(X):
    def __init__(s,n,a):super().__init__(n);s.a=a
# 2: супер метод
class Z(Y):
    def info(s):super().__init__("N",0);print("Z")
# 3: объект
y=Y("D",20);print(y.n)
# 4: тексеру
z=Z("A",1);z.info()