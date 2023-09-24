def getSum(n):
    
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum


n = int(input())
c = 1

if n > 0:
    for i in range(n, n + 3):
        for j in range(n, n + 3):
            if getSum(i*j) != 6 and c % 3 != 0:
                print(i, " * ", j, " = ", i*j, end = " ")
                c += 1
            elif getSum(i*j) != 6 and c % 3 == 0:
                print(i, " * ", j, " = ", i*j, end = "\n")
                c += 1
            elif getSum(i*j) == 6 and c % 3 != 0:
                print(i, " * ", j, " = :=)", end = " ")
                c += 1
            else:
                getSum(i*j) == 6 and c % 3 == 0
                print(i, " * ", j, " = :=)", end = "\n")
                c += 1
