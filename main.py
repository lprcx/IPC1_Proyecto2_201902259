from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from datetime import datetime
import datetime
from libro import Libro
from prestamo import Prestamo
from usuario import Usuario
app = Flask(__name__)
CORS(app)
libros = []
usuarios = []
prestamos = []
libros.append(Libro("1","fdsf","dfsd","dfsdg",3,2,1,2001,"dfs"))
usuarios.append(Usuario("1","jflll","nikl","jiji",2003,"Sistemas",201902259))
prestamos.append(Prestamo("1","1","01/04/2022","08/04/2022",1))


@app.route("/", methods=["GET"])
def inicio():
    return "Backend funcional xD", 200

@app.route("/book", methods=["POST"])
def crear_libro():
    global libros
    try:
        id = request.json["id_book"]
        titulo = request.json["book_title"]
        tipo = request.json["book_type"]
        autor = request.json["author"]
        cantidad = int(request.json["book_count"])
        disponible = int(request.json["book_available"])
        no_disponible = int(request.json["book_not_available"])
        anio = int(request.json["book_year"])
        editorial = request.json["book_editorial"]
        if verificar_libro(id)==False:
            libros.append(Libro(id, titulo, tipo, autor, cantidad, disponible, no_disponible, anio, editorial))
            return jsonify({
                "status": 200,
                "msg": "Libro agregado con exito"
            }),200
        else:
            return jsonify({
                "status": 406,
                "msg": "Error, el ID ya existe en el sistema"
            }), 406
    except:
        return jsonify({
            "status": 422,
            "msg": "No cumple con los campos requeridos para agregar el libro"
        }),422
#funcion para ver si existe el id del libro
def verificar_libro(id):
    global libros
    if len(libros)==0:
        return False
    else:
        for i in range(len(libros)):
            if id==libros[i].getId():
                return True
            else:
                return False

@app.route("/book",methods=["PUT"])
def actualizar_libro():
    global libros
    try:
        id = request.json["id_book"]
        titulo = request.json["book_title"]
        tipo = request.json["book_type"]
        autor = request.json["author"]
        cantidad = int(request.json["book_count"])
        disponible = int(request.json["book_available"])
        no_disponible = int(request.json["book_not_available"])
        anio = int(request.json["book_year"])
        editorial = request.json["book_editorial"]
        for i in range(len(libros)):
            if id==libros[i].getId():
                libros[i].setTitulo(titulo)
                libros[i].setAutor(autor)
                libros[i].setTipo(tipo)
                libros[i].setCantidad(cantidad)
                libros[i].setDisponible(disponible)
                libros[i].setNo_Disponible(no_disponible)
                libros[i].setAnio(anio)
                libros[i].setEditorial(editorial)
                return jsonify({
                "status": 200,
                "msg": "Libro actualizado con exito"
                }),200
            else:
                return jsonify({
                "status": 406,
                "msg": "Error, el ID no se encontró en el sistema"
                }), 406
    except:
        return jsonify({
            "status": 422,
            "msg": "No cumple con los campos requeridos para agregar el libro"
        }),422

@app.route("/book",methods=["GET"])
def buscar_libro():
    try:
        id = None
        titulo = None
        tipo = None
        try:
            id = request.json["id_book"]
        except:
            id = None
        try:
            titulo = request.json["book_title"]
        except:
            titulo = None
        try:
            tipo = request.json["book_type"]
        except:
            tipo = None
        if id!=None:
            for libro in libros:
                if id == libro.getId():
                    return jsonify({
                        "id_book": libro.getId(),
                        "book_title": libro.getTitulo(),
                        "book_type": libro.getTipo(),
                        "author": libro.getAutor(),
                        "book_count": libro.getCantidad(),
                        "book_available": libro.getDisponible(),
                        "book_not_available": libro.getNo_Disponible(),
                        "book_year": libro.getAnio(),
                        "book_editorial": libro.getEditorial()
                    }),200
                else:
                    return jsonify({
                    "status": 406,
                    "msg": "Error, el ID no se encontró en el sistema"
                    }), 406
        else:
            if tipo==None and titulo==None:
                return jsonify({
                    "status": 422,
                    "msg": "Error, no se encontró los datos necesarios en la petición"
                    }), 422
            elif tipo!=None:
                if titulo == None:
                    librex = []
                    for libro in libros:
                        if tipo == libro.getTipo():
                            objeto = {
                                "id_book": libro.getId(),
                                "book_title": libro.getTitulo(),
                                "book_type": libro.getTipo(),
                                "author": libro.getAutor(),
                                "book_count": libro.getCantidad(),
                                "book_available": libro.getDisponible(),
                                "book_not_available": libro.getNo_Disponible(),
                                "book_year": libro.getAnio(),
                                "book_editorial": libro.getEditorial()
                                    }
                            librex.append(objeto)
                    return jsonify(librex),200
                else:
                    librex2 = []
                    for libro in libros:
                        if tipo == libro.getTipo() and titulo==libro.getTitulo():
                            objeto = {
                                "id_book": libro.getId(),
                                "book_title": libro.getTitulo(),
                                "book_type": libro.getTipo(),
                                "author": libro.getAutor(),
                                "book_count": libro.getCantidad(),
                                "book_available": libro.getDisponible(),
                                "book_not_available": libro.getNo_Disponible(),
                                "book_year": libro.getAnio(),
                                "book_editorial": libro.getEditorial()
                                    }
                            librex2.append(objeto)
                    return jsonify(librex2),200
            elif titulo!=None:
                if tipo == None:
                    librex3 = []
                    for libro in libros:
                        if titulo == libro.getTitulo():
                            objeto = {
                                "id_book": libro.getId(),
                                "book_title": libro.getTitulo(),
                                "book_type": libro.getTipo(),
                                "author": libro.getAutor(),
                                "book_count": libro.getCantidad(),
                                "book_available": libro.getDisponible(),
                                "book_not_available": libro.getNo_Disponible(),
                                "book_year": libro.getAnio(),
                                "book_editorial": libro.getEditorial()
                                    }
                            librex3.append(objeto)
                    return jsonify(librex3),200
    except:
        return jsonify({
                    "status": 422,
                    "msg": "Error, no se pudo procesar la petición"
                    }), 422

@app.route("/user", methods=["POST"])
def agregar_usuario():
    try:
        id=request.json["id_user"]
        nombre=request.json["user_display_name"]
        nickname=request.json["user_nickname"]
        password=request.json["user_password"]
        anio=int(request.json["user_age"])
        carrera=request.json["user_career"]
        carnet=int(request.json["user_carnet"])
        if verificar_usuario(id)==False:
            usuarios.append(Usuario(id, nombre, nickname, password, anio, carrera, carnet))
            return jsonify({
                "status": 200,
                "message": "Usuario creado con éxito"
            }),200
        else:
            return jsonify({
                "status": 400,
                "message": "ID ya existente en el sistema"
            }),400
    except:
        return jsonify({
                "status": 500,
                "message": "Formato de petición invalido"
            }),500

def verificar_usuario(id):
    global usuarios
    if len(usuarios)==0:
        return False
    else:
        for i in range(len(usuarios)):
            if usuarios[i].id==id:
                return True
        return False

@app.route("/login", methods=["POST"])
def login():
    try:
        nickname=request.json["user_nickname"]
        password=request.json["user_password"]
        for i in range(len(usuarios)):
            if nickname==usuarios[i].getNickname():
                if password==usuarios[i].getPassword():
                    return jsonify({
                        "id_user":usuarios[i].getId(),
                        "user_display_name":usuarios[i].getNombre(),
                        "user_nickname":usuarios[i].getNickname(),
                        "user_password":usuarios[i].getPassword(),
                        "user_age":usuarios[i].getAnio(),
                        "user_career":usuarios[i].getCarrera(),
                        "user_carnet":usuarios[i].getCarnet()
                        }),200
                else:
                    return jsonify({
                        "status":400,
                        "msg": "Contraseña incorrecta"
                    }),400
        return jsonify({
            "status":400,
            "msg": "Usuario no encontrado"
        }),400
    except:
        return jsonify({
            "status":500,
            "msg": "Formato de petición inválido"
        }),500

@app.route("/prestamo",methods=["POST"])
def registrar_prestamo():
    try:
        idlibro = request.json["id_book"]
        idusuario = request.json["id_user"]
        fechai = datetime.datetime.utcnow().strftime('%d/%m/%Y')
        ahora = datetime.datetime.utcnow()
        fechaf = ahora + datetime.timedelta(days=7)
        fechaf = fechaf.strftime('%d/%m/%Y')
        if verificar_usuario(idusuario)==True and verificar_libro(idlibro)==True:
            if len(prestamos)==0:
                prestamos.append(Prestamo(idlibro, idusuario, fechai, fechaf, 1))
                return jsonify({
                    "id_loan": 1,
                    "id_book": retornar_libro(idlibro).getId(),
                    "book_title": retornar_libro(idlibro).getTitulo(),
                    "book_type": retornar_libro(idlibro).getTipo(),
                    "author": retornar_libro(idlibro).getAutor(),
                    "book_year": retornar_libro(idlibro).getAnio(),
                    "book_editorial": retornar_libro(idlibro).getEditorial(),
                    "loan_date": fechai,
                    "return_date": fechaf,
                    "id_user": retornar_usuario(idusuario).getId(),
                    "user_display_name": retornar_usuario(idusuario).getNombre(),
                    "user_career": retornar_usuario(idusuario).getCarrera(),
                    "user_carnet": retornar_usuario(idusuario).getCarnet()
                }),200
            else:
                prestamos.append(Prestamo(idlibro, idusuario, fechai, fechaf, prestamos[len(prestamos)-1].getId()+1))
                return jsonify({
                    "id_loan": prestamos[len(prestamos)-1].getId()+1,
                    "id_book": retornar_libro(idlibro).getId(),
                    "book_title": retornar_libro(idlibro).getTitulo(),
                    "book_type": retornar_libro(idlibro).getTipo(),
                    "author": retornar_libro(idlibro).getAutor(),
                    "book_year": retornar_libro(idlibro).getAnio(),
                    "book_editorial": retornar_libro(idlibro).getEditorial(),
                    "loan_date": fechai,
                    "return_date": fechaf,
                    "id_user": retornar_usuario(idusuario).getId(),
                    "user_display_name": retornar_usuario(idusuario).getNombre(),
                    "user_career": retornar_usuario(idusuario).getCarrera(),
                    "user_carnet": retornar_usuario(idusuario).getCarnet()
                }),200
        else:
            return jsonify({
            "status":400,
            "msg": "Datos no encontrados en el sistema"
        }),400
    except:
        return jsonify({
            "status":500,
            "msg": "Formato de petición inválido"
        }),500

def retornar_usuario(id):
    for i in range(len(usuarios)):
        if usuarios[i].getId()==id:
            return usuarios[i]

def retornar_libro(id):
    for i in range(len(libros)):
        if libros[i].getId()==id:
            return libros[i]

@app.route("/prestamo",methods=["PUT"])
def calcular_multa():
    try:
        idprestamo=request.json["id_loan"]
        for i in range(len(prestamos)):
            if idprestamo==prestamos[i].getId():
                fechasal = prestamos[i].getFechasal()
                ahora = datetime.datetime.utcnow()
                print(ahora)
                fechas=datetime.datetime.strptime(str(fechasal), '%d/%m/%Y')
                print(fechas)
                dias= ahora-fechas
                cdias=dias.total_seconds()/(3600*24)
                print(str(int(cdias)))
                if cdias>0:
                    prestamos[i].setMulta(int(cdias))
                for libro in libros:
                    for usuario in usuarios:
                        if libro.getId()==prestamos[i].getId_libro() and usuario.getId()==prestamos[i].getId_user():
                            return jsonify({
                                "id_loan":prestamos[i].getId(),
                                "book_title": libro.getTitulo(),
                                "loan_date": prestamos[i].getFechaini(),
                                "return_date": prestamos[i].getFechasal(),
                                "user_display_name": usuario.getNombre(),
                                "penalty_fee": prestamos[i].getMulta()
                            }),200            
        return jsonify({
        "status":400,
        "msg": "Datos no encontrados en el sistema"
    }),400
    except:
        return jsonify({
            "status":500,
            "msg": "Formato de petición inválido"
        }),500

@app.route("/prestamo",methods=["GET"])
def obtener_prestamo():
    try:
        idprestamo=request.json["id_loan"]
        for i in range(len(prestamos)):
            if idprestamo==prestamos[i].getId():
                for libro in libros:
                    for usuario in usuarios:
                        if libro.getId()==prestamos[i].getId_libro() and usuario.getId()==prestamos[i].getId_user():
                            return jsonify({
                                "id_loan":prestamos[i].getId(),
                                "id_book": libro.getId(),
                                "loan_date": prestamos[i].getFechaini(),
                                "return_date": prestamos[i].getFechasal(),
                                "id_user": usuario.getId()
                            }),200            
        return jsonify({
        "status":400,
        "msg": "Datos no encontrados en el sistema"
    }),400
    except:
        return jsonify({
            "status":500,
            "msg": "Formato de petición inválido"
        }),500

@app.route("/usuarios/prestamos",methods=["GET"])
def obtenerusruariosyprestamos():
    global usuarios
    global prestamos
    try:
        us=[]
        for usuario in usuarios:
            p=[]
            for prestamo in prestamos:
                if usuario.getId()==prestamo.getId_user():
                    if prestamo.getMulta==0:
                        prest={
                            "id_loan":prestamo.getId(),
                            "loan_date": prestamo.getFechaini(),
                            "return_date": prestamo.getFechasal()
                        }
                        p.append(prest)
                    else:
                        prest={
                            "id_loan":prestamo.getId(),
                            "loan_date": prestamo.getFechaini(),
                            "return_date": prestamo.getFechasal(),
                            "penalty_fee": prestamo.getMulta()
                        }
                        p.append(prest)
            user={
                "id_user":usuario.getId(),
                "user_display_name": usuario.getNombre(),
                "user_nickname": usuario.getNickname(),
                "loans": p
            }
            us.append(user)
        return jsonify(us)
    except:
        return jsonify({
            "status":500,
            "msg": "Error en la petición"
        }),500



if __name__ == "__main__":
    app.run(host="localhost", port=3000, debug=True)