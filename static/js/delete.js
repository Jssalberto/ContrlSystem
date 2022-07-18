// FUNCION ELIMINAR VENTA
$(document).ready(function () {
    $('.dltBtnv').click(function (e) {
        e.preventDefault();
        var id = $(this).attr('data-id');
        var parent = $(this).parent("td").parent("tr");
        bootbox.dialog(
            {
                message: "=== ¿Estás seguro de eliminar el registro? ===",
                title: "! ==== ADVERTENCIA == !",
                buttons: {
                    cancel: {
                        label: "No",
                        className: "btn-outline-success border_tem",
                        callback: function () {
                            $('.bootbox').modal('hide');
                        }
                    },
                    confirm: {
                        label: "Delete",
                        className: "btn-outline-danger border_tem",
                        callback: function () {
                            $.ajax({
                                url: '/eliminar_registro_venta',
                                data: { id: id }
                            })
                                //Si todo ha ido bien...
                                .done(function (response) {
                                    parent.fadeOut('slow'); //Borra la fila afectada 
                                    // bootbox.alert('Algo ha ido mal. No se ha podido completar la acción.');
                                })
                        }
                    }
                }
            });
    });

    //=====IMPRIMIR REGISTROS
    //--------------boton IMPRIMIR del archivo JS-------------
    // **************  IMPRIMIR DOCUMENT VENTA  **************
    //boton alerta
    //--------------boton IMPRIMIR del archivo JS-------------
    //boton alerta
    $('.imprimir_venta').click(function () {
        var id = $(this).attr('data-id');

        bootbox.confirm({
            message: "¿Desea Imprimir el Registro?",
            // title: "! ==== WARNING==== !",
            buttons: {
                confirm: {
                    label: 'Si',
                    className: "btn-outline-danger border_tem"
                },
                cancel: {
                    label: "No",
                    className: "btn-outline-success border_tem",
                    callback: function () {
                        $('.bootbox').modal('hide');
                    }
                }
            },
            callback: function (result) {
                window.location.href = "/imprimir_document_venta/" + id;
                console.log('This was logged in the callback: ' + result);
                console.log("id es:" + id)
            }
        });
    });

});

function imprimir(){
    window.print();
}
//&======================================================================
//&======================================================================
// FUNCION ELIMINAR RENTA
$(document).ready(function () {
    $('.dltBtnx').click(function (e) {
        e.preventDefault();
        var id = $(this).attr('data-id');
        var parent = $(this).parent("td").parent("tr");
        bootbox.dialog(
            {
                message: "===== Estás seguro de eliminar el registro? ====",
                title: "! ====== ADVERTENCIA ===== !",
                buttons: {
                    cancel: {
                        label: "No",
                        className: "btn-outline-success border_tem",
                        callback: function () {
                            $('.bootbox').modal('hide');
                        }
                    },
                    confirm: {
                        label: "Si",
                        className: "btn-outline-danger border_tem",
                        callback: function () {
                            $.ajax({
                                url: '/eliminar_registro_renta',
                                data: { id: id }
                            })
                                //Si todo ha ido bien...
                                .done(function (response) {
                                    parent.fadeOut('slow'); //Borra la fila afectada
                                })
                                .fail(function () {
                                    //bootbox.alert('Algo ha ido mal. No se ha podido completar la acción.');
                                })
                        }
                    }
                }
            });
    });

    //=====IMPRIMIR REGISTROS
    //--------------boton IMPRIMIR del archivo JS-------------
    // **************  IMPRIMIR DOCUMENT RENTA  **************
    //boton alerta
    //--------------boton IMPRIMIR del archivo JS-------------
    //boton alerta
    $('.imprimir_renta').click(function () {
        var id = $(this).attr('data-id');

        bootbox.confirm({
            message: "¿Desea Imprimir el Registro?",
            // title: "! ==== WARNING==== !",
            buttons: {
                confirm: {
                    label: 'Si',
                    className: "btn-outline-danger border_tem"
                },
                cancel: {
                    label: "No",
                    className: "btn-outline-success border_tem",
                    callback: function () {
                        $('.bootbox').modal('hide');
                    }
                }
            },
            callback: function (result) {
                window.location.href = "/imprimir_document_renta/" + id;
                console.log('This was logged in the callback: ' + result);
                console.log("id es:" + id)
            }
        });
    });
});
//&======================================================================
//&======================================================================
    // **************  IMPRIMIR DOCUMENT RECIBO  **************
// FUNCION ELIMINAR REGISTRO RECIBO
$(document).ready(function () {
    $('.dltBtnh').click(function (e) {
        e.preventDefault();
        var id = $(this).attr('data-id');
        var parent = $(this).parent("td").parent("tr");
        bootbox.dialog(
            {
                message: "===== Estás seguro de eliminar el registro? ====",
                title: "! ====== ADVERTENCIA ===== !",
                buttons: {
                    cancel: {
                        label: "No",
                        className: "btn-outline-success border_tem",
                        callback: function () {
                            $('.bootbox').modal('hide');
                        }
                    },
                    confirm: {
                        label: "Si",
                        className: "btn-outline-danger border_tem",
                        callback: function () {
                            $.ajax({
                                url: '/eliminar_registro_recibo',
                                data: { id: id }
                            })
                                //Si todo ha ido bien...
                                .done(function (response) {
                                    parent.fadeOut('slow'); //Borra la fila afectada
                                })
                                .fail(function () {
                                    //bootbox.alert('Algo ha ido mal. No se ha podido completar la acción.');
                                })
                        }
                    }
                }
            });
    });

    //=====IMPRIMIR REGISTROS
    //--------------boton IMPRIMIR del archivo JS-------------
    // **************  IMPRIMIR DOCUMENT RECIBO **************
    //boton alerta
    //--------------boton actualizar del archivo JS-------------
    //boton alerta
    $('.imprimir_recibo').click(function () {
        var id = $(this).attr('data-id');

        bootbox.confirm({
            message: "¿Desea Imprimir el Registro?",
            // title: "! ==== WARNING==== !",
            buttons: {
                confirm: {
                    label: 'Si',
                    className: "btn-outline-danger border_tem"
                },
                cancel: {
                    label: "No",
                    className: "btn-outline-success border_tem",
                    callback: function () {
                        $('.bootbox').modal('hide');
                    }
                }
            },
            callback: function (result) {
                window.location.href = "/imprimir_document_recibo/" + id;
                console.log('This was logged in the callback: ' + result);
                console.log("id es:" + id)
            }
        });
    });
});