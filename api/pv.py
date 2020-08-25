def pvSingleRate(amount, duration, rate):
    v = 1 / (1 + rate)
    d = rate * v
    pv = amount * ((1 - v ** (duration)) / d)
    return pv

def pv(data):
    annuity = data["annuity"]
    result = round(pvSingleRate(annuity["amount"],annuity["duration"],annuity["rate"]), 2)
    return result
