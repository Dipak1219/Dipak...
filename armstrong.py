for n in range(1,10000):
    t=n
    s=0
    while n>0:
        r=n%10
        s=s+(r*r*r*r)
        n=n//10
    if(t==s):
        print(s)    