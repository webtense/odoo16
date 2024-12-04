# Fecha: 2024-12-04
# Nombre del archivo: inspeccion.py
# Versión del archivo: V3

from odoo import models, fields, api

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
    new_attachment = fields.Binary(string="Subir Documento")
    new_attachment_name = fields.Char(string="Nombre del Documento")

    @api.model
    def attach_document(self):
        """Crea un nuevo archivo adjunto desde el campo de carga"""
        if self.new_attachment:
            attachment = self.env['ir.attachment'].create({
                'name': self.new_attachment_name or "Documento Adjunto",
                'type': 'binary',
                'datas': self.new_attachment,
                'res_model': self._name,
                'res_id': self.id,
            })
            self.attachment_ids = [(4, attachment.id)]
            # Limpia los campos después de subir el archivo
            self.new_attachment = False
            self.new_attachment_name = False
