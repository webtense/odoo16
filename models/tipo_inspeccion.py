# Fecha: 2024-12-04
# Nombre del archivo: tipo_inspeccion.py
# Versión del archivo: V2

from odoo import models, fields

class TipoInspeccion(models.Model):
    _name = 'btr.tipo.inspeccion'
    _description = 'Tipo de Inspección'

    name = fields.Char(string="Nombre del Tipo", required=True)
    description = fields.Text(string="Descripción", help="Detalles adicionales sobre el tipo de inspección.")
