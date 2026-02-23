import numpy as np
from risk_engine import calculate_risk_score, map_risk_to_profile
from optimizer import optimize_portfolio
from goal_simulation import monte_carlo_simulation
from tax_module import tax_loss_harvesting
from rebalance import rebalance
from metrics import portfolio_metrics
from data import assets, expected_returns, cov_matrix


# --- Risk Profiling ---
risk_score = calculate_risk_score(28, 3, 15, 3)
profile = map_risk_to_profile(risk_score)

print("Risk Score:", risk_score)
print("Investor Profile:", profile)


# --- Optimization ---
optimal_weights = optimize_portfolio(expected_returns, cov_matrix)

print("\nOptimal Allocation:")
for asset, weight in zip(assets, optimal_weights):
    print(f"{asset}: {round(weight*100,2)}%")


# --- Metrics ---
ret, vol, sharpe = portfolio_metrics(optimal_weights, expected_returns, cov_matrix)

print("\nExpected Return:", round(ret,4))
print("Volatility:", round(vol,4))
print("Sharpe Ratio:", round(sharpe,4))


# --- Goal Simulation ---
sim_results = monte_carlo_simulation(100000, ret, vol, 10)
probability = np.mean(sim_results > 200000)

print("\nProbability of reaching ₹200,000 goal in 10 years:", round(probability*100,2), "%")


# --- Rebalancing ---
current_weights = np.array([0.40, 0.30, 0.20, 0.10])
new_weights = rebalance(current_weights, optimal_weights)
print("\nRebalanced Portfolio:", new_weights)


# --- Tax Harvesting ---
current_prices = {"Equity": 90, "Debt": 105}
purchase_prices = {"Equity": 100, "Debt": 100}
losses = tax_loss_harvesting(current_prices, purchase_prices)

print("\nTax Loss Opportunities:", losses)
