from odoo import models, fields

class ItiTag(models.Model):
    _name = "iti.tag"

    tag = fields.Char()