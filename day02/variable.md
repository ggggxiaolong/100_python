"""

使用变量保存数据并进行算术运算

Version: 0.1
Author: Mrtan
Date: 2018-02-27

"""

a = 321
b = 123
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

"""

使用input函数输入
使用int()进行类型转换
用占位符格式化输出的字符串

Version: 0.1
Author: MrTan
Date: 2018-09-23

"""

a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * d))
print('%d / %d = %d' % (a, b, a / d))
print('%d // %d = %d' % (a, b, a // b))
print('%d ** %d = %d' % (a, b, a ** b))

"""

使用type()检查变量的类型

Version: 0.1
Author: Mrtan
Date: 2018-09-22

"""

a = 100
b = 12.345
c = 1 + 5j
d = 'hello'
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

"""

运算符的使用

Version: 0.1
Author: MrTan
Date: 2018-09-22

"""

a = 5
b = 10
c = 3
d = 4
e = 5
a += b
a -= c
a *= b
a /= e
print("a = ", a)

flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print("flag1 = ", flag1)
print("flag2 = ", flag2)
print("flag3 = ", flag3)
print("flag4 = ", flag4)
print("flag5 = ", flag5)
print(flag1 is True)
print(flag2 is nor Flase)

### 练习1： 华氏温度转摄氏温度
"""

将华氏温度转换为摄氏温度
F = 1.8c + 32

Version: 0.1
Author: MrTan
Date: 2018-09-22

"""

f = float(intput('请输入话是温度: '))
c = (f -32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))

练习2：输入圆的半径计算周长和面积
"""

输入半径计算圆的周长和面积

Version： 0.1
Author: MrTan
Date: 2018-09-22

"""
import math
radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.Pi * radius
area = math.Pi * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)

练习3： 输入年份判断是不是润年
"""

输入年份 如果闰年输入True 否则输出False

Version: 0.1
Author: MrTan
Date: 2018-09-22

"""

year = int(input('请输入年份： '))
# 如果代码太长写成一行不便于阅读 可以使用\或()折行
is_leap = (year % 4 == 0 and year % 100 != 0 or
           year % 400 == 0)
print(is_leap)

