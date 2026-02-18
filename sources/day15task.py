import random
Favourable = 1
Total_outcomes = 3**2 #{(Click, Click),(Click, Scroll),(Click, Exit),(Scroll, Click),(Scroll, Scroll),(Scroll, Exit),(Exit, Click),(Exit, Scroll),(Exit, Exit)}
no_click = 2**2
E_probability = no_click/Total_outcomes
print(Favourable - E_probability)


# Number of simulations
num_rolls = 1000
count_sum_7 = 0
for i in range(num_rolls):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    if die1 + die2 == 7:
        count_sum_7 += 1

experimental_probability = count_sum_7 / num_rolls
print("sum_7 probability =",experimental_probability)


#task2
p_heads = 1 / 2
p_six = 1 / 6
p_independent = p_heads * p_six
print("Theoretical probability (Heads AND 6):",round(p_independent,4))

p_first_red = 5/10
p_second_red_given_first = 4/9
p_dependent = p_first_red * p_second_red_given_first
print("Theoretical probability (Both Red):",round(p_dependent,4))

#task3


P_spam = 0.1
P_ham = 0.9
P_free_given_spam = 0.9
P_free_given_ham = 0.05
P_free = (P_free_given_spam * P_spam)+(P_free_given_ham * P_ham)
P_spam_given_free = (P_free_given_spam * P_spam) / P_free
print("P(Free) =", round(P_free, 4))
print("P(Spam | Free) =", round(P_spam_given_free, 4))

 