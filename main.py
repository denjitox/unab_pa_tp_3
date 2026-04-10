# === imports ===
from src.punto import Punto
from src.linea import Linea
from src.cancion import Cancion
from src.libro import Libro

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
    l1.mueve_abajo(3)
    print("línea después de mover abajo: ", l1.impresion())
    
    print ("=== PRUEBA CLASE CANCION ===")
    c1 = Cancion("Bohemian Rhapsody", "Queen", 355)
    print("canción: ", c1.impresion())
    
    print ("=== PRUEBA CLASE LIBRO ===")
    l2 = Libro("1984", "George Orwell", 328)
    print("libro: ", l2.impresion())
    l2 = Libro("1984", "George Orwell", 328)
    print("libro: ", l2.impresion())
    
if __name__ == "__main__":
    main()
        