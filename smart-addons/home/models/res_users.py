# Author: Thiep Wong
# Created: 18.5/2019
from odoo import models, fields

class ResUsers(models.Model):

    _inherit = 'res.users'

    sidebar_visible = fields.Boolean("Show System Sidebar", default=True)

    def __init__(self, pool, cr):
        """ Override of __init__ to add access rights on notification_email_send
            and alias fields. Access rights are disabled by default, but allowed
            on some specific fields defined in self.SELF_{READ/WRITE}ABLE_FIELDS.
        """
        init_res = super(ResUsers, self).__init__(pool, cr)
        # duplicate list to avoid modifying the original reference
        type(self).SELF_WRITEABLE_FIELDS = list(self.SELF_WRITEABLE_FIELDS)
        type(self).SELF_WRITEABLE_FIELDS.extend(['sidebar_visible'])
        # duplicate list to avoid modifying the original reference
        type(self).SELF_READABLE_FIELDS = list(self.SELF_READABLE_FIELDS)
        type(self).SELF_READABLE_FIELDS.extend(['sidebar_visible'])
        return init_res