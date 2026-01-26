from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    rrss_favorita = fields.Selection(
        [
            ('twitter', 'Twitter'),
            ('instagram', 'Instagram'),
            ('facebook', 'Facebook'),
        ],
        string='Red Social Favorita'
    )
