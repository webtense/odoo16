# Fecha: 2024-12-04
# Nombre del archivo: inspeccion.py
# Versión del archivo: V2

from odoo import models, fields

class Inspeccion(models.Model):
    _name = 'btr.inspeccion'
    _description = 'Inspección'

    name = fields.Char(string="Nombre", required=True)
    fecha_inspeccion = fields.Date(string="Fecha de Inspección", required=True)
    estado = fields.Selection([
        ('proxima', 'Próxima'),
        ('pendiente', 'Pendiente'),
        ('realizada', 'Realizada')
    ], string="Estado", default='proxima', required=True)
    entidad_id = fields.Many2one('btr.entidad.inspectora', string="Entidad Inspectora", required=True)
    tipo_id = fields.Many2one('btr.tipo.inspeccion', string="Tipo de Inspección", required=True)
    attachment_ids = fields.Many2many(
        'ir.attachment',
        string="Documentos Adjuntos",
        help="Archivos relacionados con esta inspección"
    )
