import numpy as np


# TODO: Implement the reward function as described in Gymnasium documentation.
# The end-state is always at [env_size-1,env_size-1].
def reward_function(s, env_size):
    # Initialize with 0 -- i.e. reward for all but end-state
    r = 0

    # Check if s is the end state change r to 1
    if (s == env_size -1).all():
        r = 1
    
    return r

# do not modify this function
def reward_probabilities(env_size):
    rewards = np.zeros((env_size*env_size))
    i = 0
    for r in range(env_size):
        for c in range(env_size):
            state = np.array([r,c], dtype=np.uint8)
            rewards[i] = reward_function(state, env_size)
            i+=1

    return rewards

# Check feasibility of the new state.
# If it is a possible state return s_prime, otherwise return s
def check_feasibility(s_prime, s, env_size, obstacles):
    
    # Check if s_prime inside env space
    if (s_prime >= 0).all() and (s_prime < env_size).all():
        # So it's possible to move to s_prime
        s = s_prime

    return s

def transition_probabilities(env, s, a, env_size, directions, obstacles):
    prob_next_state = np.zeros((env_size, env_size))
    # TODO
    # Fill in the cells corresponding to the next possible states with the probability of visiting each of them
    # Remember to check the feasibility of each new state!
    
    # Get s_prime in case of perpendicular action -90 degree
    s_prime = check_feasibility(s + directions[(a-1)%4], s, env_size, obstacles)
    prob_next_state[s_prime[0], s_prime[1]] = 1/3

    # Get s_prime in case of action a
    s_prime = check_feasibility(s + directions[a], s, env_size, obstacles)
    prob_next_state[s_prime[0], s_prime[1]] = 1/3

    # Get s_prime in case of perpendicular action +90 degree
    s_prime = check_feasibility(s + directions[(a+1)%4], s, env_size, obstacles)
    prob_next_state[s_prime[0], s_prime[1]] = 1/3
    return prob_next_state