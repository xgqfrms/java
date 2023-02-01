
#!/usr/bin/env python3
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
   * @created 2022-08-20
   *
   * @description
   * @augments
   * @example
   * @link
   *
  */
"""


class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return (self.name + ' ('+str(self.capacity)+'L)')
    # 改写 add
    def __add__(self, otherJuice):
        names = (self.name + '&' + otherJuice.name)
        capacities = (self.capacity + otherJuice.capacity)
        print(names, capacities)
        return Juice(names, capacities)
        # return Juice(self, names, capacities)

a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = a + b
print(result)

# class Juice:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return (self.name + ' ?')
#     # 改写 add
#     def __add__(self, otherJuice):
#         names = (self.name + '&' + otherJuice.name)
#         print(names)
#         return Juice(names)

# a = Juice('Orange')
# b = Juice('Apple')

# result = a + b
# print(result)
