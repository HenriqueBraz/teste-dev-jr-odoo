# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields
from dateutil.relativedelta import relativedelta
import datetime


class EstateModel(models.Model):
    _name = "estate.property"
    _description = "real_state_app"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(default=lambda self: datetime.date.today() + relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(required=True, selection=[('any', 'Any'), ('north', 'North'),
                                                                    ('south', 'South'), ('east', 'East'),
                                                                    ('west', 'West')], default='any')
    state = fields.Selection(required=True, selection=[('new', 'New'), ('offer', 'Offer'), ('received', 'Received'),
                                                       ('offer', 'Offer'), ('accepted', 'Accepted'), ('sold', 'Sold'),
                                                       ('canceled', 'Canceled')], default='new')
