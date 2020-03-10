# -*- coding: utf-8 -*-
# Copyright 2017 Jarsa Sistemas S.A. de C.V.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class HospitalTestSearchWizard(models.TransientModel):
    _name = 'hospital.test.search.wizard'
    _description = "Pending description"

    date = fields.Date(string="Date",
                       required=True)
