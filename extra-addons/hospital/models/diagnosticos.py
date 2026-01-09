# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Diagnosticos(models.Model):
     _name = 'hospital.diagnosticos'
     _description = 'hospital.diagnosticos'

     medico_id = fields.Many2one('hospital.medico', string="Médico", required=True)
     paciente_id = fields.Many2one('hospital.paciente', string="Paciente", required=True)
     diagnostico = fields.Text("Diagnóstico")