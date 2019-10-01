##Stats.simulation_exercises

## 1How likely is it that you roll doubles when rolling two dice?
n_trials = nrows = 10_000
n_dice = ncols = 2
rolls1 = np.random.choice([1, 2, 3, 4, 5, 6])
rolls2 = np.random.choice([1, 2, 3, 4, 5, 6])
dice_equal= count(rolls1 = rolls2)

## 2 If you flip 8 coins, what is the probability of getting exactly 3 heads? What is the probability of getting 
#more than 3 heads?
import random
def coin_trial():
    heads = 0
    for i in range(100):
        if random.random() <= 0.5:
            heads +=1
            return heads
def simulate(n):
    trials = []
    for i in range(n):
        trials.append(coin_trial())
        return(sum(trials)/n)

# 3There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup. Assuming that Codeup randomly selects an alumni to put on a billboard, what are the odds that the two billboards I drive past both have data science students on them?
import numpy as np
billboards = np.random.random((1000000,2))
prob_2_DS= (billboards<= .25).prod(1).mean()
prob_2_DS

#4 Codeup students buy, on average, 3 poptart packages (+- 1.5) a day from the snack vending machine. If on monday the machine is restocked with 17 poptart packages, how likely is it that I will be able to buy some poptarts on Friday afternoon?
poptarts= np.random.normal(3, 1.5, (1000, 5))
probability_friday = (poptarts.sum(1)<=16).mean()
probability_friday