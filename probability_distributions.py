import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy import stats
from scipy import uniform

#Grades of State University graduates are normally distributed with a mean of 3.0 and a standard deviation of .3. 
#Calculate the following:
gpa=stats.norm(3, .3)

#1What grade point average is required to be in the top 5% of the graduating class?
gpa.isf(.05)

#A marketing website has an average click-through rate of 2%. One day they observe 4326 visitors and 97 
#click-throughs. How likely is it that this many people or more click through?
clicks= stats.binom(4326, .02)
clicks.pmf(97)

#You are working on some statistics homework consisting of 100 questions where all of the answers 
#are a probability rounded to the hundreths place. Looking to save time, you put down random probabilities 
#as the answer to each question.
hw= stats.binom(100, .01)

hw.sf(.6)


#Suppose that there's a 3% chance that any one student cleans the break area when they visit it, and, on any given day, about 90% of the 3 active cohorts of 22 students visit the break area. How likely is it that the break area gets cleaned up each day? How likely is it that it goes two days without getting cleaned up? All week?

students= stats.binom(60, .03)
students.cdf(2)