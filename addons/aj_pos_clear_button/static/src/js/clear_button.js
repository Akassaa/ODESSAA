/** @odoo-module */

import { usePos } from "@point_of_sale/app/store/pos_hook";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { Component } from "@odoo/owl";

export class ClearButton extends Component {
    static template = "aj_pos_clear_button.ClearButton";

    setup() {
        this.pos = usePos();
    }
    click() {
        var current_order = this.pos.get_order();
        current_order.orderlines.filter(line=> line.get_product()).forEach(single_line=> current_order.removeOrderline(single_line));
    }
}

ProductScreen.addControlButton({
    component: ClearButton,
    condition: function () {
        return true;
    },
});
