# Fecha: 2024-12-04
# Nombre del archivo: inspeccion.py
# Versión del archivo: V3

from odoo import models, fields, api
from datetime import datetime

class Inspeccion(models.Model):
    _name = 'btr.inspeccion'
    _description = 'Inspección'

    name = fields.Char(string="Nombre", required=True)
    fecha_inspeccion = fields.Date(string="Fecha de Inspección", required=True, default=fields.Date.today)
    estado = fields.Selection([
        ('proxima', 'Próxima'),
        ('pendiente', 'Pendiente'),
        ('realizada', 'Realizada')
    ], string="Estado", default='proxima', required=True)
    entidad_id = fields.Many2one('btr.entidad.inspectora', string="Entidad Inspectora")
    tipo_id = fields.Many2one('btr.tipo.inspeccion', string="Tipo de Inspección", required=True)
    file_attachment = fields.Binary(string="Subir Documento")
    file_name = fields.Char(string="Nombre del Archivo Generado", readonly=True)

    @api.onchange('file_attachment', 'tipo_id', 'fecha_inspeccion')
    def _onchange_file_attachment(self):
        """Genera automáticamente el nombre del archivo basado en tipo de inspección y fecha."""
        if self.file_attachment and self.tipo_id and self.fecha_inspeccion:
            tipo = self.tipo_id.name.replace(' ', '_')
            fecha = self.fecha_inspeccion.strftime('%Y_%m_%d')
            self.file_name = f"{tipo}-{fecha}.pdf"

    def action_save_attachment(self):
        """Guarda el archivo con el nombre generado en el modelo ir.attachment."""
        if self.file_attachment and self.file_name:
            self.env['ir.attachment'].create({
                'name': self.file_name,
                'type': 'binary',
                'datas': self.file_attachment,
                'res_model': self._name,
                'res_id': self.id,
            })
            self.file_attachment = False
