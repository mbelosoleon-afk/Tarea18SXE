from odoo import models, fields, api

class Paciente(models.Model):
    _name = 'hospital.paciente'
    _description = 'hospital.paciente'

    nombre = fields.Char(string="Nombre del paciente", required=True)
    apellidos = fields.Char(string="Apellidos del paciente", required=True)
    sintomas = fields.Char(string="Síntomas del paciente", required=True)