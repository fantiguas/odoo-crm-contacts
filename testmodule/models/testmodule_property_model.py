from odoo import models, fields    

class crmInherit(models.Model):
    _inherit = 'crm.lead'

    contacto = fields.Selection(selection=[('azure interior', 'Azure Interior')] ,required=True)
    distribuidor = fields.Selection(selection=[('do company', 'DO Company')] ,required=True)
    tecnico = fields.Char(default='Eli Lambert',required=True)
    tipo_paquete = fields.Selection(selection=[('sky familiar', 'Sky Familiar')], required=True)
    digital = fields.Integer(default=1)
    hd = fields.Integer(default=1)
    total_cantidad = fields.Integer(default=3)
    producto = fields.Selection(selection=[('[cons_0002] simple pen', '[CONS_0002] Simple Pen')], required=True)
    forma_pago = fields.Selection(selection=[('efectivo', 'Efectivo')], required=True)
    propietario_tarjeta = fields.Char(required=True)
    tipo_bandera = fields.Selection(selection=[('bar restaurant', 'Bar Restaurant')], required=True)
    venta_promociones = fields.Selection(selection=[('nacional', 'Nacional')], required=True)



class contactsInherit(models.Model):
    _inherit = 'res.partner'

    nombre_del_suscriptor = fields.Char(required=True)
    apellido_paterno = fields.Char(required=True)
    apellido_materno = fields.Char(required=True)
    tipo_de_identificacion = fields.Selection(selection=[('pasaporte', 'Pasaporte')], required=True)
    numero_de_identificacion = fields.Char(required=True)
    nombre_referencia_1 = fields.Char(required=True)
    parentesco_referencia_1 = fields.Selection(selection=[('amigo', 'Amigo')], required=True)
    parentesco_referencia_2 = fields.Selection(selection=[('compadre', 'Compadre')], required=True)
    nombre_referencia_2 = fields.Char(required=True)
    apellido_p = fields.Char(required=True)
    apellido_m = fields.Char(required=True)
    telefono_referencia_1 = fields.Char(required=True)
    telefono_referencia_2 = fields.Char(required=True)
    telefono_2_referencia_1 = fields.Char(required=True)
    telefono_2_referencia_2 = fields.Char(required=True)
    telefono_1 = fields.Char(required=True)
    telefono_2 = fields.Char(required=True)
    telefono_3 = fields.Char(required=True)


class TestModulePropertyModel(models.Model):
    _name = 'testmodule.model'
    _description = 'Test Module Model'

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(  string='Type',
    selection=[('north', 'North'), ('south', 'South'), ('east','East'), ('west', 'West')])
    
    active = fields.Boolean(string = 'Active', default=False)
    state = fields.Selection( string='Choose One',
    selection=[('new', 'New'), ('offer received', 'Offer Received'), ('offer accepted','Offer Accepted'), ('sold', 'Sold'), ('canceled','Canceled')], default='New')
    
