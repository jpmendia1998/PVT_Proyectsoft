def corr_Pb_standing(T,API,Rs,Yg):
    a=0.00091*(T-460)-0.0125*(API)
    Pb=18.2*(((Rs/Yg)**0.83)*(10)**a-1.4)

    return Pb

def corr_Pb_Marhoun(T, API, Rs, Yg):
    A=5.38088*(10**-3)
    B=0.715082
    C=-1.87784
    D=3.1437
    E=1.32657
    Yo= 141.5/(API+131.5)
    Pb=A*(Rs**B)*(Yg**C)*(Yo**D)*(T**E)

    return Pb
