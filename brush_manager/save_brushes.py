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

class Save_Brushes_OT_Operator(bpy.types.Operator):
    bl_idname = "view3d.save_custom_brushes"
    bl_label = "Save Custom Brushes"
    bl_description = "Save custom brushes to /2.81/datafiles/brushes"

    brush_name: bpy.props.StringProperty()
    
    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons['brush_manager'].preferences
        filepath = addon_prefs.savepath
        print("FILEPATH FROM SAVE OPERATOR: %s" % (filepath))
        filepath += str(self.brush_name).translate ({ord(c): "_" for c in "!@#$%^&*()[]{};:,./<>?\|`~-=+"})
        filepath += "_brush.blend"
        brush_pack = [context.blend_data.brushes[self.brush_name]]
        brush_pack = set(brush_pack)
        bpy.data.libraries.write(filepath, brush_pack)
        return {'FINISHED'}

def menu_draw(self, context):
    layout = self.layout
    tool_settings = context.tool_settings
    
    if context.sculpt_object:
        settings = tool_settings.sculpt
        brush = getattr(settings, "brush", None)
        
        layout.separator()

        op = layout.operator('view3d.save_custom_brushes', text = "Save " + brush.name)
        op.brush_name = brush.name