import matplotlib.pyplot as plt
import numpy as np

def run_backtest(ticker, strategy_name):
    np.random.seed(42)
    price = np.cumsum(np.random.randn(100)) + 100
    fig, ax = plt.subplots()
    ax.plot(price)
    ax.set_title(f"{ticker} Strategy: {strategy_name}")
    return fig