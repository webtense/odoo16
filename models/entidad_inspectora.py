from odoo import models, fields

class EntidadInspectora(models.Model):
    _name = 'btr.entidad.inspectora'
    _description = 'Entidad Inspectora'

    name = fields.Char(string="Nombre", required=True)
    contacto = fields.Char(string="Contacto")
    correo = fields.Char(string="Correo Electrónico")
    telefono = fields.Char(string="Teléfono")
