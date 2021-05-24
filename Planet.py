def check(t,r1,r2,r3,v1,v2,v3,n):
    i=0
    while i<=n:
        if (r3*v3)%(r2*v2)==0 and (r2*v2)%(r1*v1)==0:
            return True
        else:
            return False
  

 

t=int(input())
for i in range(1,t+1):
  r1=int(input())
  r2=int(input())
  r3=int(input())

  v1=int(input())
  v2=int(input())
  v3=int(input())
  n=int(input())
  check=check(t,r1,r2,r3,v1,v2,v3,n)
  print(check)