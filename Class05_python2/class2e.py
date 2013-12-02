#!/usr/bin/env python

team = ["Braves", "Yankees", "Nationals"]
wins = [94, 95, 99]
losses = [64,67,68]
tempList = []

print team[0]
print tempList


for number in wins:
    print "Wins=%d" % number
    
for i in team:
    print "The teams %r" % i

for i in range(0,len(team)):
    print team[i]
    tempList.append(team[i]);

print tempList

    