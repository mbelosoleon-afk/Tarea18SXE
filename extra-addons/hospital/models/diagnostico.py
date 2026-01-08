from odoo import models, fields, api


class Diagnostico(models.Model):
    _name = 'hospital.diagnostico'
    _description = 'hospital.diagnostico'

    nombreMedico = fields.Many2one('hospital.medico', string="Médico", required=True)
    nombrePaciente = fields.Many2one('hospital.paciente', string="Paciente", required=True)
    diagnosticos = fields.Text(string="Diagnóstico")