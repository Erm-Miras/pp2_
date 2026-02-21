# 1: биринши ата
class L:l=1
# 2: екинши ата
class R:r=2
# 3: косу
class M(L,R):pass
# 4: колдану
m=M();print(m.l+m.r)
if m.l==1:print("L bar")
print("R bar")