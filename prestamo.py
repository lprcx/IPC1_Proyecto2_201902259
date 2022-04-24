


class Prestamo:
    def __init__(self, id_libro, id_user, fechaini, fechasal, id):
        self.id_libro = id_libro
        self.id_user = id_user
        self.fechaini = fechaini
        self.fechasal = fechasal
        self.id = id
        self.multa= 0

    def getId_libro(self):
        return self.id_libro

    def setId_libro(self, id_libro):
        self.id_libro = id_libro

    def getId_user(self):
        return self.id_user

    def setId_user(self, id_user):
        self.id_user = id_user
    
    def getFechaini(self):
        return self.fechaini

    def setFechaini(self, fechaini):
        self.fechaini = fechaini

    def getFechasal(self):
        return self.fechasal

    def setFechasal(self, fechasal):
        self.fechasal = fechasal

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getMulta(self):
        return self.multa

    def setMulta(self, multa):
        self.multa = multa
