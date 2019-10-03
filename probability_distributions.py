import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy import stats
from scipy import uniform

#A bank found that the average number of cars waiting during the noon hour at a drive-up window follows a Poisson distribution with a mean of 2 cars. Make a chart of this distribution and answer these questions concerning the probability of cars waiting at the drive-up window.

waiting= stats.poisson(2)
#What is the probability that no cars drive up in the noon hour?
waiting.cdf(0)

#What is the probability that 3 or more cars come through the drive through?
waiting.sf(3)
#How likely is it that the drive through gets at least 1 car?
waiting.cdf(1)

#Grades of State University graduates are normally distributed with a mean of 3.0 and a standard deviation of .3. 
#Calculate the following:
gpa=stats.norm(3, .3)
gpa.rvs(10000).mean()
#What grade point average is required to be in the top 5% of the graduating class?
gpa.sf(.95)

#What GPA constitutes the bottom 15% of the class?
gpa.ppf(.15)

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
students.sf(0)
students.sf(2)
students.sf(5)

#You want to get lunch at La Panaderia, but notice that the line is usually very long at lunchtime. After several weeks of careful observation, you notice that the average number of people in line when your lunch break starts is normally distributed with a mean of 15 and standard deviation of 3. If it takes 2 minutes for each person to order, and 10 minutes from ordering to getting your food, what is the likelihood that you have at least 15 minutes left to eat your food before you have to go back to class? Assume you have one hour for lunch, and ignore travel time to and from La Panaderia.
people_in_line = stats.norm(15, 3)
lunch_hour= (60-15-10)//2
people_in_line.cdf(lunch_hour)

#Connect to the employees database and find the average salary of current employees, along with the standard deviation. Model the distribution of employees salaries with a normal distribution and answer the following questions:

#What percent of employees earn less than 60,000?
#What percent of employees earn more than 95,000?
#What percent of employees earn between 65,000 and 80,000?
#What do the top 5% of employees make?

salaries = pd.read_sql(query,url)
mean = salaries['salary'].mean()
std = salaries['salary'].std
salary_dist = stats.norm(mean,std)
p_under_60k = salary_dist.cdf(60_000)
p_over_95k = salary_dist.sf(95_000)
p_between_65k_and_80k = salary_dist.cdf(80_000) - salary_dist.cdf(65_000)
top_5_percent = salary_dist.isf(.05)