def sTriangle(sideLength):
	area = (sideLength ** 2) * (3**0.5) /2
	return area

def getArea(numOfSide,area,sideLength,n):
	if n > 0:
		sideLength /= 3
		area += numOfSide * sTriangle(sideLength)
		numOfSide *= 4
		return getArea(numOfSide,area,sideLength,n-1)
	return area

if __name__ == '__main__':
	area = sTriangle(10)
	print(getArea(3,area,10,2))
