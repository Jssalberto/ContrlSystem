from flask import Flask
from flask import render_template 
from flask import request
from flask import url_for
from flask import json, jsonify
from flask import redirect

from Models.renta import Renta
from Models.venta import Venta
from Models.fastAPI import FastAPI_app
from Models.recibo import Recibo

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

    
#&===========================================RECIBO========================================================
#&===========================================RECIBO========================================================

@app.route('/documentrecibo', methods=['GET'])
def documentrecibo():
    return render_template('documentrecibo.html')

@app.route('/formrecibo', methods=['GET'])
def formrecibo():
    return render_template('formrecibo.html')

@app.route('/tableregistrorecibo', methods=["GET"])
def tableregistrorecibo():
    lista_recibo = db.child("Recibo").get().val()
    try:
        lista_indice_recibo = lista_recibo.keys()
        lista_indice_final_recibo = list(lista_indice_recibo)
        return render_template('tableregistrorecibo.html', elemento_registros_recibo=lista_recibo.values(), lista_indice_final_recibo=lista_indice_final_recibo)
    except:
        return render_template('tableregistrorecibo')

@app.route('/save_data_recibo', methods=["POST"])
def save_data_recibo():
    recibo = request.form.get('recibo')
    fechaexpedicion = request.form.get('fechaexpedicion')
    telefonocliente = request.form.get('telefonocliente')
    monto = request.form.get('monto')
    cantidadletra = request.form.get('cantidadletra')
    consepto = request.form.get('consepto')
    quienentrega = request.form.get('quienentrega')
    quienrecibe = request.form.get('quienrecibe')
    nuevo_recibo = Recibo(recibo, fechaexpedicion, telefonocliente, monto, cantidadletra, consepto, quienentrega, quienrecibe)
    enviar_respuesta_recibo = json.dumps(nuevo_recibo.__dict__)
    crear_formato_recibo = json.loads(enviar_respuesta_recibo)
    db.child("Recibo").push(crear_formato_recibo)
    return redirect(url_for('tableregistrorecibo'))


@app.route('/eliminar_registro_recibo', methods=["GET"])
def eliminar_registro_recibo():
    id = request.args.get("id")#AGREGAR SOLO ESTO
    print(id)
    db.child("Recibo").child(str(id)).remove()
    return redirect(url_for('tableregistrorecibo'))

@app.route('/imprimir_document_recibo/<id>', methods=["GET"])
def imprimir_document_recibo(id):
    lista_imprimir_recibo = db.child("Recibo").child(str(id)).get().val()
    return render_template('imprimir_document_recibo.html', lista_imprimir_recibo=lista_imprimir_recibo, id_recibo=id)

@app.route('/imprimir_registros_recibo', methods=["POST"])
def imprimir_registros_recibo():
    idrecibo=request.form.get('id')
    recibo = request.form.get('recibo')
    fechaexpedicion = request.form.get('fechaexpedicion')
    telefonocliente = request.form.get('telefonocliente')
    monto = request.form.get('monto')
    cantidadletra = request.form.get('cantidadletra')
    consepto = request.form.get('consepto')
    quienentrega = request.form.get('quienentrega')
    quienrecibe = request.form.get('quienrecibe')
    nuevo_document_impreso_recibo = Recibo(recibo, fechaexpedicion, telefonocliente, monto, cantidadletra, consepto, quienentrega, quienrecibe)
    nuevo_objeto_impreso_recibo = json.dumps(nuevo_document_impreso_recibo.__dict__)
    datos_impreso_recibo = json.loads(nuevo_objeto_impreso_recibo)
    db.child("Recibo").child(str(idrecibo)).update(datos_impreso_recibo)
    return redirect(url_for(documentrecibo))



#*============================================VENTA==============================================================
#*============================================VENTA==============================================================
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
    print(id)
    db.child("plan_Venta").child(str(id)).remove()
    return redirect(url_for('tableregistroventa'))

@app.route('/imprimir_document_venta/<id>', methods=['GET'])
def imprimir_document_venta(id):
    lista_imprimir_venta = db.child("plan_Venta").child(str(id)).get().val()
    return render_template('imprimir_document_venta.html', lista_imprimir_venta=lista_imprimir_venta, id_venta=id)

@app.route('/imprimir_registros_venta', methods=["POST"])
def imprimir_registros_venta():
    idventa=request.form.get('id')
    cuenta=request.form.get('cuenta')
    cuotamensual=request.form.get('cuotamensual')
    nombrecliente=request.form.get('nombrecliente')
    domicilio=request.form.get('domicilio')
    fecha=request.form.get('fecha')
    persona=request.form.get('persona')
    ciudad=request.form.get('ciudad')
    precio=request.form.get('precio')
    equipos=request.form.get('equipos')
    nuevo_document_impreso_venta = Venta(cuenta, cuotamensual, nombrecliente, domicilio, fecha, persona, ciudad, precio, equipos)
    nuevo_objeto_impreso_venta = json.dumps(nuevo_document_impreso_venta.__dict__)
    datos_impreso_venta = json.loads(nuevo_objeto_impreso_venta)
    db.child("plan_Venta").child(str(idventa)).update(datos_impreso_venta)
    return redirect(url_for(documentventa))
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


@app.route('/imprimir_document_renta/<id>', methods=["GET"])
def imprimir_document_renta(id):
    lista_imprimir_renta = db.child("plan_Renta").child(str(id)).get().val()
    if imprimir_document_renta == tablefinalizadosventa:
        return render_template(' tablefinalizadosventa')
    return render_template('imprimir_document_renta.html', lista_imprimir_renta=lista_imprimir_renta, id_renta=id)

@app.route('/imprimir_registros_renta', methods=["POST"])
def imprimir_registros_renta():
    idrenta=request.form.get('id')
    cuenta=request.form.get('cuenta')
    cuotamensual=request.form.get('cuotamensual')
    nombrecliente=reques.form.get('nombrecliente')
    domicilio=request.form.get('domicilio')
    fecha=request.form.get('fecha')
    persona=request.form.get('persona')
    ciudad=request.form.get('ciudad')
    precio=request.form.get('precio')
    equipos=request.form.get('equipos')
    nuevo_document_impreso = Renta(cuenta, cuotamensual, nombrecliente, domicilio, fecha, persona, ciudad, precio, equipos)
    nuevo_objeto_impreso = json.dumps(nuevo_document_impreso.__dict__)
    datos_impreso_renta = json.loads(nuevo_objeto_impreso)
    db.child("plan_Renta").child(str(idrenta)).update(datos_impreso_renta)
    return redirect(url_for('documentrenta'))
    
@app.route('/save_data_renta', methods=['POST'])
def save_data_renta():
    cuenta = request.form.get('cuenta')
    cuotamensual = request.form.get('cuotamensual')
    nombrecliente = request.form.get('nombrecliente')
    domicilio  = request.form.get('domicilio')
    tiempocontrato = request.form.get('tiempocontrato')
    tiempoiniciocontrato = request.form.get('tiempoiniciocontrato')
    tiempoterminocontrato = request.form.get('tiempoterminocontrato')
    fecha = request.form.get('fecha')
    persona = request.form.get('persona')
    ciudad = request.form.get('ciudad')
    precio = request.form.get('precio')
    equipos = request.form.get('equipos')
    
    nueva_renta = Renta(cuenta, cuotamensual, nombrecliente, domicilio, tiempocontrato, tiempoiniciocontrato, tiempoterminocontrato, fecha, persona, ciudad, precio, equipos)
    enviar_respuesta_renta = json.dumps(nueva_renta.__dict__)
    crear_formato_renta = json.loads(enviar_respuesta_renta)
    db.child("plan_Renta").push(crear_formato_renta)
    return redirect(url_for('tableregistrorenta'))

@app.route('/eliminar_registro_renta', methods=["GET"])
def eliminar_registro_renta():
    id = request.args.get("id")#AGREGAR SOLO ESTO
    db.child("plan_Renta").child(str(id)).remove()
    return redirect(url_for('tableregistrorenta'))



#&====================================== PROCESOS =================================================
#&=======================================================================================
# ______________ Contratos en Proceso ______________

@app.route('/tablependientesventa', methods=['GET'])
def tablependientesventa():
    return render_template('tablependientesventa.html')


@app.route('/tablependientesrenta', methods=['GET'])
def tablependientesrenta():
    return render_template('tablependientesrenta.html')


@app.route('/tablefinalizadosventa', methods=['GET'])
def tablefinalizadosventa():

    return render_template('tablefinalizadosventa.html')

@app.route('/tablefinalizadosrenta', methods=['GET'])
def tablefinalizadosrenta():
    return render_template('tablefinalizadosrenta.html')  

@app.route('/tablecancelados', methods=['GET'])
def tablecancelados():
    return render_template('tablecancelados.html')

# ______________ Facturación ______________



if __name__=='__main__':
    app.run(debug = True)