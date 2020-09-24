def pvSingleRate(amount, duration, rate):
    i = ((1 + rate) ** (1/12)) - 1
    v = 1 / (1 + i)
    d = i * v
    pv = amount * ((1 - v ** (max(duration, 0))) / d)
    return pv

def deferralSingleRate(value, rate, deferral):
    i = ((1 + rate) ** (1/12)) - 1
    v = 1 / (1 + i)
    pv = value * v ** deferral
    return pv

def pvPPARates(amount, duration, rates):
    rate1 = ((1 + rates[0]) ** (1/12)) - 1
    rate2 = ((1 + rates[1]) ** (1/12)) - 1
    rate3 = ((1 + rates[2]) ** (1/12)) - 1
    v1 = 1 / (1 + rate1)
    v2 = 1 / (1 + rate2)
    pv1 = pvSingleRate(amount, min(duration, 60), rates[0])
    pv2 = pvSingleRate(amount, min(duration - 60, 180), rates[1])
    pv3 = pvSingleRate(amount, (duration - 240), rates[2])
    pv = pv1 + pv2 * (v1 ** 60) + pv3 * (v2 ** 180) * (v1 ** 60)
    return pv

def pvSingleAnnuity(annuity):
    if isinstance(annuity["rates"], list):
        result = round(pvPPARates(annuity["amount"], annuity["duration"], annuity["rates"]), 2)
    else:
        result = round(pvSingleRate(annuity["amount"], annuity["duration"], annuity["rates"]), 2)
    return result

def pv(data):
    annuities = data["annuities"]
    result = 0
    for annuity in annuities:
        result += pvSingleAnnuity(annuity)
    return result
    
