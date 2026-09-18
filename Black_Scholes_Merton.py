import numpy as np
from scipy.stats import norm

def BSM(S0, T, sigma, r, K):
    d1 = (np.log(S0/K) + (r + np.square(sigma)/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    c = S0 * norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
    print(f"N(d1) = {norm.cdf(d1)}")
    print(f"N(d2) = {norm.cdf(d2)}")
    return c

def main():
    S0 = 100 # price of the stock at t=0
    T = 0.5 # time to maturity in years
    sigma = 0.25 # annual volatility
    r = 0.10 # risk-free rate
    K = 100 # strike price  
    call_price = BSM(S0, T, sigma, r, K)
    print(f"Call option price estimated with Black-Scholes-Merton on non dividend paying stocks: {call_price}")

if __name__ == "__main__":
    main()

