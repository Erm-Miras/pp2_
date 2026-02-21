# 1: жай сорттау
s=[(1,2),(3,1)];print(sorted(s,key=lambda x:x[1]))
# 2: создер узындыгымен
w=["a","ccc","bb"];print(sorted(w,key=lambda x:len(x)))
# 3: диктты сорттау
d=[{"a":2},{"a":1}];print(sorted(d,key=lambda x:x["a"]))
# 4: терис ретпен
n=[1,5,2];print(sorted(n,key=lambda x:-x))