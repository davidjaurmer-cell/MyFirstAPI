
#intalar flask: pip install flask
from flask import Flask

app = Flask(__name__)

# Lista de usuarios en memoria para el crud
usuarios = [
    {"id": 1, "nombre": "Ana"},
    {"id": 2, "nombre": "Carlos"}
]

# GET 
#aqui
@app.get("/")
def obtener_usuarios():
    return str(usuarios)   # devolvemos como string

# POST → Agregar un usuario (simulación, sin body)
@app.post("/add/<nombre>")
def agregar_usuario(nombre):
    nuevo = {
        "id": len(usuarios) + 1,
        "nombre": nombre
    }
    usuarios.append(nuevo)
    return f"Usuario agregado: {nuevo}"

# PUT → Modificar un usuario por id (simulación)
@app.put("/update/<int:id>/<nuevo_nombre>")
def modificar_usuario(id, nuevo_nombre):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuario["nombre"] = nuevo_nombre
            return f"Usuario actualizado: {usuario}"
    return "Usuario no encontrado"

# DELETE → Eliminar un usuario por id
@app.delete("/delete/<int:id>")
def eliminar_usuario(id):
    global usuarios
    usuarios = [u for u in usuarios if u["id"] != id]
    return f"Usuario con id {id} eliminado"

# Evitar fire 
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=50000)

#GET: VER USUARIOS:
#http://localhost:5000/

#POST: AGREGAR UN USUARIO
#http://localhost:5000/

#PUT: MODIFICAR UN USUARIO POR ID
#http://localhost:5000/update/1/Luis

#DELETE: ELIMINAR USUARIO POR ID
#http://localhost:5000/delete/2
