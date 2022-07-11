from flask import Flask
from flask import render_template 
from flask import request
from flask import url_for
from flask import json, jsonify
from flask import redirect

from Models.renta import Renta
from Models.venta import Venta

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


#*=======================================================================================
#*=======================================================================================
# ______________ Generar Contrato plan venta______________
@app.route('/planventa', methods=['GET'])
def planventa():
    # db.child("plan_Venta").push({})
    lista_registros_venta = db.child("plan_Venta").get().val()
    try:
        lista_indice_venta = lista_registros_venta.keys()
        #lista_indice_final_venta = list(lista_indice_venta )
        return render_template('planventa.html',elemento_registros_venta =  lista_registros_venta.values(),  )
    except:
        return render_template('planventa.html')

@app.route('/save_data_venta', methods=['POST'])
def save_data_venta():
    cuenta = request.form.get('cuenta')
    cuotamensual = request.form.get('cuotamensual')
    nombrecliente = request.form.get('nombrecliente')
    domicilio  = request.form.get('domicilio ')
    fecha = request.form.get('fecha')
    persona = request.form.get('persona')
    ciudad = request.form.get('ciudad')
    precio = request.form.get('precio')
    equipos = request.form.get('equipos')
    nueva_venta = Venta(cuenta, cuotamensual, nombrecliente, domicilio, fecha, persona, ciudad, precio, equipos)
    enviar_respuesta_venta = json.dumps(nueva_venta.__dict__)
    crear_formato_venta = json.loads(enviar_respuesta_venta)
    db.child("plan_Venta").push(crear_formato_venta)
    return redirect(url_for('inicio'))
#*=======================================================================================
#*=======================================================================================
# ______________ Generar Contrato plan renta ______________
@app.route('/planrenta', methods=['GET'])
def planrenta():
    # db.child("plan_Renta").push({"asfsfaf":"asfasfaf"})
    lista_registros_renta = db.child("plan_Renta").get().val()
    try:
        # lista_indice_renta = lista_registros_renta.keys()
        #lista_indice_final_renta = list(lista_indice_renta )
        return render_template('planrenta.html',elemento_registros_renta =  lista_registros_renta.values(),  )
    except:
        return render_template('planrenta.html')

@app.route('/save_data_renta', methods=['POST'])
def save_data_renta():
    cuenta = request.form.get('cuenta')
    cuotamensual = request.form.get('cuotamensual')
    nombrecliente = request.form.get('nombrecliente')
    domicilio = request.form.get('domicilio')
    fecha = request.form.get('fecha')
    persona = request.form.get('persona')
    ciudad = request.form.get('ciudad')
    precio = request.form.get('precio')
    equipos = request.form.get('equipos')
    nueva_renta = Renta(cuenta, cuotamensual, nombrecliente, domicilio, fecha, persona, ciudad, precio, equipos)
    enviar_respuesta_renta = json.dumps(nueva_renta.__dict__)
    crear_formato_renta = json.loads(enviar_respuesta_renta)
    db.child("plan_Renta").push(crear_formato_renta)
    return redirect(url_for('docrenta'))
    # return render_template('docrenta.html')

#*=======================================================================================
#*=======================================================================================
@app.route('/docrenta', methods=['GET'])
def docrenta():
    return render_template('docrenta.html')

@app.route('/docventa', methods=['GET'])
def docventa():
    return render_template('docventa.html')
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

# ______________ Facturación ______________
@app.route('/planrecibo')
def planrecibo():
    return render_template('planrecibo.html')

@app.route('/recibo', methods=['GET'])
def recibo():
    return render_template('recibo.html')

if __name__=='__main__':
    app.run(debug = True)