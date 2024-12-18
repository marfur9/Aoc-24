inputfile = open('Day2/example.txt', 'r')
sum=0

prev=0
direction="unsure"
for line in inputfile:
    for report in line.split():
        if prev==0 and direction =="unsure":
            prev=report

