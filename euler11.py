'''What is the greatest product of four adjacent numbers in the same direction (up, down,
left, right, or diagonally) in the 20×20 grid?'''

a0  = [8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8]
a1  = [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0]
a2  = [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65]
a3  = [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91]
a4  = [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80]
a5  = [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50]
a6  = [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70]
a7  = [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21]
a8  = [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72]
a9  = [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95]
a10 = [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92]
a11 = [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57]
a12 = [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58]
a13 = [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40]
a14 = [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66]
a15 = [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69]
a16 = [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36]
a17 = [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16]
a18 = [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54]
a19 = [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]

b = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19]

 #done
def prodUp(i, j):
	if i >= 3:
		prod = b[i][j] * b[i-1][j] * b[i-2][j] * b[i-3][j]
	else:
		prod = 0
	return prod
	
def prodDown(i, j):
	if i <= 16:
		prod = b[i][j] * b[i+1][j] * b[i+2][j] * b[i+3][j]
	else:
		prod = 0
	return prod
	
def prodLeft(i, j):
	if j >= 3:
		prod = b[i][j] * b[i][j-1] * b[i][j-2] * b[i][j-3]
	else:
		prod = 0
	return prod	
	
def prodRight(i, j):
	if j <= 16:
		prod = b[i][j] * b[i][j+1] * b[i][j+2] * b[i][j+3]
	else:
		prod = 0
	return prod	
	
def prodDiagUL(i, j):
	if i >= 3 and j >= 3:
		prod = b[i][j] * b[i-1][j-1] * b[i-2][j-2] * b[i-3][j-3]
	else:
		prod = 0
	return prod	
	
def prodDiagUR(i, j):
	if i >= 3 and j <= 16:
		prod = b[i][j] * b[i-1][j+1] * b[i-2][j+2] * b[i-3][j+3]
	else:
		prod = 0
	return prod	
	
def prodDiagDL(i, j):
	if i <= 16 and j >= 3:
		prod = b[i][j] * b[i+1][j-1] * b[i+2][j-2] * b[i+3][j-3]
	else:
		prod = 0
	return prod	
	
def prodDiagDR(i, j):
	if i <= 16 and j <= 16:
		prod = b[i][j] * b[i+1][j+1] * b[i+2][j+2] * b[i+3][j+3]
	else:
		prod = 0
	return prod	

def main():
	max = 0
	
	for i in range(19):
		for j in range(19):
			if prodUp(i, j) > max:
				max = prodUp(i, j)
				
			if prodDown(i, j) > max:
				max = prodDown(i, j)	
			
			if prodLeft(i, j) > max:
				max = prodLeft(i, j)
			
			if prodRight(i, j) > max:
				max = prodRight(i, j)	
			
			if prodDiagUL(i, j) > max:
				max = prodDiagUL(i, j)		
			
			if prodDiagUR(i, j) > max:
				max = prodDiagUR(i, j)		
			
			if prodDiagDL(i, j) > max:
				max = prodDiagDL(i, j)		
			
			if prodDiagDR(i, j) > max:
				max = prodDiagDR(i, j)
				
	print(max)
	
main()