/** @odoo-module **/
import { registry } from "@web/core/registry";
import { Component, xml } from "@odoo/owl";

class GadjetDashboard extends Component {
    static template = "repair_system.gadjet_dashboard_template";
}

registry.category("actions").add("gadjet_dashboard_tag", GadjetDashboard);

