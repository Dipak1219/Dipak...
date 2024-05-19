for n in range(1,501):
    i=n
    s=0
    while n>9:
        while n>0:
            r=n%10
            s=s+r
            n=n//10
        n=s
        s=0   
    if(n==1):
        print(i)    
