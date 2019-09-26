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
from . select_brushes_menu import BrushMenuCreatorOperator
    
class Load_Brushes_OT_Operator(bpy.types.Operator):
    bl_idname = "view3d.load_custom_brushes"
    bl_label = "Load Custom Brushes"
    bl_description = "Load custom brushes from /2.81/datafiles/brushes"
    
    def execute(self, context):
        filepath = ""
        if platform == "win32":
            filepath = "./"
            filepath = os.path.abspath(filepath)
            filepath += "\\2.81\\datafiles\\brushes\\"
        if platform == "linux" or platform == "linux2" or platform == "darwin":
            filepath = os.getcwd()
            filepath = os.path.dirname(filepath)
            filepath += "/Resources/2.81/datafiles/brushes/"
        current_brushes = []
        
        for brush in bpy.data.brushes:
            current_brushes.append(brush.name)
            
        for file in os.listdir(filepath):
            if file.endswith(".blend"):
                with bpy.data.libraries.load(filepath + file, link = False) as (data_from, data_to):
                    data_to.brushes = [name for name in data_from.brushes if name not in current_brushes]

        bpy.ops.sculpt.brush_menu_items_operator()
        return {'FINISHED'}

@persistent
def load_custom_brushes_handler(empty):
    filepath = ""
    if platform == "win32":
        filepath = "./"
        filepath = os.path.abspath(filepath)
        filepath += "\\2.81\\datafiles\\brushes\\"
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        filepath = os.getcwd()
        filepath = os.path.dirname(filepath)
        filepath += "/Resources/2.81/datafiles/brushes/"
    current_brushes = []
    
    for brush in bpy.data.brushes:
        current_brushes.append(brush.name)
        
    for file in os.listdir(filepath):
        if file.endswith(".blend"):
            with bpy.data.libraries.load(filepath + file, link = False) as (data_from, data_to):
                data_to.brushes = [name for name in data_from.brushes if name not in current_brushes]

    bpy.ops.sculpt.brush_menu_items_operator()
    return {'FINISHED'}

def load_menu_draw(self, context):
    layout = self.layout

    layout.separator()

    layout.operator("view3d.load_custom_brushes", text="Reload Custom Brushes")

class Brush_Menu_Items(bpy.types.Operator):
    """Generic Operator"""
    bl_idname = "sculpt.brush_menu_items_operator" 
    bl_label = "Brush Menu Items"
    
    brush_collection = {'a':[],
                        'b':[],
                        'c':[],
                        'd':[],
                        'e':[],
                        'f':[],
                        'g':[],
                        'h':[],
                        'i':[],
                        'j':[],
                        'k':[],
                        'l':[],
                        'm':[],
                        'n':[],
                        'o':[],
                        'p':[],
                        'q':[],
                        'r':[],
                        's':[],
                        't':[],
                        'u':[],
                        'v':[],
                        'w':[],
                        'x':[],
                        'y':[],
                        'z':[],
                        '0':[],
                        '1':[],
                        '2':[],
                        '3':[],
                        '4':[],
                        '5':[],
                        '6':[],
                        '7':[],
                        '8':[],
                        '9':[]
                        }
                        
    def execute(self, context):
        brushes = bpy.data.brushes
        collection = self.brush_collection
        
        for brush in brushes:
            if brush.use_paint_sculpt:
                b_start_letter = brush.name[0]
                collection[b_start_letter.lower()].append(brush.name)
            
        bpy.data.scenes['Scene']['brush_collection'] = collection

        bpy.ops.sculpt.brush_menu_creator_operator()
        return {'FINISHED'}
