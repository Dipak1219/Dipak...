for n in range(1,500):
    i=2
    while i<=n-1:
        if(n%i==0):
            break
        i+=1
    if(i==n):
        print(n)    