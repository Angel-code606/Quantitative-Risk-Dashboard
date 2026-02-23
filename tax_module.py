def tax_loss_harvesting(current_prices, purchase_prices):
    losses = {}
    for asset in current_prices:
        if current_prices[asset] < purchase_prices[asset]:
            losses[asset] = purchase_prices[asset] - current_prices[asset]
    return losses
