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
    //--------------boton actualizar del archivo JS-------------
    // **************  IMPRIMIR DOCUMENT RENTA  **************
    //boton alerta
    //--------------boton actualizar del archivo JS-------------
    //boton alerta
    $('.imprimir').click(function () {
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

function imprimir(){
    window.print();
}
//======================================================================
//======================================================================
// FUNCION ELIMINAR MEDICOS
$(document).ready(function () {
    $('.dltBtnx').click(function (e) {
        e.preventDefault();
        var id = $(this).attr('data-id');
        var parent = $(this).parent("td").parent("tr");
        bootbox.dialog(
            {
                message: "====== ¿Estás seguro de eliminar el registro? ====",
                title: "! ============ ADVERTENCIA ============= !",
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
});
//======================================================================
//======================================================================
// FUNCION ELIMINAR ENFERMERIA
$(document).ready(function () {
    $('.dltBtny').click(function (e) {
        e.preventDefault();
        var id = $(this).attr('data-id');
        var parent = $(this).parent("td").parent("tr");
        bootbox.dialog(
            {
                message: "====== ¿Estás seguro de eliminar el registro? ====",
                title: "! ============ ADVERTENCIA ============= !",
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
                                url: '/eliminar_enfermeria',
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
});

//======================================================================
//======================================================================
// FUNCION ELIMINAR REGISTRO SENSORES
$(document).ready(function () {
    $('.dltBtnV').click(function (e) {
        e.preventDefault();
        var id = $(this).attr('data-id');
        var parent = $(this).parent("td").parent("tr");
        bootbox.dialog(
            {
                message: "====== ¿Estás seguro de eliminar el registro? ====",
                title: "! ============ ADVERTENCIA ============= !",
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
                                url: '/delete_registro_sensores',
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
});
//======================================================================
//======================================================================
// FUNCION ELIMINAR OTROS
$(document).ready(function () {
    $('.dltBtnz').click(function (e) {
        e.preventDefault();
        var id = $(this).attr('data-id');
        var parent = $(this).parent("td").parent("tr");
        bootbox.dialog(
            {
                message: "====== ¿Estás seguro de eliminar el registro? ====",
                title: "! ============ ADVERTENCIA ============= !",
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
                                url: '/eliminar_otros',
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

    //=====ACTUALIZAR REGISTROS
    //--------------boton actualizar del archivo JS-------------
    // **************  ACTUALIZAR PACIENTES  **************
    //boton alerta
    //--------------boton actualizar del archivo JS-------------
    //boton alerta
    $('.actualizar').click(function (e) {
        var id = $(this).attr('data-id');

        bootbox.confirm({
            message: "¿Desea actualizar el Registro?",
            title: "! ============ ADVERTENCIA ============= !",
            buttons: {
                confirm: {
                    label: 'Si',
                    className: "btn-outline-danger border_tem"
                },
                cancel: {
                    label: 'No',
                    className: "btn-outline-warning border_tem"
                }
            },
            callback: function (result) {
                window.location.href = "/actualizar_pacientes/" + id;
                console.log('This was logged in the callback: ' + result);
                console.log("id es:" + id)
            }
        });
    });

    //=====ACTUALIZAR REGISTROS
    //--------------boton actualizar del archivo JS-------------
    // **************  ACTUALIZAR MEDICOS  **************
    //boton alerta
    //--------------boton actualizar del archivo JS-------------
    //boton alerta
    $('.actualizarm').click(function (e) {
        var id = $(this).attr('data-id');

        bootbox.confirm({
            message: "¿Desea actualizar el Registro?",
            title: "! ============ ADVERTENCIA ============= !",
            buttons: {
                confirm: {
                    label: 'Si',
                    className: 'btn-outline-danger  border_tem'
                },
                cancel: {
                    label: 'No',
                    className: 'btn-outline-warning border_tem'
                }
            },
            callback: function (result) {
                window.location.href = "/actualizar_medicos/" + id;
                console.log('This was logged in the callback: ' + result);
                console.log("id es:" + id)
            }
        });
    });

    //=====ACTUALIZAR REGISTROS
    //--------------boton actualizar del archivo JS-------------
    // **************  ACTUALIZAR ENFERMERIA  **************
    //boton alerta
    //--------------boton actualizar del archivo JS-------------
    //boton alerta
    $('.actualizarh').click(function (e) {
        var id = $(this).attr('data-id');

        bootbox.confirm({
            message: "¿Desea actualizar el Registro?",
            title: "! ============ ADVERTENCIA ============= !",
            buttons: {
                confirm: {
                    label: 'Si',
                    className: 'btn-outline-danger border_tem'
                },
                cancel: {
                    label: 'No',
                    className: 'btn-outline-warning border_tem'
                }
            },
            callback: function (result) {
                window.location.href = "/actualizar_enfermeria/" + id;
                console.log('This was logged in the callback: ' + result);
                console.log("id es:" + id)
            }
        });
    });

    //=====ACTUALIZAR REGISTROS
    //--------------boton actualizar del archivo JS-------------
    // **************  ACTUALIZAR OTROS  **************
    //boton alerta
    //--------------boton actualizar del archivo JS-------------
    //boton alerta
    $('.actualizars').click(function (e) {
        var id = $(this).attr('data-id');

        bootbox.confirm({
            message: "¿Desea actualizar el Registro?",
            title: "! ============ ADVERTENCIA ============= !",
            buttons: {
                confirm: {
                    label: 'Si',
                    className: 'btn-outline-danger border_tem'
                },
                cancel: {
                    label: 'No',
                    className: 'btn-outline-warning border_tem'
                }
            },
            callback: function (result) {
                window.location.href = "/actualizar_otros/" + id;
                console.log('This was logged in the callback: ' + result);
                console.log("id es:" + id)
            }
        });
    });

});


//======================================================================
//======================================================================
// FUNCION USUARIOS DEL SISTEMA
$(document).ready(function () {
    $('.dltBtnk').click(function (e) {
        e.preventDefault();
        var id = $(this).attr('data-id');
        var parent = $(this).parent("td").parent("tr");
        bootbox.dialog(
            {
                message: "====== ¿Estás seguro de eliminar el registro? ====",
                title: "! ============ ADVERTENCIA ============= !",
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
                                url: '/delete_usersistem',
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
});