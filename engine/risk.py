def check_risk(signal):
    risky_signals = ["Buy Put", "Buy Call"]
    return signal not in risky_signals