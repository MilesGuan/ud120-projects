__author__ = 'renjieguan'

# Define the neural network function y = x * w
def nn(x, w): return x*w

# Define the cost function
def cost(y, t): return ((t - y) ** 2).sum()

# define the gradient function. Remember that y = nn(x, w) = x * w
def gradient(w, x, t):
  return 2 * x * (nn(x, w) - t)

# define the update function delta w
def delta_w(w_k, x, t, learning_rate):
  return learning_rate * gradient(w_k, x, t).sum()

# Set the initial weight parameter
w = 0.1
# Set the learning rate
learning_rate = 0.1

# Start performing the gradient descent updates, and print the weights and cost:
nb_of_iterations = 4 # number of gradient descent updates
w_cost = [(w, cost(nn(x, w), t))] # List to store the weight, costs values
for i in range(nb_of_iterations):
  dw = delta_w(w, x, t, learning_rate) # Get the delta w update
  w = w - dw # Update the current weight parameter
  w_cost.append((w, cost(nn(x, w), t))) # Add weight, cost to list

# Print the final w, and cost
for i in range(0, len(w_cost)):
  print('w({}): {:.4f} \t cost: {:.4f}'.format(i, w_cost[i][0], w_cost[i][1]))
