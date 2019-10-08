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

#Use the following contingency table to help answer the question of whether using a macbook and being a codeup 
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