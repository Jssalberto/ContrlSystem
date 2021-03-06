from flask import Flask
from flask import render_template 
from flask import request
from flask import url_for
from flask import json, jsonify
from flask import redirect

from Models.renta import Renta
from Models.venta import Venta
from Models.fastAPI import FastAPI_app

import pyrebase
#CADENA DE CONEXION
config = {
 "apiKey": "AIzaSyBG41wQzOm7SsWMw7nAXz6Vd36I6m2bpdA",
  "authDomain": "systemcontrol-a3f41.firebaseapp.com",
  "databaseURL": "https://systemcontrol-a3f41-default-rtdb.firebaseio.com",
  "projectId": "systemcontrol-a3f41",
  "storageBucket": "systemcontrol-a3f41.appspot.com",
  "messagingSenderId": "576880718092",
  "appId": "1:576880718092:web:31ecd5474b6bc7c73e5929"
}
firebase=pyrebase.initialize_app(config)
db=firebase.database()

app = Flask(__name__)

# ______________ Rutas Principales ______________

@app.route('/', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/inicio', methods=['GET'])
def inicio():
    return render_template('index.html')


@app.route('/estructura', methods=['GET'])
def estructura():
    return render_template('estructura.html')

#!===========================================Formnt========================================================
#!===========================================Formnt========================================================

@app.route('/FastAPI', methods=['GET'])
def FastAPI():
    Lista_valores = db.child("plan_Venta_FastAPI").get().val()
    try:
        return render_template("FastAPI.html",Lista_valores  = Lista_valores.values())
    except:
        return render_template('FastAPI.html')

@app.route('/FormFastAPI')
def FormFastAPI():
    return render_template('FormFastAPI.html')

@app.route('/save_data_fastAPI', methods = ['POST'])
def save_data_fastAPI():
    cuenta = request.form.get('cuenta')
    fecha = request.form.get('fecha')
    edad = request.form.get('edad')
    ciudad = request.form.get('ciudad')
    nueva_venta = FastAPI_app(cuenta, fecha, edad, ciudad)
    enviar_respuesta_venta = json.dumps(nueva_venta.__dict__)
    crear_formato_venta = json.loads(enviar_respuesta_venta)
    db.child("plan_Venta_FastAPI").push(crear_formato_venta)
    return redirect(url_for('FastAPI'))

#*=======================================================================================
#*=======================================================================================

# @app.route('/tableregistrorenta', methods=['GET'])
# def tableregistrorenta():
#     return render_template('tableregistrorenta.html')

    
#!===========================================RECIBO========================================================
#!===========================================RECIBO========================================================

@app.route('/documentrecibo', methods=['GET'])
def documentrecibo():
    return render_template('documentrecibo.html')

@app.route('/formrecibo', methods=['GET'])
def formrecibo():
    return render_template('formrecibo.html')


#!============================================VENTA==============================================================
#!============================================VENTA==============================================================
@app.route('/documentventa', methods=['GET'])
def documentventa():
    return render_template('documentventa.html')

@app.route('/formplanventa', methods=['GET'])
def formplanventa():
    return render_template('formplanventa.html')

#_______registrosVenta
@app.route('/tableregistroventa', methods=['GET'])
def tableregistroventa():
    lista_registros_venta = db.child("plan_Venta").get().val()
    try:
        lista_indice_venta = lista_registros_venta.keys()
        lista_indice_final_venta = list(lista_indice_venta)
        return render_template('tableregistroventa.html', elemento_registros_venta=lista_registros_venta.values(), lista_indice_final_venta = lista_indice_final_venta)
    except:
        return render_template('tableregistroventa.html')
    

@app.route('/save_data_venta', methods=['POST'])
def save_data_venta():
    cuenta = request.form.get('cuenta')
    cuotamensual = request.form.get('cuotamensual')
    nombrecliente = request.form.get('nombrecliente')
    domicilio  = request.form.get('domicilio')
    fecha = request.form.get('fecha')
    persona = request.form.get('persona')
    ciudad = request.form.get('ciudad')
    precio = request.form.get('precio')
    equipos = request.form.get('equipos')
    
    nueva_venta = Venta(cuenta, cuotamensual, nombrecliente, domicilio, fecha, persona, ciudad, precio, equipos)
    enviar_respuesta_venta = json.dumps(nueva_venta.__dict__)
    crear_formato_venta = json.loads(enviar_respuesta_venta)
    db.child("plan_Venta").push(crear_formato_venta)
    return redirect(url_for('tableregistroventa'))

@app.route('/eliminar_registro_venta', methods=["GET"])
def eliminar_registro_venta():
    id = request.args.get("id")#AGREGAR SOLO ESTO
    db.child("plan_Venta").child(str(id)).remove()
    return redirect(url_for('tableregistroventa'))

#*==========================================RENTA===================================================================
#*==========================================RENTA===================================================================
@app.route('/formplanrenta', methods=['GET'])
def formplanrenta():
    return render_template('formplanrenta.html')

@app.route('/documentrenta', methods=['GET'])
def documentrenta():
    return render_template('documentrenta.html')

@app.route('/tableregistrorenta', methods=['GET'])
def tableregistrorenta():
    lista_registros_renta=db.child("plan_Renta").get().val()
    try:
        lista_indice_renta = lista_registros_renta.keys()                  
        lista_indice_final_renta = list(lista_indice_renta)
        return render_template('tableregistrorenta.html', registros_renta=lista_registros_renta.values(), lista_indice_final_renta=lista_indice_final_renta)
    except:
        return render_template('tableregistrorenta.html')

@app.route('/imprimir_document_renta', methods=["GET"])
def imprimir_document_renta():
    id  = request.args.get("id")
    db.child("plan_Renta").child(str(id)).get()
    return render_template('documentrenta.html')

    
@app.route('/save_data_renta', methods=['POST'])
def save_data_renta():
    cuenta = request.form.get('cuenta')
    cuotamensual = request.form.get('cuotamensual')
    nombrecliente = request.form.get('nombrecliente')
    domicilio  = request.form.get('domicilio')
    fecha = request.form.get('fecha')
    persona = request.form.get('persona')
    ciudad = request.form.get('ciudad')
    precio = request.form.get('precio')
    equipos = request.form.get('equipos')
    
    nueva_renta = Renta(cuenta, cuotamensual, nombrecliente, domicilio, fecha, persona, ciudad, precio, equipos)
    enviar_respuesta_renta = json.dumps(nueva_renta.__dict__)
    crear_formato_renta = json.loads(enviar_respuesta_renta)
    db.child("plan_Renta").push(crear_formato_renta)
    return redirect(url_for('tableregistrorenta'))

@app.route('/eliminar_registro_renta', methods=["GET"])
def eliminar_registro_renta():
    id = request.args.get("id")#AGREGAR SOLO ESTO
    db.child("plan_Renta").child(str(id)).remove()
    return redirect(url_for('tableregistrorenta'))



#*=======================================================================================
#*=======================================================================================
# ______________ Contratos Generales ______________

@app.route('/contratoGeneral', methods=['GET'])
def contratoGeneral():
    return render_template('general.html')

# ______________ Contratos en Proceso ______________

@app.route('/pendientes', methods=['GET'])
def pendientes():
    return render_template('pendiente.html')

@app.route('/finalizado', methods=['GET'])
def finalizado():
    return render_template('finalizados.html')

@app.route('/cancelados', methods=['GET'])
def cancelados():
    return render_template('cancelado.html')

# ______________ Facturaci??n ______________



if __name__=='__main__':
    app.run(debug = True)