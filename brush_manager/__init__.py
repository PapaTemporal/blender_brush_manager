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
    "category" : "3D View",
    "author" : "Abinadi Cordova",
    "description" : "This addon will auto-load custom brushes in datafiles/brushes and give quick custom brush shave capabilities",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "3D View > Shift-Space",
}

import bpy
from . load_brushes import *
from . save_brushes import *
from . select_brushes_menu import *

addon_keymaps = []

def register():
    bpy.utils.register_class(Load_Brushes_OT_Operator)
    bpy.utils.register_class(Save_Brushes_OT_Operator)
    bpy.types.VIEW3D_MT_brush_context_menu.append(menu_draw)
    bpy.app.handlers.load_post.append(load_custom_brushes_handler)
    bpy.types.TOPBAR_MT_file.prepend(load_menu_draw)
    bpy.utils.register_class(VIEW3D_MT_brush_main_menu)
    
    # register hotkeys
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Sculpt')
    kmi = km.keymap_items.new('wm.call_menu', 'SPACE', 'PRESS', shift=True)
    kmi.properties.name = "VIEW3D_MT_brush_main_menu"
    addon_keymaps.append((km, kmi))

def unregister():
    bpy.utils.unregister_class(Load_Brushes_OT_Operator)
    bpy.utils.unregister_class(Save_Brushes_OT_Operator)
    bpy.types.VIEW3D_MT_brush_context_menu.remove(menu_draw)
    bpy.app.handlers.load_post.remove(load_custom_brushes_handler)
    bpy.types.TOPBAR_MT_file.remove(load_menu_draw)
    bpy.utils.unregister_class(VIEW3D_MT_brush_main_menu)
    
    # unregister hotkeys
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

if __name__ == '__main__':
    register()