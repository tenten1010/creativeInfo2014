#辺長10の正方形
i,j=(0,0)
count = 0
d = int(input("input d:"))
for i in range(11):
	for j in range(11):
		if i%d == 0 and j%d ==0:
			count +=1
		else:
			pass
print(count)