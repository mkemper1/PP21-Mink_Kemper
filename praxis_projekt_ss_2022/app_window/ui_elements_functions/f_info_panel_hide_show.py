# ----------------------------------------------------------------------------
# Created By  : Tobias Mink, Marvin Kemper
# ---------------------------------------------------------------------------
"""
Shows the selected side panel and hides the others. Ord hides the selected side panel.
"""
# ---------------------------------------------------------------------------


def do(self):
    if self.found_label.isHidden() and self.found_scroll_area.isHidden():
        self.shapefile_tool_load_button.hide()
        self.shapefile_tool_scroll_area.hide()
        self.shapefile_tool_info_panel.setChecked(False)

        self.interaction_objects_label.hide()
        self.interaction_accessible_objects_scroll_area.hide()
        self.interaction_loaded_objects_scroll_area.hide()
        self.interaction_objects_create_button.hide()
        self.interaction_objects_delete_button.hide()
        self.interaction_objects_object_view_mode_button.hide()
        self.interaction_objects_info_panel.setChecked(False)

        self.found_label.show()
        self.found_scroll_area.show()
        self.founds_info_panel.setChecked(True)
    else:
        self.found_label.hide()
        self.found_scroll_area.hide()
        self.founds_info_panel.setChecked(False)
