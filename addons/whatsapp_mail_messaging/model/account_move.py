# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Aysha Shalin (odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from itertools import groupby
from odoo import models, _
from odoo.exceptions import UserError


class AccountMove(models.Model):
    """
    This class extends the 'account.move' model to add custom functionalities
    related to WhatsApp messaging.
    """
    _inherit = 'account.move'

    def action_send_whatsapp(self):
        """ Action for sending whatsapp message."""
        compose_form_id = self.env.ref(
            'whatsapp_mail_messaging.whatsapp_send_message_view_form').id
        ctx = dict(self.env.context)
        message = (
                "Bonjour" + " " + self.partner_id.name + ',' + '\n' +
                "Voici votre facture" + ' ' + self.name + ' ' + "d'un montant de" +
                ' ' + str(self.amount_total) + self.currency_id.symbol + ' ' +
                "de la part de " + self.company_id.name +
                ". Veuillez effectuer le paiement dès que possible. " + '\n'
                + "Veuillez utiliser la communication suivante pour votre paiement" +
                ' ' + self.name)

        ctx.update({
            'default_message': message,
            'default_partner_id': self.partner_id.id,
            'default_mobile': self.partner_id.mobile,
            'default_image_1920': self.partner_id.image_1920,
        })
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'whatsapp.send.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
            'context': ctx,
        }

    def check_customers(self, partner_ids):
        """ Check if the selected invoices belong to the same customer."""
        partners = groupby(partner_ids)
        return next(partners, True) and not next(partners, False)

    def action_whatsapp_multi(self):
        """
        Initiate WhatsApp messaging for multiple invoices and open a message
        composition wizard.
        """
        account_move_ids = self.env['account.move'].browse(
            self.env.context.get('active_ids'))
        partner_ids = []
        for account_move in account_move_ids:
            partner_ids.append(account_move.partner_id.id)
        partner_check = self.check_customers(partner_ids)
        if partner_check:
            account_move_numbers = account_move_ids.mapped('name')
            account_move_numbers = "\n".join(account_move_numbers)
            compose_form_id = self.env.ref(
                'whatsapp_mail_messaging.whatsapp_send_message_view_form').id
            ctx = dict(self.env.context)
            message = ("Bonjour" + " " + self.partner_id.name + ',' + '\n' +
                       "Vos commandes sont" + '\n' + account_move_numbers + ' ' +
                       "sont prêtes pour examen. N'hésitez pas à nous contacter si "
                       "vous avez des questions.")

            ctx.update({
                'default_message': message,
                'default_partner_id': account_move_ids[0].partner_id.id,
                'default_mobile': account_move_ids[0].partner_id.mobile,
                'default_image_1920': account_move_ids[0].partner_id.image_1920,
            })
            return {
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'whatsapp.send.message',
                'views': [(compose_form_id, 'form')],
                'view_id': compose_form_id,
                'target': 'new',
                'context': ctx,
            }
        else:
            raise UserError(_(
                'Il semble que vous ayez sélectionné des commandes de plusieurs'
                ' clients. Veuillez sélectionner des commandes d\'un seul client.'))

