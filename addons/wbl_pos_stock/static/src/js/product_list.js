/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { ProductsWidget } from "@point_of_sale/app/screens/product_screen/product_list/product_list";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { useService } from "@web/core/utils/hooks";
import { patch } from "@web/core/utils/patch";
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";
import { Component, useState, useEffect, useRef } from "@odoo/owl";

patch(ProductsWidget.prototype, {
    setup() {
        super.setup(...arguments);
        this.pos = usePos();
    },
    getProductInfo(product) {
        if (this.pos.config.hide_out_of_stock_product) {
            for (const warehouse of product.product_info.warehouses) {
                if (warehouse.available_quantity < 1) {
                    return false;
                }
            }
        }
        return true;
    },
});
