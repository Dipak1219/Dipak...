# n=int(input("Enter any no."))
for n in range(1,500):
    c=0
    for i in range(1,n+1):
          if (n%i==0):
             c=c+1
    if(c==2):
        print(n)        
#  else:
#     print("not")    