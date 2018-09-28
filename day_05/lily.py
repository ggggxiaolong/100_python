"""

找出100～999之间的所有水仙花数
水仙花数是各位立方等于这个数本身的数

Version: 0.1
Author: MrTan
Date: 2018-09-27

"""

for i in range(101, 1000):
				high = i // 100
				mid = i // 10 % 10
				low = i % 10
				if i == high ** 3 + mid ** 3 + low ** 3:
								print(i)
