inputfile = open('Day1/input.txt', 'r')


list1=[]
list2=[]
sum=0
for line in inputfile:
    list1.append(int(line.split()[0]))
    list2.append(int(line.split()[1]))


for num1 in list1:
    numberOfTimes=0
    for num2 in list2:
        if num1==num2:
            numberOfTimes=numberOfTimes+1

    sum=sum+(num1*numberOfTimes)






print(sum)