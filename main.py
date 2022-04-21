from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from libro import Libro
from prestamo import Prestamo
from usuario import Usuario
app = Flask(__name__)
CORS(app)
libros = []
usuarios = []

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
if __name__ == "__main__":
    app.run(host="localhost", port=3000, debug=True)