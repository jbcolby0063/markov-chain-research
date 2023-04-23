import time, random, math

def get_particles(n): # return initial top particles and bottom particles
    particle_top = [1] * (n // 2 + (1 if n % 2 == 1 else 0)) + [0] * (n // 2) # 1 = occupied, 0 = empty
    particle_bottom = [1] * (n // 2 + (1 if n % 2 == 1 else 0)) + [0] * (n // 2)
    return particle_top, particle_bottom

def is_in_range(x, particle_nums): # check if index is in range
    return 0 <= x < particle_nums

def drift_prob(q, n): # calculate drift probabilities 
    driftLeftRate = q * (q**(2*n - 1) + q**(-2*n + 1))
    driftRightRate = (1/q) * ((1/q)**(2*n - 1) + (1/q)**(-2*n + 1))
    return driftLeftRate/(driftLeftRate + driftRightRate), driftRightRate/(driftLeftRate + driftRightRate)

def drift_choice(p): # choose whether to move or not
    get_choice = random.choices([True, False], weights=(p, 1 - p), k=1)
    return get_choice[0]

def drift_particles(particles, particle_nums, driftLeftProb, driftRightProb, i):
    if particles[i] == 1: # if current particle is occupied
        left_i = i - 1 # left particle
        right_i = i + 1 # right particle
        moved = False 
        # visit left empty particle first
        if is_in_range(left_i, particle_nums) and particles[left_i] == 0 and drift_choice(driftLeftProb):
            particles[left_i] = 1
            particles[i] = 0
            moved = True
        # if the particle didn't move to left, visit right empty particle
        if is_in_range(right_i, particle_nums) and not moved and particles[right_i] == 0 and drift_choice(driftRightProb):
            particles[right_i] = 1
            particles[i] = 0
            moved = True

def drift(t, q, n, particle_nums): # time (seconds), speed of drift, n, number of particles
    particle_top, particle_bottom = get_particles(particle_nums)
    # print initial state
    print(f"Initial state of particles: ")
    print(*particle_top, sep=" ")
    print(*particle_bottom, sep=" ")

    time_end = time.time() + t
    driftLeftProb, driftRightProb = drift_prob(q, n)
    i = 0 # particle index
    while time.time() < time_end:
        # drift top particles
        drift_particles(particle_top, particle_nums, driftLeftProb, driftRightProb, i)
        # drift bottom particles
        drift_particles(particle_bottom, particle_nums, driftLeftProb, driftRightProb, i)
        i = (i + 1) % particle_nums # keep moving index to right

    # print result
    print(f"After drifting particles for {t} seconds with q={q} and n={n}: ")
    print(*particle_top, sep=" ")
    print(*particle_bottom, sep=" ")

drift(5, 0.7, 3, 20) # input: time (seconds), speed of drift, n, number of particles