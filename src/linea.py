from src.punto import punto

class Linea:
    
    def __init__(self, p1: punto, p2: punto) -> None:
        self._punto_a = p1
        self._punto_b = p2
        
    def mueve_derecha(self, d: float) -> None:
        self._punto_a.x = self._punto_a.x + d
        self._punto_b.x = self._punto_b.x + d
    def mueve_izquierda(self, d: float) -> None:
        self._punto_a.x = self._punto_a.x - d
        self._punto_b.x = self._punto_b.x - d
    def mueve_arriba(self, d: float) -> None:
        self._punto_a.y = self._punto_a.y + d
        self._punto_b.y = self._punto_b.y + d
    def mueve_abajo(self, d: float) -> None:
        self._punto_a.y = self._punto_a.y - d
        self._punto_b.y = self._punto_b.y - d
    
    def __str__(self):
        return f"({self._punto_a.impresion()}, {self._punto_b.impresion()})"