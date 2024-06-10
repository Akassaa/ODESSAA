/** @odoo-module */

import { Orderline } from "@point_of_sale/app/generic_components/orderline/orderline";
import { useListener } from "@web/core/utils/hooks";
import { Component, useState, useEffect, useRef } from "@odoo/owl";
import { OrderWidget } from "@point_of_sale/app/generic_components/order_widget/order_widget";
import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";


const itemRemoveOrder = {
    setup() {
        super.setup();
        this.numberBuffer = useService("number_buffer");
    },
    clear_button_fun() {
        this.numberBuffer.sendKey("Backspace");
        this.numberBuffer.sendKey("Backspace");
    }
};

patch(Orderline.prototype, itemRemoveOrder);
