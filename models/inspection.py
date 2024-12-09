# Created by Andres Sanchez - Date: 2024-11-07
from odoo import models, fields, api
from datetime import timedelta

class InspectionManagement(models.Model):
    _name = 'inspection.management'
    _description = 'Gestión de Inspecciones'

    # Fields for inspection details
    name = fields.Char(string="Tipo de Inspección", required=True)
    type_id = fields.Many2one('inspection.type', string="Tipo de Inspección", required=True)
    entity_id = fields.Many2one('inspection.entity', string="Entidad Inspectora")
    periodicity = fields.Integer(string="Periodicidad (Años)", default=1)
    items = fields.Text(string="Ítems a Tener en Cuenta")
    location_id = fields.Many2one('maintenance.equipment', string="Hotel")
    last_inspection_date = fields.Date(string="Fecha Última Inspección")
    next_inspection_date = fields.Date(
        string="Fecha Próxima Inspección",
        compute="_compute_next_inspection_date",
        store=True
    )
    state = fields.Selection(
        [('pending', 'Próxima'), ('done', 'Realizada')],
        default='pending',
        string="Estado"
    )
    certificate_attachment_id = fields.Many2many('ir.attachment', string="Certificados Adjuntos")

    @api.depends('last_inspection_date', 'periodicity')
    def _compute_next_inspection_date(self):
        for record in self:
            if record.last_inspection_date:
                record.next_inspection_date = record.last_inspection_date + timedelta(days=record.periodicity * 365)

    def action_done(self):
        self.state = 'done'


class InspectionEntity(models.Model):
    _name = 'inspection.entity'
    _description = 'Entidad Inspectora'

    name = fields.Char(string="Nombre de la Entidad", required=True)
    contact_name = fields.Char(string="Nombre del Contacto")  # Nuevo campo
    contact_email = fields.Char(string="Correo Electrónico")  # Nuevo campo
    contact_phone = fields.Char(string="Teléfono")  # Nuevo campo


class InspectionType(models.Model):
    _name = 'inspection.type'
    _description = 'Tipo de Inspección'

    name = fields.Char(string="Nombre del Tipo", required=True)
    description = fields.Text(string="Descripción")
    state = fields.Selection(
        [('active', 'Activo'), ('inactive', 'Inactivo')],
        default='active',
        string="Estado"
    )
