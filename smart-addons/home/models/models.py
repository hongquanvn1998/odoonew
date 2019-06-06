# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Home(models.Model):
    _name = 'home.home'
    _inherit = "ir.ui.menu"
    

    @api.model
    def home_board_view(self):
        return self
    #_table = 'ir_module_module'
    # name = fields.Char()
    # shortdesc = fields.Char()
    #id = fields.Integer()

    #phanmem = fields.('ir.module.module', string='Financial Account', domain=[('application', '=', True),('state', '=','installed' ),('auto_install','=',True)])
    #_custom = True
   # _sql_constraints =["home","select id, name, shortdesc from ir_module_module where application==true","Ok"]

   
    #domain=['&', ('state', '=','installed' ),('auto_install','=',True)]
    # activated = fields.Char("Da goi den model")

    # @api.model_cr
    # def init(self):
    #     self._cr.execute("""
    #     SELECT * from ir_module_module where application = 'true'
    #     """)
    #self.where
    # @api.model
    # def list(self, args):
    #     self.domain = ["home","select id, name, shortdesc from ir_module_module where application==true","Ok"]
    #     print (self)
    #     print(self.list)
    #     return self       

   # def List():

    # name = fields.Char()
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     self.value2 = float(self.value) / 100