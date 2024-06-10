/** @odoo-module **/
import { patch } from "@web/core/utils/patch";
import { FloorScreen } from "@pos_restaurant/app/floor_screen/floor_screen";

patch(FloorScreen.prototype, {
  onPatched() {
    var img =
      "/web/image/pos.config/" +
      String(this.pos.config.id) +
      "/floor_Background";
    this.floorMapRef.el.style.background = "url(" + img + ")";
    this.state.floorMapScrollTop =
      this.floorMapRef.el.getBoundingClientRect().top;
  },
  onMounted() {
    var img =
      "/web/image/pos.config/" +
      String(this.pos.config.id) +
      "/floor_Background";
    this.floorMapRef.el.style.background = "url(" + img + ")";
    this.state.floorMapScrollTop =
      this.floorMapRef.el.getBoundingClientRect().top;

    if (!this.pos.isEditMode && this.pos.floors.length > 0) {
      this.addFloorRef.el.style.display = "none";
    } else {
      this.addFloorRef.el.style.display = "initial";
    }
    this.state.floorMapScrollTop =
      this.floorMapRef.el.getBoundingClientRect().top;
  },
});
