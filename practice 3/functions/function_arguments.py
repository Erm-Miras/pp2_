# 1: дефолтты аргумент
def k(a,b=2):print(a*b)
k(5);k(5,3)
# 2: позиционный
def info(f,j):print(f"{f}-{j}")
info(20,"zhasta")
# 3: тизимди аргумент кылу
def tizim(l):
    for i in l:
        print(i)
tizim([1,2,3])