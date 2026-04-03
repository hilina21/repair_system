# type: ignore
from odoo import models, fields, api


class GadgetRepair(models.Model):
    _name = "gadjet.repair"
    _description = "Gadget Repair"

    reference = fields.Char(string="Reference", readonly=True)
    customer_id = fields.Many2one('res.partner', string='Customer')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('under_repair', 'Under Repair'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], default='draft')

    priority = fields.Selection([
        ('1', 'Low'),
        ('2', 'Normal'),
        ('3', 'High'),
    ], default='1')

    @api.model
    def create(self, vals):
        if not vals.get('reference'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('gadjet.repair') or 'New'
        return super().create(vals)