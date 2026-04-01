# type: ignore
from odoo import models, fields, api


class GadjetRepairSystem(models.Model):
    _name = "gadjet.repair"
    _description = "Repair System"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    reference = fields.Char( string="Reference" ,readonly=True , )
    customer_id = fields.Many2one('res.partner', string='Customer')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('under repair', 'Under Repair'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], default='draft')
    priority = fields.Selection([
        ('1', 'Low'),
        ('2', 'Normal'),
        ('3', 'High'),
    ], string='Priority', default='1')
    
    



    