# Fecha: 2024-12-04
# Nombre del archivo: inspeccion.py
# Versión del archivo: V1

from odoo import models, fields, api

class Inspeccion(models.Model):
    _name = 'btr.inspeccion'
    _description = 'Gestión de Inspecciones'

    name = fields.Char(string="Referencia", required=True)
    fecha_inspeccion = fields.Date(string="Fecha de Inspección", required=True)
    estado = fields.Selection([
        ('proxima', 'Próxima'),
        ('pendiente', 'Pendiente'),
        ('realizada', 'Realizada')
    ], string="Estado", default='proxima', required=True)
    entidad_id = fields.Many2one('btr.entidad.inspectora', string="Entidad Inspectora", required=True)
    tipo_id = fields.Many2one('btr.tipo.inspeccion', string="Tipo de Inspección", required=True)
    notas = fields.Text(string="Notas")
