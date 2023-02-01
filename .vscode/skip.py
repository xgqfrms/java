
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




n = int(input())

# n = 15

for x in range(1, n):
    if(x % 2 == 0):
        continue
    elif x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
    elif x % 3 == 0:
        print("Solo")
    elif x % 5 == 0:
        print("Learn")
    else:
        print(x)
