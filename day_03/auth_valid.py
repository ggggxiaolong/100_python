"""

身份验证

Version: 0.1
Author: MrTan
Date: 2018-09-24

"""
import getpass

username = input('请输入用户名: ')
#password = input('请输入口令:')
password = getpass.getpass('请输入口令:')

if username == 'admin' and password == '123456':
				print('身份验证成功！')
else:
				print('身份验证失败!')