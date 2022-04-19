class Libro:
    def __init__(self, id, titulo, tipo, autor, cantidad, disponible, no_disponible, anio, editorial):
        self.id= id
        self.titulo = titulo
        self.tipo = tipo
        self.autor = autor
        self.cantidad = cantidad
        self.disponible = disponible
        self.no_disponible = no_disponible
        self.anio = anio
        self.editorial = editorial

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getTitulo(self):
        return self.titulo

    def setTitulo(self, titulo):
        self.titulo = titulo

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo

    def getAutor(self):
        return self.autor

    def setAutor(self, autor):
        self.autor = autor

    def getCantidad(self):
        return self.cantidad

    def setCantidad(self, cantidad):
        self.cantidad = cantidad

    def getDisponible(self):
        return self.disponible

    def setDisponible(self, disponible):
        self.disponible = disponible

    def getNo_Disponible(self):
        return self.no_disponible

    def setNo_Disponible(self, no_disponible):
        self.no_disponible = no_disponible

    def getAnio(self):
        return self.anio

    def setAnio(self, anio):
        self.anio = anio

    def getEditorial(self):
        return self.editorial

    def setEditorial(self, editorial):
        self.editorial = editorial

    