import numpy as np

# Markov chains

# initial distribution (P(s0), P(s1))
v = np.array([[1.0, 0.0]])

# Transition matrix T = [[P(s0|s0), P(s1|s0)]; [P(s0|s1), P(s0|s0)]]
T = np.array([[0.90, 0.10],
              [0.50, 0.50]])

# T after three steps
T_3 = np.linalg.matrix_power(T, 3)
# T after 50 steps
T_50 = np.linalg.matrix_power(T, 50)
# T after 100 steps
T_100 = np.linalg.matrix_power(T, 100)

# printing the matrices
print("v: " + str(v))
print("v_1: " + str(np.dot(v, T)))
print("v_3: " + str(np.dot(v, T_3)))
print("v_50: " + str(np.dot(v, T_50)))
print("v_100: " + str(np.dot(v, T_100)))
