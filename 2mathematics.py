a=int(input())
T=0
for i in range(2,a//2+1):
      if(a%i==0):
        T=T+1
if(T<=0):
   print('yes')
else:
   print('no')
