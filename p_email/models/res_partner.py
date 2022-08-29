from odoo import api, models
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.constrains('email')
    def _check_duplicate_email(self):
        for rec in self:
            emails = self.env['res.partner'].search([('email', '=', rec.email)])
            for obj in emails:
                if obj.email:
                    raise ValidationError("Duplicate Email")
