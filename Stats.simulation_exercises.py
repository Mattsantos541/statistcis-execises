##Stats.simulation_exercises

##How likely is it that you roll doubles when rolling two dice?
n_trials = nrows = 10_000
n_dice = ncols = 2
rolls1 = np.random.choice([1, 2, 3, 4, 5, 6])
rolls2 = np.random.choice([1, 2, 3, 4, 5, 6])
dice_equal= count(rolls1 = rolls2)

##If you flip 8 coins, what is the probability of getting exactly 3 heads? What is the probability of getting 
#more than 3 heads?