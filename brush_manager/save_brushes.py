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

    filename: bpy.props.StringProperty()
    brush_name: bpy.props.StringProperty()
    
    def execute(self, context):
        filepath = ""
        if platform == "win32":
            filepath = "./"
            filepath = os.path.abspath(filepath)
            filepath += "\\2.81\\datafiles\\brushes\\"
        if platform == "linux" or platform == "linux2" or platform == "darwin":
            filepath = os.getcwd()
            filepath = os.path.dirname(filepath)
            filepath += "/Resources/2.81/datafiles/brushes/" + self.filename
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
        op.filename = brush.name + "_brush.blend"
        op.brush_name = brush.name