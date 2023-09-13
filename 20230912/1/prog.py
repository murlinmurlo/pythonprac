sortNum = eval(input('Enter a list: '))
sortNum.sort()
res = ", ".join(str(num) for num in sortNum)
print(res)