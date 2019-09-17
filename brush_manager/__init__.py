# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Custom Brush Manager",
    "author" : "Abinadi Cordova",
    "description" : "This addon will auto-load custom brushes in datafiles/brushes and give quick custom brush shave capabilities",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "3D View"
}

import bpy
from . load_brushes import Load_Brushes_OT_Operator
from . load_brushes import load_custom_brushes_handler
from . load_brushes import load_menu_draw
from . save_brushes import Save_Brushes_OT_Operator
from . save_brushes import menu_draw
from . select_brushes_menu import VIEW3D_MT_brush_menu
import brush_manager.select_brushes_menu

def register():
    bpy.utils.register_class(Load_Brushes_OT_Operator)
    bpy.utils.register_class(Save_Brushes_OT_Operator)
    select_brushes_menu.register()
    bpy.types.VIEW3D_MT_brush_context_menu.append(menu_draw)
    bpy.app.handlers.load_post.append(load_custom_brushes_handler)
    bpy.types.TOPBAR_MT_file.prepend(load_menu_draw)

def unregister():
    bpy.utils.unregister_class(Load_Brushes_OT_Operator)
    bpy.utils.unregister_class(Save_Brushes_OT_Operator)
    select_brushes_menu.unregister()
    bpy.types.VIEW3D_MT_brush_context_menu.remove(menu_draw)
    bpy.app.handlers.load_post.remove(load_custom_brushes_handler)
    bpy.types.TOPBAR_MT_file.remove(load_menu_draw)

if __name__ == '__main__':
    register()