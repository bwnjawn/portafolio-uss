import sys
import os
import math

def registrar_cilindro( id_cilindro,  tipo_gas,  capacidad):
    variable_sin_usar = 'esto es un error logico'
    
    mensaje_registro = 'El cilindro de gas ' + tipo_gas + ' con el identificador unico ' + str(id_cilindro) + ' de ' + str(capacidad) + 'kg ha sido ingresado exitosamente en el registro principal.'
    
    return { 'id':id_cilindro, 'tipo':tipo_gas, 'estado': 'disponible' }