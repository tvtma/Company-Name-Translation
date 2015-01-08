# -*- coding: utf-8 -*-
##############################################################################
#
#    @package t_to_website_filter TO Partner Name Translation for Odoo 8.0
#    @copyright Copyright (C) 2015 T.V.T Marine Automation (aka TVTMA). All rights reserved.#
#    @license http://www.gnu.org/licenses GNU Affero General Public License version 3 or later; see LICENSE.txt
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import fields,models
    
class res_partner(models.Model):
    _inherit = 'res.partner'
    
    name = fields.Char(string="Name", required=True, select=True, translate=True)

class res_company(models.Model):
    _inherit = 'res.company'    
    
    name = fields.Char(string="Company Name", size=128, required=True, store=True, related='partner_id.name', translate=True)
