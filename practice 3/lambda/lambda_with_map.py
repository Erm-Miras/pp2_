# 1: сандык тизим
l=[1,2,3];print(list(map(lambda x:x*2,l)))
# 2: стрингтер
s=["a","b"];print(list(map(lambda x:x+"!",s)))
# 3: еки тизимди косу
a=[1,2];b=[3,4];print(list(map(lambda x,y:x+y,a,b)))
# 4: типти ауыстыру
n=["1","2"];print(list(map(int,n)))