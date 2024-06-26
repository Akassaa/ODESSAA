/** @odoo-module */

import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { useService } from "@web/core/utils/hooks";
import { Component } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";
import { ConfirmPopup } from "@point_of_sale/app/utils/confirm_popup/confirm_popup";
import { _t } from "@web/core/l10n/translation";

export class SaleOrderButton extends Component {
	static template = "wt_create_so_from_pos.SaleOrderButton";
	setup() {
		this.pos = usePos();
		this.orm = useService("orm");
		this.popup = useService("popup");
	}
	async onClick() {
		var self = this;
		const oderdetails = {};
		let selectedOrder = self.pos.get_order();
		if (selectedOrder.get_partner()){
			if (this.pos.get_order().get_orderlines().length > 0){
				this.pos.get_order().get_orderlines().forEach(function(orderLine) {
					oderdetails[orderLine.id] = {
						product: orderLine.get_product().id,
						quantity: orderLine.quantity,
						price: orderLine.price,
						discount: orderLine.discount,
						};
				});
				if (this.pos.get_order().get_total_tax() > 0){
					oderdetails['tax_amount'] = this.pos.get_order().get_total_tax()
				}
				oderdetails['partner_id'] = selectedOrder.get_partner().id;
				const result = await this.orm.call('sale.order','craete_saleorder_from_pos', [oderdetails]);
				if(result){
					this.pos.showScreen('ProductScreen');
					await this.popup.add(ConfirmPopup, {
						title: _t('Succès!'),
						body: _t(
							'La Commande a été ' + result.name + ' créé avec succès !!!!'
						),
					});
					// Effacer les produits et le client sélectionnés
					selectedOrder.get_orderlines().forEach(orderLine => {
						selectedOrder.remove_orderline(orderLine);
					});
					
					
				}

			}
			else if(this.pos.get_order().get_orderlines().length <= 0){
				await this.popup.add(ErrorPopup, {
					title: _t('Aucun produit'),
					body: _t("Il n’y a aucun produit pour la commande client."),
				});
			}
		}
		else{
			await this.popup.add(ErrorPopup, {
				title: _t('Client inconnu'),
				body: _t("Sélectionnez un Client."),
			});
		}
	}
}

ProductScreen.addControlButton({
	component: SaleOrderButton,
	condition: function () {
        return this.pos.config.create_so;
    },
});
