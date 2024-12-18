inputfile = open('Day1/input.txt', 'r')
def findDifference(num1, num2):
    if num1>num2:
        return num1-num2
    elif num1<=num2:
        return num2-num1

list1=[]
list2=[]
sum=0
for line in inputfile:
    list1.append(line.split()[0])
    list2.append(line.split()[1])

list1.sort()
list2.sort()
i=0
while i < len(list1):
    sum=sum + findDifference(int(list1[i]), int(list2[i]))
    i=i+1

print(sum)