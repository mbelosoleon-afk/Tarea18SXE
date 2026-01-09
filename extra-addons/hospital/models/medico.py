from odoo import models, fields, api

class Medico(models.Model):
    _name = 'hospital.medico'
    _description = 'hospital.medico'

    nombre = fields.Char(string="Nombre del médico", required=True)
    apellidos = fields.Char(string="Apellidos del médico", required=True)
    numColegiado = fields.Char(string="Número de colegiado del médico", required=True)