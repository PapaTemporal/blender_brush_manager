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

import bpy

class VIEW3D_MT_brush_main_menu(bpy.types.Menu):
    """Opens a menu with all brushes in several columns"""
    bl_idname = "VIEW3D_MT_brush_main_menu"
    bl_label = "Sculpt Brush Main Menu"

    def draw(self, context):
        layout = self.layout
        
        flow = layout.column_flow(columns=4)
        for brush in bpy.data.brushes:
            if brush.use_paint_sculpt:
                col = flow.column()
                props = col.operator("wm.context_set_id", icon_value=layout.icon(bpy.data.brushes[brush.name]), text=brush.name)
                props.data_path = "tool_settings.sculpt.brush"
                props.value = brush.name