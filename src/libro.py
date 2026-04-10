class Libro:
    def __init__(self, titulo: str, autor: str, paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        
    def impresion(self):
        return f"'{self.titulo}' por {self.autor} ({self.paginas} páginas)"