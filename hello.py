from flask import Flask

app = Flask(__name__) 

@app.route("/english") # Ruta 1 normal
def saludo():
   return "Andres mocoso!"

    

@app.route("/spanish") # Ruta 2 con o sin variable
@app.route("/spanish/<nombre>")
def saludo_español(nombre="Andres"):
   return f"Hello kitty!  {nombre}"

    #evadir fire
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=80)
