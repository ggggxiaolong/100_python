"""

用for循环实现1～100之间的偶数求和

Version: 0.1
Author: MrTan
Date: 2018-09-26

"""
sum = 0
for x in range(1, 101):
				 if x % 2 == 0:
								 sum += x
print(sum)
