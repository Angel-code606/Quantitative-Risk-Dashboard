import numpy as np

def rebalance(current_weights, target_weights, threshold=0.05):
    deviation = np.abs(current_weights - target_weights)
    if any(deviation > threshold):
        return target_weights
    return current_weights
