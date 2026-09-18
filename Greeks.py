import numpy as np
from scipy.stats import norm

def Greeks_c(S0, T, sigma, r, q, K, n):
    d1 = (np.log(S0/K) + (r - q + np.square(sigma)/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    Nd1 = norm.cdf(d1)
    Nd2 = norm.cdf(d2)
    Phi1 = norm.pdf(d1)
    disc = np.exp(-q * T)

    Delta = disc * Nd1 
    Gamma = (Phi1 * disc)/(S0 * sigma * np.sqrt(T)) 
    Theta_annual = (- S0 * Phi1 * sigma * disc)/(2*np.sqrt(T)) + q * S0 * Nd1 * disc - r * K * np.exp(-r*T) * Nd2 
    Theta = Theta_annual/365
    Vega = S0 * np.sqrt(T) * Phi1 * disc
    Rho = K * T * np.exp(-r*T) * Nd2
    Rho_f = - T * disc *S0 * Nd1

    return Delta*n, Gamma*n, Theta*n, Vega*n, Rho*n, Rho_f*n

def main():
    S0 = 0.8 # price of the stock at t=0
    T = 7/12 # time to maturity in years
    sigma = 0.15 # annual volatility
    r = 0.08 # risk-free rate
    q = 0.05
    K = 0.81 # strike price  
    n = -1000
    Greeks_call = Greeks_c(S0, T, sigma, r, q, K, n)
    print(f"Delta = {Greeks_call[0]}")
    print(f"Gamma = {Greeks_call[1]}")
    print(f"Theta = {Greeks_call[2]}")
    print(f"Vega = {Greeks_call[3]}")
    print(f"Rho = {Greeks_call[4]}")
    print(f"Foreign Rho = {Greeks_call[5]}")

if __name__ == "__main__":
    main()

