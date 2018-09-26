"""

输出乘法口诀表(九九表)

Version: 0.1
Author: MrTan
Date: 2018-09-26

"""

for i in range(1, 10):
				for j in range(1, i + 1):
								print("%d * %d = %d" % (i, j, i * j), end='\t')
				print()
