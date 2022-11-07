import pandas as pd
import csv
 
archivo=pd.read_csv('Data\Entradas\Entradas_reventa.csv', encoding='utf-8')
archivo.to_csv('Data\Entradas\Entradas_reventa2.csv', index=False, encoding="utf-8")
print(archivo)