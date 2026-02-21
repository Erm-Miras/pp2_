# 1: ата класс
class A:
    def f1(s):print("A")
# 2: бала класс
class B(A):
    def f2(s):print("B")
# 3: тексеру
o=B();o.f1();o.f2()
# 4: мурагерлик тизбеги
class C(B):pass
c=C();c.f1()