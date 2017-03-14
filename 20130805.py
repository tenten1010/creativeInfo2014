def distance(x1,y1,x2,y2):
	return ((x2-x1)**2+(y2-y1)**2)**0.5

def isInTriangle(x1,y1,x2,y2,x3,y3,arr):
	dist = distance(x1,y1,arr[0],arr[1])+distance(x2,y2,arr[0],arr[1])+distance(x3,y3,arr[0],arr[1])
	sideLength = distance(x1,y1,x2,y2)
	if dist >= 3**0.5*sideLength and dist <= 2*sideLength:
		return True
	return False

def findD(x1,x2,y1,y3,d):
	arr = []
	for i in range(min(int(x1),int(x2)),max(int(x1),int(x2))):
		for j in range(min(int(y1),int(y3)),max(int(y1),int(y3))):
			if i % d == 0 and j % d == 0:
				arr.append([i,j])
	return arr

def hasPoint(x3,y3,x4,y4,x5,y5,d):
	if y4 == y3 :
		return findD(x3,x4,y3,y5,d)
	elif y5 == y3:
		return findD(x3,x5,y3,y4,d)
	elif y4 == y5:
		return findD(x4,x5,y4,y3,d)
	else:
		return False

def kosh(x1,y1,x2,y2,status,n,d,arr):
	if status == n:
		return arr
	x3 = (x2 - x1) / 3 + x1
	y3 = (y2 - y1) / 3 + y1
	x4 = (x2 - x1) / 3 * 2 + x1
	y4 = (y2 - y1) / 3 * 2 + y1
	x5 = x3 + ((x2 - x1) - (y2 - y1) * 3 ** 0.5) / 6
	y5 = y3 + ((x2 - x1) * 3 ** 0.5 + (y2 - y1)) / 6
	if hasPoint(x3,y3,x4,y4,x5,y5,d):
		for index in hasPoint(x3,y3,x4,y4,x5,y5,d):
			# print(index)
			if isInTriangle(x3,y3,x4,y4,x5,y5,index):
				arr.append(index)
	status += 1
	kosh(x1, y1, x3, y3, status, n, d,arr)
	kosh(x3, y3, x5, y5, status, n, d,arr)
	kosh(x5, y5, x4, y4, status, n, d,arr)
	kosh(x4, y4, x2, y2, status, n, d,arr)

if __name__ == '__main__':
	x0,y0 = (0,0)
	x1,y1 = (10,0)
	x2,y2 = (5,5*3**0.5)
	d = int(input("d="))
	n = 2
	arr = []
	for index in hasPoint(x0,y0,x1,y1,x2,y2,d):
		if isInTriangle(x0,y0,x1,y1,x2,y2,index):
			arr.append(index)
	kosh(x0,y0,x2,y2,0,n,d,arr)
	kosh(x2,y2,x1,y1,0,n,d,arr)
	kosh(x1,y1,x0,y0,0,n,d,arr)
	print(len(arr))



