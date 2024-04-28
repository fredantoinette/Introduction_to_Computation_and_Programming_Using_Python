"""
The Empire State Building is 102 stories high. A man wanted to know the 
highest floor from which he could drop an egg without the egg breaking. He 
proposed to drop an egg from the top floor. If it broke, he would go down a 
floor, and try it again. He would do this until the egg did not break. At 
worst, this method requires 102 eggs. Implement a method that at worst uses 
seven eggs.
"""

for i in range(1,103):
    low = 0 # so actual floor = 1 is possible
    high = 102
    num_eggs = 1 # we use at least 1 egg to do the experiment
    ans = round((high + low) / 2) # floor number should be a whole number
    while round(ans) != i: # when expected floor != actual floor
        #print('low =', low, 'high =', high, 'ans =', ans)
        if round(ans) < i: # if expected floor < actual floor
            low = round(ans)
        else: # if expected floor > actual floor
            high = round(ans)
            num_eggs += 1 # if the egg breaks, we need to use a new egg
        ans = round((high + low) / 2)
    if i != round(ans) or num_eggs > 7:
        print('expected floor =', i)
        print('incorrect floor =', round(ans))
        print('incorrect number of eggs used =', num_eggs)
        print('----------')
    else:
        print('expected floor =', i)
        print('actual floor =', round(ans))
        print('number of eggs used =', num_eggs)
        print('----------')
