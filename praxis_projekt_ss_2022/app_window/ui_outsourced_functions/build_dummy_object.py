# ----------------------------------------------------------------------------
# Created By  : Tobias Mink, Marvin Kemper
# ---------------------------------------------------------------------------
"""
Loads a dummy object in plot, which some other functions depend on.
"""
# ---------------------------------------------------------------------------
from data.dictionarys import dummy_layer, original_layers


def do(self):
    # For the clipping algorithm to work, a mesh, where the plane/box widget can itself attach to, must preexist.
    # Therefore an invisible dummy is created.
    dummy_layer['dummy_layer_0'] = self.plotter.add_mesh(mesh=next(iter(original_layers.items()))[1],
                                                         name='dummy_layer_0', opacity=0.0,
                                                         show_scalar_bar=False, reset_camera=False)
