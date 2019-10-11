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

# 5 Compare Heights

#Men have an average height of 178 cm and standard deviation of 8cm.
#Women have a mean of 170, sd = 6cm.
#If a man and woman are chosen at random, P(woman taller than man)?
height_men= np.random.normal(178, 8, 10000)
height_woman= np.random.normal(170, 6, 10000)

prob_men_taller= (height_men > height_woman).mean()

prob_woman_taller

#When installing anaconda on a student's computer, there's a 1 in 250 chance that the download is corrupted and the installation fails. What are the odds that after having 50 students download anaconda, no one has an installation issue? 100 students?
corrupt= (1/250)

prob_50=(np.random.random((1000000,50)) > corrupt).prod(1).mean()
prob_50

prob_100= (np.random.random((10000,100))>corrupt).prod(1).mean()
prob_100

prob_150= 1-(np.random.random((10000,150))>corrupt).prod(1).mean()
prob_450= (np.random.random((10000,450))>corrupt).prod(1).mean()


#There's a 70% chance on any given day that there will be at least one food truck at Travis Park. However, 
#you haven't seen a food truck there in 3 days.How unlikely is this?
truck= (.7)
seeing_truck= (np.random.random((1000000,3)) > .7).prod(1).mean()
#How likely is it that a food truck will show up sometime this week?
truckanyday=1-(np.random.random((1000000,7)) > .7).prod(1).mean()

#If 23 people are in the same room, what are the odds that two of them share a birthday? What if it's 20 people? 40?
bday_23 = np.random.randint(0,365,(1000000,23))
bday_23
np.random.choice(range(365), 23)
  