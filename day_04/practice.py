"""

输入两个整数计算最大公约数和最小公倍数

Version: 0.1
Author: MrTan
Date: 2018-09-26

"""

x = int(input('x = '))
y = int(input('y = '))
if x > y:
				(x, y) = (y, x)
for factor in range(x, 0, -1):
				if x % factor == 0 and y % factor == 0:
								print('%d和%d的最大公约数是%d' % (x, y, factor))
								print('%d和%d的最大公约数是%d' % (x, y , x * y // factor))
								break
