# ----------------------------------------------------------------------------
# Created By  : Tobias Mink, Marvin Kemper
# ---------------------------------------------------------------------------
"""
Loads every mesh from segmentation_extraction_clipped_layers into the plot.
"""
# ---------------------------------------------------------------------------
from data.dictionarys import excavation_layers, shapefiles_layers, dummy_layer, segmentation_extraction_layers, \
    shapefiles_clipped_and_subdivided_layers
from data.lists import excavation_semaphor, shapefile_semaphor, dummy_semaphore, segmentation_semaphor, \
    extraction_semaphor


def do(self, state=None):
    self.plotter.show_grid()
    # clear and reset
    self.plotter.remove_actor(excavation_layers.keys())
    self.plotter.remove_actor(shapefiles_layers.keys())
    self.plotter.remove_actor(shapefiles_clipped_and_subdivided_layers.keys())

    self.plotter.clear_plane_widgets()

    self.excavation_side_texture.setChecked(False)
    self.excavation_side_color.setChecked(False)
    self.segmentation_tool_texture.setChecked(False)
    self.segmentation_tool_color.setChecked(False)
    self.shapefile_tool_load.setChecked(False)

    excavation_layers.clear()
    shapefiles_layers.clear()
    shapefiles_clipped_and_subdivided_layers.clear()

    excavation_semaphor[0] = 2
    shapefile_semaphor[0] = 2

    self.interaction_objects_label.hide()
    self.interaction_accessible_objects_scroll_area.hide()
    self.interaction_loaded_objects_scroll_area.hide()
    self.interaction_objects_create_button.hide()
    self.interaction_objects_delete_button.hide()
    self.interaction_objects_object_view_mode_button.hide()
    self.interaction_objects_info_panel.setChecked(False)

    self.found_label.hide()
    self.found_scroll_area.hide()
    self.founds_info_panel.setChecked(False)

    self.shapefile_tool_load_button.hide()
    self.shapefile_tool_scroll_area.hide()
    self.shapefile_tool_info_panel.setChecked(False)

    # load dummy
    if dummy_semaphore[0] == 1:
        self.build_dummy_object()
        dummy_semaphore[0] = 0

    # clip function
    def clip_mesh(box):
        segmentation_semaphor[0] = 2
        self.clipping(use='extraction', param=[box])

    # plot textures or colores
    if state:
        if self.extraction_tool_texture.isChecked() and extraction_semaphor[0] != 0:
            extraction_semaphor[0] = 0
            self.clear_tool(use='extraction_tool', tex_or_col='tex')
        elif self.extraction_tool_color.isChecked() and extraction_semaphor[0] != 1:
            extraction_semaphor[0] = 1
            self.clear_tool(use='extraction_tool', tex_or_col='col')
        self.plotter.add_box_widget(clip_mesh, rotation_enabled=False)
    else:
        # check for found/-s
        if self.founds_show_hide.isChecked():
            self.check_founds()
        dummy_semaphore[0] = 1
        dummy_layer.clear()
        self.plotter.clear_box_widgets()
