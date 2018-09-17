import numpy as np
import matplotlib.pyplot as plt

# Using python3.6

scores = [3.0, 1.0, 0.2]

# transforms the scores into probabilities
def softmax(x):
	return np.exp(x) / np.sum(np.exp(x), axis = 0)

x = np.arange(-2.0, 6.0, 0.1)

scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])
# print("scores: ", scores)

scores_mult_10 = scores*10
scores_div_10 = scores/10

print("softmax: ", softmax(scores_div_10))

# plot a graphic
plt.plot(x, softmax(scores_div_10).T, linewidth = 2)
plt.show()