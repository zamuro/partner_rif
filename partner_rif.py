from openerp.osv import fields, osv


class res_partner(osv.osv):
    _inherit = 'res.partner'

    _columns = {
        'partner_rif': fields.char('CI/RIF', size=16, help='J-12345678-9'),
        }

res_partner()