s,e=input().split()
s=int(s)
e=int(e)
count=0
u=0
for i in range(s,e+1):
  sum=0
  while i>0:
    dig=i%10
    sum=sum+dig
    i=i//10
  count=0
  for j in range(2,sum+1):
    if(sum%j==0):
      count+=1
  if count==1:
    u+=1
print(u)
