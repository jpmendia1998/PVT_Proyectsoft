import Controller.develop as develop
import mode.aleatorio as aleatorio

DATOS="Datos"

#Nombres de columnas
RS_STANDING="Rs_Standing"
RS_MARHOUNS="Rs_Marhouns"
BO_STANDING="Bo_Standing"
BO_MARHOUNS="Bo_Marhouns"
UO_BEALS="Uo_Beals"
PO_STANDING="Po_Standing"
PO_CORRE_LAB="Po_corre_lab"
CO_STANDING="Co_Standing"
CO_VAZQUES="Co_Vazques"

DET_RS_STANDING="det_Rs_Standing"
DET_RS_MARHOUNS="det_Rs_Marhouns"
DET_BO_STANDING="det_Bo_Standing"
DET_BO_MARHOUNS="det_Bo_Marhouns"
DET_UO_BEALS="det_Uo_Beals"
DET_PO_STANDING="det_Po_Standing"
DET_PO_CORRE_LAB="det_Po_corre_lab"
DET_CO_STANDING="det_Co_Standing"
DET_CO_VAZQUES="det_Co_Vazques"

if __name__ == '__main__':
    df = aleatorio.generate_data_with_scipy(20)
    develop.exportar_a_excel(df)