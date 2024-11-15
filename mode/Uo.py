def corr_Uo_Beals(API,T):
    a = (10) ** (0.42 + (8.33 / API))
    uod = 0.32 + ((18 * (10 ** 7)) / API ** 4.53) * (360 / (T - 260)) ** a
    return uod