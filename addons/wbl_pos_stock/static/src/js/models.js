/** @odoo-module */

import { Order, Orderline, Payment } from "@point_of_sale/app/store/models";
import { patch } from "@web/core/utils/patch";
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";
import { _t } from "@web/core/l10n/translation";

patch(Order.prototype, {
   async pay() {
        let self = this;
        let order = this.pos.get_order();
        let lines = order.get_orderlines();
        let message = this.env.services.pos.config.custom_error_message;
        let stock_limit_deny_order = this.env.services.pos.config.deny_pos_order;
        let deny_order = false;
        var products_name = '';
        $.each(lines, function( i, line ) {
            if (this.env.services.pos.config.restrict_zero_qty_line) {
                if (line.quantity <= 0) {
                    deny_order = true;
                }
            }
            if (this.env.services.pos.config.restrict_zero_price_line) {
                if (line.get_display_price() == 0.00) {
                    deny_order = true;
                }
            }
            for (const warehouse of line.product.product_info.warehouses) {
                if (!this.env.services.pos.config.allow_order_for_out_of_stock) {
                    if (warehouse.available_quantity < 1) {
                        deny_order = true;
                        products_name += line.product.display_name + ', '
                    }
                }
                if (stock_limit_deny_order != null) {
                    if (warehouse.available_quantity <= stock_limit_deny_order) {
                        deny_order = true;
                        products_name += line.product.display_name + ', '
                    }
                }
            }
        });
        if (deny_order) {
            self.env.services.popup.add(ErrorPopup, {
                'title': _t("Stock Warning"),
                'body':  _t(message.replace('{product_name}', products_name)),
            });
        } else {
            super.pay();
        }
    },
});
