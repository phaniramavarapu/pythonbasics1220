'''
abc = [1,2,3,4,5,6]
for i in abc:
    print(i)
'''

#Square pattern
for number in range(1,6):
    for number in range(1,6):
        print(number, end="")
    print()



#Triangle Pattern

n = int(input("Enter the number of rows: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(i, end="")
    print()







