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

import os
import bpy
from bpy.app.handlers import persistent
from sys import platform
    
class Load_Brushes_OT_Operator(bpy.types.Operator):
    bl_idname = "view3d.load_custom_brushes"
    bl_label = "Load Custom Brushes"
    bl_description = "Load custom brushes from /2.81/datafiles/brushes"
    
    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons['brush_manager'].preferences
        filepath = addon_prefs.savepath
        current_brushes = []
        
        for brush in bpy.data.brushes:
            current_brushes.append(brush.name)
            
        for file in os.listdir(filepath):
            if file.endswith(".blend"):
                with bpy.data.libraries.load(filepath + file, link = False) as (data_from, data_to):
                    data_to.brushes = [name for name in data_from.brushes if name not in current_brushes]

        return {'FINISHED'}

@persistent
def load_custom_brushes_handler(empty):
    preferences = bpy.context.preferences
    addon_prefs = preferences.addons['brush_manager'].preferences
    filepath = addon_prefs.savepath
    current_brushes = []
    
    for brush in bpy.data.brushes:
        current_brushes.append(brush.name)
        
    for file in os.listdir(filepath):
        if file.endswith(".blend"):
            with bpy.data.libraries.load(filepath + file, link = False) as (data_from, data_to):
                data_to.brushes = [name for name in data_from.brushes if name not in current_brushes]

    return {'FINISHED'}

def load_menu_draw(self, context):
    layout = self.layout

    layout.separator()

    layout.operator("view3d.load_custom_brushes", text="Reload Custom Brushes")