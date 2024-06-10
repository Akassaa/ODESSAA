/** @odoo-module **/

import { RenderContainer } from "@point_of_sale/app/printer/render_service";
import { patch } from "@web/core/utils/patch";
import { xml } from "@odoo/owl";

patch(RenderContainer, {
    template: xml`
        <div style="position: absolute;">
            <div t-ref="ref">
                <t t-if="props.comp.component" t-component="props.comp.component" t-props="props.comp.props"/>
            </div>
            <div class="render-container" />
        </div>`
})