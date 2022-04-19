class Usuario:
    def __init__(self, id, nombre, nickname, password, anio, carrera, carnet):
        self.id= id
        self.nombre = nombre
        self.nickname = nickname
        self.password = password
        self.carrera = carrera
        self.carnet = carnet
        self.anio = anio

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNickname(self):
        return self.nickname

    def setNickname(self, nickname):
        self.nickname = nickname

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password

    def getCarrera(self):
        return self.carrera

    def setCarrera(self, carrera):
        self.carrera = carrera

    def getCarnet(self):
        return self.carnet

    def setCarnet(self, carnet):
        self.carnet = carnet

    def getAnio(self):
        return self.anio

    def setAnio(self, anio):
        self.anio = anio
