def corr_Rs_standing(T,Yg,API,p):
    p=float(input("Ingrese el valor de Presion: "))
    x=0.0125*API-0.00091*(T-460)
    Rs= Yg*((p/18.2)+1.4)*(10**x)**1.2048
    return Rs

def corr_Rs_Marhouns(T, Yg,API, p):
    Yo=141.5/(API+131.5)
    a=185.843208
    b=1.877840
    c=3.1437
    d=1.32657
    e=1.39844
    Rs=(a*(Yg**b)*(Yo**c)*(T**d)*p)**e
    return Rs