from odoo import models, fields

class ConfSetting(models.TransientModel):
    _inherit = 'res.config.settings'

    is_hide_price = fields.Boolean(default=False, config_parameter="hide_price")
    
    #testing
    def action_confirm(self):
        is_hide_price = self.env['ir.config_parameter'].sudo().get_param('database.uuid')