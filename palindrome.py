for n in range(1,5000):
    t=n
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    if(t==s):
        print(s)    