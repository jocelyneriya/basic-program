int_num = list(map(int,input().split()))
a,b,c = sorted(int_num)
if a**2+b**2==c**2:
	print('yes')
else:
	print('no')
		
