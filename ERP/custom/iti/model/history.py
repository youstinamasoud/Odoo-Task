from odoo import models, fields

class Itihistory(models.Model):
    _name = "history"

    date = fields.Date()
    desc = fields.Text()
    user_id = fields.Many2one('res.users')
    machine_id = fields.Many2one('iti.machines')