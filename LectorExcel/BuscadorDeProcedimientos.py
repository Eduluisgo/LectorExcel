import pandas as pd

archivo = "CONTRATOS.xlsx"
hoja = "COOSALUD 2024"

df = pd.read_excel(archivo, sheet_name=hoja)

print("primero registos cargados: ")
print (df.head())

def buscarProcedimiento():
    criterio = input("¿Quieres buscar por CUPS o NOMBRE? Escribe la palabra 'CUPS' o 'NOMBRE': ").strip().lower()
    
    if criterio not in ['cups', 'nombre']:
        print("por favor, escribe 'CUPS' o 'NOMBRE'. ")
        
    ValorBuscar = input(f"introduce el {criterio} que quieres buscar: ").strip()
    
    if criterio == 'cups':
        df['CUPS'] = df ['CUPS'].astype(str).str.lower().str.strip()
        ValorBuscar = ValorBuscar.strip()
        
        resultado = df[df['CUPS'] == ValorBuscar]
    elif criterio == 'nombre':
        resultado = df[df['NOMBRE'].str.contains(ValorBuscar, case=False, na=False)]
        
    if resultado.empty:
        print(f"No se encontro el {criterio} '{ValorBuscar}' en el archivo ")
    else: 
        print (f"\nResultados encontrados para {criterio.upper()} '{ValorBuscar}':")
        print (resultado)
        
buscarProcedimiento()
    
