 # -*- coding: utf-8 -*-

from odoo import models, fields, api


class my_module(models.Model):

     _name = 'my_module.my_module'


     name = fields.Char(String='Name',required=True)
     Gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')],string='Gender')
     DOB= fields.Date(String='Date')
     nationality = fields.Many2one('res.country', string='Nationality')
     age=fields.Integer(String="Age")
     photo=fields.Binary(String="Image")