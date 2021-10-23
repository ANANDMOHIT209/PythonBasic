num=[1,2,3,45,5]
print(num)
print(num[3])
print(num[2:])
name=['shailee','mohit','sneha']
mill=[num,name]
print(mill)

num.append(49)     #to insert a element at last
print(num)
num.insert(2,56)     #to insert a element at certain index
print(num)
num.remove(49)     #to delete certain element
print(num)
num.pop(4)     #to delete certain index element
print(num)
num.pop()     #to delete last element
print(num)
del num[2:]   #to delete multiple element
print(num)
num.extend([73,48,85,63])
print(num)

print(min(num))
print(max(num))
num.sort()
print(num)

