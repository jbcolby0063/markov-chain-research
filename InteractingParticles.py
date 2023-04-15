import time, random, math

particle_nums = 10
particle_top = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0] # 1 = occupied, 0 = empty
particle_bottom = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

def is_in_range(x): # check if index is in range
    return 0 <= x < particle_nums

def drift_prob(q, n): # drift probabilities 
    driftLeftRate = q * (q**(2*n - 1) + q**(-2*n + 1))
    driftRightRate = (1/q) * ((1/q)**(2*n - 1) + (1/q)**(-2*n + 1))
    return driftLeftRate/(driftLeftRate + driftRightRate), driftRightRate/(driftLeftRate + driftRightRate)

def drift_choice(p): # choose whether to move or not
    get_choice = random.choices([True, False], weights=(p, 1 - p), k=1)
    return get_choice[0]

def drift(t, q, n): # time (seconds), speed of drift, n
    time_end = time.time() + t
    driftLeftProb, driftRightProb = drift_prob(q, n)
    i = 0 # top particle index
    j = 0 # bottom particle index
    while time.time() < time_end:
        # top
        if particle_top[i] == 1: # if occupied
            left_i = i - 1 # left particle
            right_i = i + 1 # right particle
            moved = False 
            # visit left empty particle first
            if is_in_range(left_i) and particle_top[left_i] == 0 and drift_choice(driftLeftProb):
                particle_top[left_i] = 1
                particle_top[i] = 0
                moved = True
            # if the particle didn't move to left, visit right empty particle
            if is_in_range(right_i) and not moved and particle_top[right_i] == 0 and drift_choice(driftRightProb):
                particle_top[right_i] = 1
                particle_top[i] = 0
                moved = True
        i = (i + 1) % particle_nums # keep moving index to right
        
        # bottom
        if particle_bottom[j] == 1: # if occupied
            left_j = j - 1 # left particle
            right_j = j + 1 # right particle
            moved = False 
            # visit left empty particle first
            if is_in_range(left_j) and particle_bottom[left_j] == 0 and drift_choice(driftLeftProb):
                particle_bottom[left_j] = 1
                particle_bottom[j] = 0
                moved = True
            # if the particle didn't move to left, visit right empty particle
            if is_in_range(right_j) and not moved and particle_bottom[right_j] == 0 and drift_choice(driftRightProb):
                particle_bottom[right_j] = 1
                particle_bottom[j] = 0
                moved = True
        j = (j + 1) % particle_nums # keep moving index to right

    # print result
    print(f"After drifting particles for {t} seconds with q={q} and n={n}: ")
    print(*particle_top, sep=" ")
    print(*particle_bottom, sep=" ")

drift(5, 0.5, 3)