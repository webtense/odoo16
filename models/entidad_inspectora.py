# Fecha: 2024-12-04
# Nombre del archivo: entidad_inspectora.py
# Versión del archivo: V1

from odoo import models, fields

class EntidadInspectora(models.Model):
    _name = 'btr.entidad.inspectora'
    _description = 'Entidad Inspectora'

    name = fields.Char(string="Nombre", required=True)
    contacto = fields.Char(string="Contacto")
    correo = fields.Char(string="Correo Electrónico")
    telefono = fields.Char(string="Teléfono")
