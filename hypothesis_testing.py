##Hypothesis

#Do your work for this exercise in a jupyter notebook named hypothesis_testing.ipynb.
#For each of the following questions, formulate a null and alternative hypothesis (be as specific as you can be), then give an example of what a true positive, true negative, type I and type II errors would look like.

#is the website redesign any good?
H0: web traffic did not increase after the web site design
H1: the website design did increase web traffic
Type 1: the increase in traffice can be attributed to the redesign, when it is just a natural bump in traffic
Type 2: the redesign did not increase traffice, when it was just a low traffic day

#Is our television ad driving more sales?
H1: there is no increase in sales after the ad aired
HO: there is an increase in sales after the ad aired
Type1: Sales increased bc of the ad, when it was just an increase in sales not related to the add 
Type 2:Sales did not increase bc of the ad, when it eas just low sales

#Has the network latency gone up since we switched internet service providers?
HO: There is no change in latenxcy since we switched
H1: There is an increase in network latency since we swithched

Type 1: since we switched network latency has increased, but the sample is just high
Type 2: There is no change in latency since we changed, but the sample just hsow no change


# Ace Realty wants to determine whether the average time it takes to sell homes is different for its two offices. A sample of 40 sales from office #1 revealed a mean of 90 days and a standard deviation of 15 days. A sample of 50 sales from office #2 revealed a mean of 100 days and a standard deviation of 20 days. Use a .05 level of significance.
from math import sqrt
from scipy import stats
n1 = 40
n2 = 50

s1 = 15
s2 = 20

m1 = 90
m2 = 100

degf = n1 + n2 - 2

s_p = sqrt((((n1-1) * s1**2) + ((n2-1) * s2**2))/(n1+n2-2))

standard_error = se = sqrt(s1**2 / n1 + s2**2/n2)
t = (m1-m2) /(s_p * sqrt(1/n1+1/n2))

#Correlation Test 


#3Use the sleepstudy data. Is there a relationship between days and reaction time?
ss= data("sleepstudy")
ss
plt.scatter(x= ss.Days, y= ss.Reaction)
r, p = stats.pearsonr(x, y)

#Chi Test 

#1  Use the following contingency table to help answer the question of whether using a macbook and being a codeup 
#student are independent of each other.

index = ['Use MB', 'No MB']
columns = ['Codeup', 'not Codeup']
observed = pd.DataFrame([[49, 20], [1, 30]], index=index, columns=columns)
n = observed.values.sum()
expected = pd.DataFrame([[.49, .2], [.01, .30]], index=index, columns=columns) * n
chi2 = ((observed - expected)**2 / expected).values.sum()
nrows, ncols = observed.shape

degrees_of_freedom = (nrows - 1) * (ncols - 1)

p = stats.chi2(degrees_of_freedom).sf(chi2)

print('Observed')
print(observed)
print('---\nExpected')
print(expected)
print('---\n')
print(f'chi^2 = {chi2:.4f}')
print(f'p     = {p:.4f}')

#Choose another 2 categorical variables from the mpg dataset and perform a 
c
h
i
2
contingency table test with them. Be sure to state your null and alternative hypotheses.