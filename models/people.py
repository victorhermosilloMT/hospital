# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Employee(models.Model):
    _name = 'hospital.employee'
    _description = "Hospital Employee"

    id = fields.Integer(string="Id")
    image = fields.Binary(string="Image", attachment=True, store=True)
    name = fields.Char(string="Name:", required=True)
    lastName = fields.Char(string="Last name:")
    phone = fields.Char(string="Phone:")
    age = fields.Integer(string="Age:")

    file_ids = fields.One2many('hospital.file', 'employee_id', string="Cases attending:")
    patient_id = fields.One2many('hospital.patient', 'employee_id', string="Patients:")


class Patient(models.Model):
    _name = 'hospital.patient'
    _description = "Hospital Patient"

    id = fields.Integer(string="Id")
    name = fields.Char(string="Name:", required=True)
    lastName = fields.Char(string="Last name:")
    phone = fields.Char(string="Phone:")
    age = fields.Integer(string="Age:")
    problem = fields.Text(string="Sintoms:", required=True)
    status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')], required=True)

    files_id = fields.One2many('hospital.file', 'patients_id', ondelete='cascade', string="Cases:")
    employee_id = fields.Many2one('hospital.employee', ondelete='set null', string="Employee in charge:", required=True)

    _defaults = {
        'status': 'active'
    }

class File(models.Model):
    _name = 'hospital.file'
    _description = "Hospital Files"

    id = fields.Integer(string="Id")
    name = fields.Char(string="File name:", required=True)
    info = fields.Text(string="File info:")
    employee_id = fields.Many2one('hospital.employee', ondelete='set null', string="Employee in charge:", required=True)
    patients_id = fields.Many2one('hospital.patient', ondelete='set null', string="Patient attending:", required=True)
