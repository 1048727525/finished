import numpy as np
import math
from scipy import stats

def em_single(priors, observations):
    update = {'A':{'up':0, 'down':0}, 'B':{'up':0, 'down':0}}
    theta_A = priors[0]
    theta_B = priors[1]
    for observation in observations:
        len_ob = len(observation)
        num_heads = observation.sum()
        num_tails = len_ob - num_heads
        P_i_A = stats.binom.pmf(num_heads, len_ob, theta_A)#stats.binom.pmf(k,n,0.5)计算了抛n次硬币出现k次正面的概率分布
        P_i_B = stats.binom.pmf(num_heads, len_ob, theta_B)
        P_A_i = P_i_A/(P_i_A + P_i_B)
        P_B_i = P_i_B/(P_i_A + P_i_B)
        update['A']['up'] += P_A_i * num_heads
        update['A']['down'] += num_tails * P_A_i
        update['B']['up'] += P_B_i * num_heads
        update['B']['down'] += num_tails * P_B_i
    new_theta_A = update['A']['up']/(update['A']['down'] + update['A']['up'])
    new_theta_B = update['B']['up']/(update['B']['down'] + update['B']['up'])
        #new_theta_A = update['A']['up'] / update['A']['down']
        #new_theta_B = update['B']['up'] / update['B']['down']
    return [new_theta_A, new_theta_B]

def em(observations, prior, tol=1e-6, iterations=10000):
    iteration = 0
    while iteration<iterations:
        new_prior = em_single(prior, observations)
        print([new_prior, iteration])

        delta_change = np.abs(prior[0] - new_prior[0])
        #print("delta_chang:" + str(delta_change))
        if delta_change<tol:
            break
        else:
            prior = new_prior
            iteration += 1
    return [new_prior, iteration]

if __name__ == "__main__":
    observations = np.array([[1, 0, 0, 0, 1, 1, 0, 1, 0, 1],
                             [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                             [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
                             [1, 0, 1, 0, 0, 0, 1, 1, 0, 0],
                             [0, 1, 1, 1, 0, 1, 1, 1, 0, 1]])
    print(em(observations, [0.6, 0.5]))