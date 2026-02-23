import numpy as np

def portfolio_metrics(weights, returns, cov_matrix):
    portfolio_return = np.dot(weights, returns)
    portfolio_vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    sharpe_ratio = portfolio_return / portfolio_vol
    return portfolio_return, portfolio_vol, sharpe_ratio
