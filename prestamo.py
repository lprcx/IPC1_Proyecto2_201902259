from libro import Libro


class Prestamo:
    def __init__(self, id_libro, id_user):
        self.id_libro = id_libro
        self.id_user = id_user

    def getId_libro(self):
        return self.id_libro

    def setId_libro(self, id_libro):
        self.id_libro = id_libro

    def getId_user(self):
        return self.id_user

    def setId_user(self, id_user):
        self.id_user = id_user