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