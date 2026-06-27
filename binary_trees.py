#import region
import numpy as np

S0 = 100 # price of the stock at t=0
T = 1 # time to maturity in years
N = 100 # number of nodes
sigma = 0.2 # annual volatility
r = 0.04 # risk-free rate
K = 100 # strike price

def payoff(S, K):
    return np.maximum(S-K,0)

def tree(S0, T, N, sigma, r, K):
    dt = T/N # time step
    u = np.exp(sigma * np.sqrt(dt)) # increase percentage
    d = np.exp(-sigma*np.sqrt(dt)) # decrease percentage
    disc = np.exp(-r * dt) # discount factor
    p = (np.exp(r * dt) - d)/(u -d) # risk neutral probability of up movement
    stock_tree = []

    for i in range(N+1): # iterating over steps
        step_prices = []
        for j in range(i+1): # iterating over nodes
            S_ij = S0 * (u**j) *(d**(i-j))
            step_prices.append(S_ij)
        stock_tree.append(step_prices)

    option_tree = [payoff(np.array(stock_tree[N]), K).tolist()]

    for i in reversed(range(N)):
        step_option_values = []
        for j in range(i+1):
            f_up = option_tree[0][j+1]
            f_down = option_tree[0][j]
            f_ij = disc * (p * f_up + (1 - p) * f_down)
            step_option_values.append(f_ij)
        # Insert at the beginning of our option tree list
        option_tree.insert(0, step_option_values)

    return option_tree[0][0]

def main():

    call_price = tree(S0, T, N, sigma, r, K)
    print(f"\nFair Option Price at t=0: {call_price:.4f}")

if __name__ == "__main__":
    main()
