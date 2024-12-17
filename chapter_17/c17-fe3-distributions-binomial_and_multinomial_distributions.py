"""
Use the binomial distribution formula to implement a function that calculates 
the probability of rolling exactly two 3's in k rolls of a fair die. Use this 
function to plot the probability as k varies from 2 to 100.
"""


import matplotlib.pyplot as plt

def fact_rec_memo(n, memo = None):
    """Assumes n is an int >= 0, memo is used only by recursive calls
    Returns n!"""
    if memo == None:
        memo = {}
    if n == 0:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = n * fact_rec_memo(n - 1)
        memo[n] = result
        return result

def binomial_dist(k, n, p):
    """k = number of successes; n = number of independent trials; 
    p = probability of a success in a single trial"""
    binomial_coefficient = fact_rec_memo(n) / (fact_rec_memo(k) * fact_rec_memo(n - k))
    return binomial_coefficient * p**k * (1 - p)**(n - k)

def make_plot(x_vals, y_vals, title, x_label, y_label, style, 
              log_x = False, log_y = False):
    plt.figure()
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(x_vals, y_vals, style)
    if log_x:
        plt.semilogx()
    if log_y:
        plt.semilogy()
        
def roll_plot(num_successes, min_rolls, max_rolls, prob_success_single_roll):
    x_axis = []
    y_axis = []
    for roll in range(min_rolls, max_rolls + 1):
        x_axis.append(roll)
    for i in x_axis:
        y_axis.append(binomial_dist(num_successes, i, prob_success_single_roll))
    title = "Probability of Rolling Exactly Two 3's of a Fair Die"
    make_plot(x_axis, y_axis, title, "Number of Rolls", "Probability", "ko")
    plt.show()

# Test
# print(binomial_dist(2, 10, 1/6)) # 0.291

roll_plot(2, 2, 100, 1/6)
