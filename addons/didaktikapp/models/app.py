from odoo import models, fields

class DidaktikApp(models.Model):
    _name = 'didaktikapp.app'
    _description = 'Aplicaciones Didaktik'

    name = fields.Char(string="Nombre de la App", required=True)
    description = fields.Text(string="Descripcion")
    fecha_fin = fields.Date(string="Fecha de finalizacion")

    cliente_id = fields.Many2one('res.partner', string="Cliente")

    responsable_comunicacion_id = fields.Many2one(
    'hr.employee',
    string="Responsable Comunicacion",
    domain="[('category_ids.name', '=', 'Comunicador')]")

    ios = fields.Boolean(string="Version iOS")

    def action_marcar_todas_ios(self):
        self.search([]).write({'ios': True})

    def action_desmarcar_todas_ios(self):
        self.search([]).write({'ios': False})