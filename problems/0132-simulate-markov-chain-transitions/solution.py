import numpy as np

def simulate_markov_chain(transition_matrix, initial_state, num_steps):
    # Your code here

    #for each step starting from init initial_state
    #multiply the row with matrix 
    states = [initial_state]
    current_state = initial_state
    for _ in range(num_steps):
        row = transition_matrix[current_state]
        next_state = np.random.choice(len(row), p=row)
        states.append(next_state)
        current_state = next_state

    return np.array(states)


    

