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
        if verificar_libro(id)==False:
            titulo = request.json["book_title"]
            tipo = request.json["book_type"]
            autor = request.json["author"]
            cantidad = int(request.json["book_count"])
            disponible = int(request.json["book_available"])
            no_disponible = int(request.json["book_not_available"])
            anio = int(request.json["book_year"])
            editorial = request.json["book_editorial"]
            libros.append(Libro(id, titulo, tipo, autor, cantidad, disponible, no_disponible, anio, editorial))
            return jsonify({
                "status": 200,
                "msg": "Libro agregado con exito"
            })
        else:
            return jsonify({
                "status": 406,
                "msg": "Error, el ID ya existe en el sistema"
            })
    except:
        return jsonify({
            "status": 422,
            "msg": "No cumple con los campos requeridos para agregar el libro"
        })
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

if __name__ == "__main__":
    app.run(host="localhost", port=3000, debug=True)