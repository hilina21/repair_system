/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";

class GadgetDashboard extends Component {}

GadgetDashboard.template = "repair_system.dashboard";

registry.category("actions").add("gadget_dashboard", GadgetDashboard);