# 1: жуп сандар
n=[1,2,3,4,5,6];print(list(filter(lambda x:x%2==0,n)))
# 2: узын создер
w=["alma","nan","banan"];print(list(filter(lambda x:len(x)>3,w)))
# 3: бос емес
d=["",None,"ok"];print(list(filter(None,d)))
# 4: улкен сандар
z=[10,50,5,100];print(list(filter(lambda x:x>20,z)))