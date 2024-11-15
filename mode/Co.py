def corr_co_Standing(p,pb):
    co = (10 ** (-6)) * 2.72 * ((pb + 0.004347 * (p - pb) - 79.1) / 0.0007141 * (p - pb) - 12.398)

    return co

def corr_co_Vaszques_Beggs(Rs,T,Yg,API,p):
    co2 = (-1433 + 5 * Rs + 17.2 * (T - 460) - 1180 * Yg + 12.61 * API) / ((10 ** 5) * p)

    return co2