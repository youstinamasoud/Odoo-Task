from odoo import models , fields

class ModulesVisit(models.Model):
    _name="modules.visit"
    _rec_name='Date'

    Date=fields.Date()
    Datetime=fields.Datetime()
    patiant_id=fields.Many2one(comodel_name='modules.patiant' , string='Patiant')

