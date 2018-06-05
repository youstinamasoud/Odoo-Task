from odoo import models, fields


class ItiMachine(models.Model):
    _name = "iti.machines"

    name = fields.Char()
    description = fields.Text()
    price = fields.Float()
    approved_by = fields.Char()
    is_approved = fields.Boolean()
    image = fields.Binary()
    category_ids = fields.Many2many('iti.tag')
    history_id = fields.One2many('history','machine_id')
