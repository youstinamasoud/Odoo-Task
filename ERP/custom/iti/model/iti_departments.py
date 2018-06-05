from odoo import models, fields

class Department(models.Model):
    _name="iti.departments"

    name = fields.Char()
    number_of_machines = fields.Integer()