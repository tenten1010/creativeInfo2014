#円心(5,5)　半径5の円
#辺長10の正方形
def isCircle(i,j):
	if (i-5)**2 + (j-5)**2 <= 5**2:
		return True
	else:
		return False
def isRange(d):
	r1,r0 = (0,0)
	for i in range(11):
		for j in range(11):
			if i%d == 0 and j%d ==0:
				if isCircle(i,j):
					r1 += 1
					r0 += 1
				else:
					r0 += 1
			else:
				pass
	return (r1,r0)

if __name__ == '__main__':
	i,j=(0,0)
	d = int(input("input d:"))
	r1,r0 = isRange(d)
	result = r1 / r0*4
	print(result)