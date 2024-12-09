# Creado por Andres Sanchez - Fecha: 2024-11-26
# inspection_entity.py
from odoo import models, fields, api

class InspectionEntity(models.Model):
    _name = 'inspection.entity'
    _description = 'Entidad Inspectora'

    name = fields.Char(string="Nombre de la Entidad", required=True)
    contact_name = fields.Char(string="Nombre del Contacto")
    contact_email = fields.Char(string="Correo Electrónico")
    contact_phone = fields.Char(string="Teléfono")
    contact_info = fields.Char(
        string="Información de Contacto",
        compute="_compute_contact_info",
        store=True
    )

    @api.depends('contact_name', 'contact_email', 'contact_phone')
    def _compute_contact_info(self):
        for record in self:
            parts = []
            if record.contact_name:
                parts.append(record.contact_name)
            if record.contact_email:
                parts.append(record.contact_email)
            if record.contact_phone:
                parts.append(record.contact_phone)
            record.contact_info = " - ".join(parts)
