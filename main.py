# === imports ===
from src.punto import Punto
from src.linea import Linea

def main():
    print ("=== PRUEBA CLASE PUNTO ===")
    p1 = Punto(2, 3)
    print("punto: ", p1.impresion())
    opuesto_p1 = p1.opuesto()
    print("punto opuesto: ", opuesto_p1.impresion())
    
    print ("=== PRUEBA CLASE LINEA ===")
    p2 = Punto(4, 5)
    l1 = Linea(p1, p2)
    print("línea: ", l1.impresion())
    linea.mueve_abajo(3)
    print("línea después de mover abajo: ", l1.impresion())
    
    if __name__ == "__main__":
        main()
        