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