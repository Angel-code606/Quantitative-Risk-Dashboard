def calculate_risk_score(age, income_stability, horizon, risk_preference):
    score = 0
    
    score += 3 if age < 30 else 2 if age < 45 else 1
    score += income_stability
    score += 3 if horizon > 10 else 2 if horizon > 5 else 1
    score += risk_preference
    
    return min(score, 10)


def map_risk_to_profile(score):
    if score <= 4:
        return "Conservative"
    elif score <= 7:
        return "Moderate"
    else:
        return "Aggressive"
