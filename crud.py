
#intalar flask: pip install flask
from flask import Flask

app = Flask(__name__)

# Lista de usuarios en memoria para el crud
usuarios = [
    {"id": 1, "nombre": "Ana"},
    {"id": 2, "nombre": "Carlos"}
]

# GET
@app.get("/")
def ver_usuarios():
    # devolvemos la lista directamente
    return usuarios

# POST
@app.post("/add/<nombre>")
def agregar_usuario(nombre):
    # el nuevo usuario será el siguiente número en la lista
    nuevo_usuario = {
        "id": len(usuarios) + 1,
        "nombre": nombre
    }
    usuarios.append(nuevo_usuario)
    return {"mensaje": "Usuario agregado", "usuario": nuevo_usuario}

# PUT
@app.put("/update/<int:id>/<nuevo_nombre>")
def cambiar_usuario(id, nuevo_nombre):
    for u in usuarios:
        if u["id"] == id:   # encontramos al usuario
            u["nombre"] = nuevo_nombre
            return {"mensaje": "Usuario actualizado", "usuario": u}
    return {"error": "Usuario no encontrado"}

# DELETE 
@app.delete("/delete/<int:id>")
def borrar_usuario(id):
    # recorremos cada usuario de la lista
    for usuario in usuarios:
        if usuario["id"] == id:   # si el id coincide se elimina 
            usuarios.remove(usuario) 
            return {"mensaje": "Usuario eliminado", "id": id}
    
    # si no se encontró
    return {"mensaje": "Ese usuario no existe"}



# Evitar fire 
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=50000)

#GET: VER USUARIOS:
#curl.exe http://127.0.0.1:50000/

#POST: AGREGAR UN USUARIO
#curl.exe -X POST http://127.0.0.1:50000/add/Pedro


#PUT: MODIFICAR UN USUARIO POR ID
#curl.exe -X PUT http://127.0.0.1:50000/update/2/Natalia


#DELETE: ELIMINAR USUARIO POR ID
#curl.exe -X DELETE  http://127.0.0.1:50000/delete/3
