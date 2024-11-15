def corr_dens_standing(T,Rs,API,Yg):
    Yo=141.5/(API+131.5)
    po=(62.4*Yo+0.0136*Rs*Yg)/(0.972+0.000147*(Rs*(Yg/Yo)**0.5+1.25(T-460))**1.175)

    return po

def corr_dens( bo,Rs,API, Yg):
    Yo=141.5/(API+131.5)
    po2 = (62, 4 * Yo + 0.0136 * Rs * Yg) / bo

    return po2