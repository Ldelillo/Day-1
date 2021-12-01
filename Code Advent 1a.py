import os
with open('C:/Users/ldeli/Desktop/numerosProblema1.txt', 'r') as numsInput:
    list = (numsInput.read()).split("\n")
    res = 0
    for x in range(1, len(list)):
       if int(list[x]) > int(list[x-1]):
            res += 1
print(res)
