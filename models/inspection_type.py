# Creado por Andres Sanchez - Fecha: 2024-11-26
# inspection_type.py
from odoo import models, fields

class InspectionType(models.Model):
    _name = 'inspection.type'
    _description = 'Tipo de Inspección'

    name = fields.Char(string="Nombre del Tipo", required=True)
    description = fields.Text(string="Descripción")
    state = fields.Selection([
        ('active', 'Activo'),
        ('inactive', 'Inactivo')
    ], default='active', string="Estado")
