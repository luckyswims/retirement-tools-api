def pvSingleRate(amount, duration, rate):
    v = 1 / (1 + rate)
    d = rate * v
    pv = amount * ((1 - v ** (duration)) / d)
    return round(pv, 2)

def pv(data):
    annuity = data["annuity"]
    result = pvSingleRate(annuity["amount"],annuity["duration"],annuity["rate"])
    return result
