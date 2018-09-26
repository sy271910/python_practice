# -*- coding: UTF-8 -
# ^	匹配字符串的开头
# $	匹配字符串的末尾。
# .	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
# [...]	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
# [^...]	不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
# *	匹配0个或多个的表达式。
# +	匹配1个或多个的表达式。
# ?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式   贪婪模式是指匹配尽可能长的字符串

import re

aa = '蚂蚁1：储存食321物以防冬665人类555令 蚂蚁2：储反倒是存食物以防冬人类41412341242139113212121995令'
a1 = re.findall(r'(\d+)', aa)[1]
a2 = re.findall(r'食(\d+)', aa)[0]
a3 = re.findall(r'蚂蚁2：.*?(\d+)', aa)[0]

print (re.match('abc','abcdef').group())
print ("".join(re.findall('[^蚂蚁\d]',aa)))

print(a1)
print(a2)
print(a3)

phone = "2004-959-559 #888这是一个电话号码#999"
print( re.sub(r'#\d*$', "", phone))

movieId="http://www.cbooo.cn/m/642989"
print(re.findall(r'(\d+)',movieId)[0])

print(re.split(r'\s+', 'a b   c'))
