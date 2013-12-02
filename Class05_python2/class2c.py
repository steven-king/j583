#!/usr/bin/env python

from sys import argv

script, apples, oranges, bananas = argv

apples = int(apples)
oranges = int(oranges)
banans = int(bananas)


if apples < oranges:
    print "There are more oranges than apples."
elif apples == 100:
        print "There are excatlly 100 apples and that is more than there are oranges"

if bananas > apples:
    print "There are more bananas than apples."
else:
    print "Failed"
    
if apples == 10:
    print 'There are 10 apples.'

if apples <= 10:
    print 'There are not more than 10 apples.'
    
if apples >= 10:
    print 'There are atleast 10 apples.'


    
    
    