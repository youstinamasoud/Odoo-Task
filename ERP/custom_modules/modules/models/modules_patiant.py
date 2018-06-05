from odoo import models , fields

class ModulesPatiant(models.Model):
    _name="modules.patiant"

    name=fields.Char()
    mobile=fields.Char()
    visit_ids=fields.One2many('modules.visit','patiant_id', string='visitation')
