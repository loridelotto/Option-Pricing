from Black_Scholes_Merton import BSM
from binary_trees import tree
import matplotlib.pyplot as plt
import numpy as np

S0 = 100 # price of the stock at t=0
T = 1 # time to maturity in years
sigma = 0.2 # annual volatility
r = 0.04 # risk-free rate
K = 100 # strike price

N_values = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000]
tree_price = []
for N in N_values:
    tree_price.append(tree(S0, T, N, sigma, r, K))

BSM_price = BSM(S0, T, sigma, r, K)

# Calculate absolute error
errors = [abs(price - BSM_price) for price in tree_price]

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Convergence of option price
ax1.plot(N_values, tree_price, 'bo-', label='Binomial Tree', linewidth=2, markersize=6)
ax1.axhline(y=BSM_price, color='r', linestyle='--', label='Black-Scholes-Merton', linewidth=2)
ax1.set_xlabel('Number of Steps (N)', fontsize=12)
ax1.set_ylabel('Option Price', fontsize=12)
ax1.set_title('Convergence of Binomial Tree to Black-Scholes-Merton', fontsize=13)
ax1.set_xscale('log')
ax1.grid(True, alpha=0.3)
ax1.legend(fontsize=11)

# Plot 2: Absolute error
ax2.plot(N_values, errors, 'go-', linewidth=2, markersize=6)
ax2.set_xlabel('Number of Steps (N)', fontsize=12)
ax2.set_ylabel('Absolute Error', fontsize=12)
ax2.set_title('Approximation Error vs BSM', fontsize=13)
ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.grid(True, alpha=0.3)

plt.show()

# Print summary
print(f"Black-Scholes-Merton Price: {BSM_price:.6f}")
print(f"interation:   Value of N:   Binary Tree price:    Error:   ")

for i, N in enumerate(N_values):
    print(f"{i}   {N}   {tree_price[i]:.6f}    {np.abs((BSM_price - tree_price[i])/BSM_price *100):.4f}")
    

