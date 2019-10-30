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
    "blender" : (2, 82, 0),
    "version" : (0, 0, 1),
    "location" : "3D View > Shift-Space",
}

import bpy
from . load_brushes import *
from . save_brushes import *
from . select_brushes_menu import *
from bpy.types import AddonPreferences
from bpy.props import StringProperty
from sys import platform
import os
from os import path

class CustomBrushManagerPreferences(AddonPreferences):
    bl_idname = __name__

    if platform == "linux" or platform == "linux2":
        app_data = os.getenv('HOME')
        user_prefs = app_data + '/.config/blender/brush_manager.txt'
    elif platform == "darwin":
        app_data = os.getenv('HOME')
        user_prefs = app_data + '/Library/Application Support/Blender/brush_manager.txt'
    elif platform == 'win32' or platform == 'cygwin':
        app_data = os.getenv('APPDATA')
        user_prefs = app_data + '\\Roaming\\Blender Foundation\\Blender\\brush_manager.txt'
    filepath = ""

    if not os.path.exists(user_prefs):
        if platform == "win32" or platform == "cygwin":
            app_data = os.getenv('APPDATA')
            filepath = app_data + "\\Roaming\\Blender Foundation\\Blender\\brushes\\"
        elif platform == "linux" or platform == "linux2":
            app_data = os.getenv('HOME')
            filepath = app_data + "/.config/blender/brushes/"
        elif platform == "darwin":
            app_data = os.getenv('HOME')
            filepath = app_data + '/Library/Application Support/Blender/brushes/'
        if not os.path.exists(filepath):
            os.mkdir(filepath)
        with open(user_prefs, "w") as uPrefs:
            uPrefs.write(filepath)
    else:
        with open(user_prefs) as prefs_file:
            filepath = prefs_file.readline().strip()
                

    savepath: StringProperty(
        name="Save Brush Path",
        subtype='FILE_PATH',
        default=filepath
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "savepath")
        op = layout.operator('view3d.save_bmprefs', text="Save Brush Path")
        op.user_prefs = self.user_prefs

class Save_BMPrefs_OT_Operator(bpy.types.Operator):
    bl_idname = "view3d.save_bmprefs"
    bl_label = "Save Brush Manager Preferences"
    bl_description = "Saves the Brush Manager preferences to a file in blender appdata directory"

    user_prefs: bpy.props.StringProperty()

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences
        filepath = addon_prefs.savepath

        if not os.path.exists(filepath):
            os.mkdir(filepath)
            with open(self.user_prefs, "w") as uPrefs:
                uPrefs.writelines(filepath)
        else:
            with open(self.user_prefs, "w") as uPrefs:
                uPrefs.writelines(filepath)
        return {'FINISHED'}

addon_keymaps = []

def register():
    bpy.utils.register_class(Save_BMPrefs_OT_Operator)
    bpy.utils.register_class(CustomBrushManagerPreferences)
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
    bpy.utils.unregister_class(Save_BMPrefs_OT_Operator)
    bpy.utils.unregister_class(CustomBrushManagerPreferences)
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