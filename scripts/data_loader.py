# %%
import pandas as pd
import os

# Ruta absoluta de la carpeta donde está el script (.../scripts/)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta del archivo csv de data
DATA_PATH = os.path.join(SCRIPT_DIR, '..', 'data', 'Reviews.csv')

# creacion de funcion

def cargar_datos(path):
    print(f"Cargando datos desde: {path}")
    
    try:
        df = pd.read_csv(path)
        print("Datos han sido cargados")
        return df
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en: {path}")
        print("Asegurate de tener el archivo en la carpeta 'data'")         
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None
    
    # ¿este archivo se está ejecutando directamente por el usuario o está siendo importado por otro script?
    
if __name__ == "__main__":
    # indica donde está el script actual 
    print(f"Directorio del script: {os.path.abspath(__file__)}")
    #llama a la funcion de arriba para cargar el csv
    df_reviews = cargar_datos(DATA_PATH)
    if df_reviews is not None:
        print("\n---Primeras 5 filas---")  
        print(df_reviews.head())
        
        print("\n---Información del DataFrame---")
        df_reviews.info()