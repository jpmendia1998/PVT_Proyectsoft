import Controller.develop as develop
import mode.aleatorio as aleatorio

if __name__ == '__main__':
    df = aleatorio.generate_data_with_scipy(20)
    develop.exportar_a_excel(df)