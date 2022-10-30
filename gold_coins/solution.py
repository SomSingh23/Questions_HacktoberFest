def total(n):
    if n==0:
        return 0
    if n in d:
        return d[n]
    else:
        d[n]=max(n,(total(int(n/2))+total(int(n/3))+total(int(n/4))))
        return d[n]

d={}
while(True):
    try:
        n=int(input())
        print(total(n))
    except:
        break
