class Cancion:
    def __init__(self, titulo: str, artista: str, duracion: int):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion  # en segundos
        
    def impresion(self):
        minutos = self.duracion // 60
        segundos = self.duracion % 60
        return f"'{self.titulo}' de {self.artista} ({minutos}:{segundos:02d})"