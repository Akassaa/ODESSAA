/** @odoo-module **/
import { patch } from "@web/core/utils/patch";
import { ActionpadWidget } from "@point_of_sale/app/screens/product_screen/action_pad/action_pad";
import { OrderItemsPopup } from "./popup_ord_items";
import { useService } from "@web/core/utils/hooks";
import { _t } from "@web/core/l10n/translation"; 
patch(ActionpadWidget.prototype, {
    setup() {
        super.setup();  
        this.popup = useService("popup");
    },
    async onClickItems(){ 
        const { confirmed,payload: inputNote } = await this.popup.add(OrderItemsPopup, {
            displayCategoryCount: this.displayCategoryCount,
            title: _t("Order Items"),
        });
    }
});