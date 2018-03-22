import numpy as np
import matplotlib.pyplot as plt

scores = [3.0, 1.0, 0.2]

# transforms the scores into probabilities
def softmax(x):
	return np.exp(x) / np.sum(np.exp(x), axis = 0)

x = np.arange(-2.0, 6.0, 0.1)
print "x: ", x

scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])
print "np.ones_like(x): ", np.ones_like(x)
print "scores: ", scores

# plot a graphic
plt.plot(x, softmax(scores).T, linewidth = 2)
plt.show()