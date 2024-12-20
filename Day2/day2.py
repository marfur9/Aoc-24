inputfile = open('Day2/example.txt', 'r')
sum=0


for line in inputfile:
    i=0
    prev=0
    direction=""
    valid=True
    for report in line.split():
        if i==0:
            prev=report
        elif i==1:
            if report > prev:
                direction="ascending"
            elif report < prev:
                direction="descending"
        i = i + 1 
    

        

