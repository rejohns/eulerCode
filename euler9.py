"""find abc such that a^2 + b^2 = c^2 and a + b + c = 1000"""

def main():
	for i in range(1,501):
		for j in range(1,501):
			for k in range(1,501):
				if i + j + k == 1000 :
					if i * i + j * j == k * k:
						print(i)
						print(j)
						print(k)
						print(i * j * k)
				
main()