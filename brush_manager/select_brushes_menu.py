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
import string

class BrushMenuCreatorOperator(bpy.types.Operator):
    """Creates the individual menus and registers them"""
    bl_label = "Create brush selection menus"
    bl_idname = "sculpt.brush_menu_creator_operator"

    def execute(self, context):
        collection = bpy.data.scenes['Scene']['brush_collection']
        for key in collection:
            self.registerSubmenu(key)

        return {'FINISHED'}

    def registerSubmenu(self, letter):

        brush_names = bpy.data.scenes['Scene']['brush_collection'][letter]

        bl_id_name = "VIEW3D_MT_brush_menu_" + letter

        class TempBrushMenu(bpy.types.Menu):
            """Submenu for brushes"""
            bl_idname = bl_id_name
            bl_label = "Sculpt Brush Menu " + letter

            def draw(self, context):
                layout = self.layout

                row = layout.row()
                for name in brush_names:
                    props = layout.operator("wm.context_set_id", icon_value=layout.icon(bpy.data.brushes[name]), text=name)
                    props.data_path = "tool_settings.sculpt.brush"
                    props.value = name

        bpy.utils.register_class(TempBrushMenu)
        return bl_id_name

class VIEW3D_MT_brush_main_menu(bpy.types.Menu):
    """Opens a menu with all brushes in several columns"""
    bl_idname = "VIEW3D_MT_brush_main_menu"
    bl_label = "Sculpt Brush Main Menu"

    def draw(self, context):
        layout = self.layout
        alphabet = bpy.data.scenes['Scene']['brush_collection']
        
        for letter in alphabet:
            layout.menu("VIEW3D_MT_brush_menu_" + letter, text=letter)