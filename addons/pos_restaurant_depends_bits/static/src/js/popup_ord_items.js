/** @odoo-module */

import { AbstractAwaitablePopup } from "@point_of_sale/app/popup/abstract_awaitable_popup";
import { _t } from "@web/core/l10n/translation";
import { useState } from "@odoo/owl";

export class OrderItemsPopup extends AbstractAwaitablePopup {
    static template = "cart_ord_popup_bits";
    static defaultProps = {  
        body: "",
        list: [],
        confirmKey: false,
        confirmText: _t("Confirm"),
        cancelText: _t("Discard"),
    }; 
    setup() {
        super.setup();
        this.state = useState({ displayCategoryCount: this.props.displayCategoryCount });  
    }   
    get displayCategoryCount(){
        return this.state.displayCategoryCount;
    }
}
