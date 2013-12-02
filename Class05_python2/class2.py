#!/usr/bin/env python
from __future__ import division

age = raw_input("How old are you? ")
height = raw_input("How tall are you in inches? ")
weight = raw_input("How much do you weigh? ")

height = int(height)
weight = int(weight)

#BMI FORUMLA = ( Weight in Pounds / ( Height in inches x Height in inches ) ) x 703
bmi = round((weight / height**2) * 703)

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)








#BMI FORUMLA = ( Weight in Pounds / ( Height in inches x Height in inches ) ) x 703
bmi = round((weight / height**2) * 703)


#Your BMI is %r." , bmi