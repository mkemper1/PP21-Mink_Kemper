# ----------------------------------------------------------------------------
# Created By  : Tobias Mink, Marvin Kemper
# ---------------------------------------------------------------------------
"""
Converts every new .obj file into .ply-format

-1- Get all files (.obj, .jpg, .mtl) from obj_path and ply_path
-2- Looks if files are already present in ply_path
-3- Change the format of .obj-files to .ply and save them into ply_path
-4- Copy all non .obj files into ply_path
"""
# ---------------------------------------------------------------------------
import shutil
import pymeshlab
from app_functions.general.search_for_format import search_for_format

ms = pymeshlab.MeshSet()


def do(obj_path: str, ply_path: str):
    # -1-
    obj_list = search_for_format(obj_path, ['obj'], cut=True)
    ply_list = search_for_format(ply_path, ['ply'], cut=True)
    obj_rest_list = search_for_format(obj_path, ['jpg', 'mtl'], cut=False)
    ply_rest_list = search_for_format(ply_path, ['jpg', 'mtl'], cut=False)

    # -2-
    new_obj = [elem for elem in obj_list if elem not in ply_list]
    new_rest = [elem for elem in obj_rest_list if elem not in ply_rest_list]


    # -3-
    if new_obj:
        print('New files:')
        for elem in new_obj:
            print(elem)
            ms.load_new_mesh(obj_path + elem + '.obj')
            ms.save_current_mesh(ply_path + elem + '.ply')

    # -4-
    for elem in new_rest:
        try:
            shutil.copyfile(obj_path + elem, ply_path + elem)
        except OSError:
            print(f'cannot copy {elem} from {obj_path} to {ply_path}')


