

# arr = ['a', 'b', 'c']

# s = 'b'

# # AttributeError: 'list' object has no attribute 'find'
# if(arr.find(s) > -1):
#   print(True)

# print(arr.find('x'))

ss = 'anc'
s = 'b'

if(ss.find(s) > -1):
  print(True)

print(ss.find('x'))
# -1
# print(ss.index('x'))
# ValueError: substring not found ❌

steps = list(range(0, 10, 3))
print(steps)
