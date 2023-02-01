#!/usr/bin/env python3
#!/usr/bin/python3

# coding: utf-8
# coding: utf8
# coding=utf-8

__author__ = 'xgqfrms'
__editor__ = 'vscode'
__version__ = '1.0.1'
__copyright__ = """
  Copyright (c) 2012-2050, xgqfrms; mailto:xgqfrms@xgqfrms.xyz
"""

"""
  /**
   *
   * @author xgqfrms
   * @license MIT
   * @copyright xgqfrms
   * @created 2022-08-17
   *
   * @description
   * @augments
   * @example
   * @link
   *
  */
"""


# print('py3 code template 🐍')

# print('人生苦短，我用拍三 🐍')

# python3 ./py3.py

author = "xgqfrms"
title = "CTO"

# 1. 字符串拼接
# print('👨🏻‍💻' + author + ' is ' + title + '🐍🇨🇳🌎')

# 2. %
# print("👨🏻‍💻 %s is %s 🐍🇨🇳🌎" %(author, title))

# 3. str.format
# print("👨🏻‍💻 {var1} is {var2} 🐍🇨🇳🌎".format(var1 = author, var2 = title))
# print("👨🏻‍💻 {author} is {title} 🐍🇨🇳🌎".format(author = author, title = title))

# 4. f
# print(f"👨🏻‍💻 {author} is {title} 🐍🇨🇳🌎")


# 5. Template
from string import Template;



template = Template('👨🏻‍💻 $author is $title 🐍🇨🇳🌎')

print(template)
# <string.Template object at 0x7ff169dc70d0>
print(template.substitute(author = author, title = title))
# 👨🏻‍💻 xgqfrms is CTO 🐍🇨🇳🌎






# name = input("input your name: ")
# print(f"your name is {name}")

# input() & multi args
# 多个参数之间通过空格分隔：xgqfrms 23
# name,age = (input("name and age: ")).split()

# 多个参数之间通过逗号分隔：xgqfrms,23
name,age = (input("name and age: ")).split(",")

# name = input("name: ")
# age = input("age: ")

print(f"your name is {name}, age is {age}")
# your name is xgqfrms, age is 23






# string to int
# i = int(input("age: "))
i = int("3")

# int to string
s = str(3)

# int to float
f = float(10)

print(i, s, f)

