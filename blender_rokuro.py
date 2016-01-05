bl_info = {
    "name": "Blender Rokuro",
    "author": "Yuichi Sato",
    "version": (0, 1),
    "blender": (2, 76, 0),
    "location": "Found in the properties shelf.",
    "description": "Modeling on the rokuro.",
    "warning": "",
    "wiki_url": "https://github.com/satoyuichi/BlenderRokuro",
    "tracker_url": "",
    "category": "3D View"}

import bpy
import math

class BlenderRokuroProps(bpy.types.PropertyGroup):
    rotate_axis_x = bpy.props.BoolProperty(name="X", default=False)
    rotate_axis_y = bpy.props.BoolProperty(name="Y", default=False)
    rotate_axis_z = bpy.props.BoolProperty(name="Z", default=True)
    rotate_speed = bpy.props.IntProperty(name="Speed", min=1, max=32, soft_max=32, soft_min=1, step=1)
    rotate_direction = bpy.props.BoolProperty(name="Rotate Left", default=True)
    
class BlenderRokuroRotate(bpy.types.Operator):
    bl_idname = "rokuro.rotate"
    bl_label = "Start"

    is_running = False
    
    def execute(self, context):
        BlenderRokuroRotate.is_running = not BlenderRokuroRotate.is_running
        print(BlenderRokuroRotate.is_running)
        return {'RUNNING_MODAL'}

    def modal(self, context, event):
        if BlenderRokuroRotate.is_running:
            print('Modal!!')
            return {'RUNNING_MODAL'}
        else:
            print('Finished!!')
            return {'FINISHED'}

        
class BlenderRokuroPanel(bpy.types.Panel):
    bl_label = "Rokuro"
    bl_idname = "OBJECT_PT_rokuro"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Tools'

    @classmethod
    def poll(self, context):
        return context.mode == 'SCULPT'
        
    def draw(self, context):
        props = context.window_manager.rokuro
        
        layout = self.layout

        row = layout.row()
        column = row.column()
        column.prop(props, "rotate_axis_x")
        column = row.column()
        column.prop(props, "rotate_axis_y")
        column = row.column()
        column.prop(props, "rotate_axis_z")

        row = layout.row()
        row.prop(props, "rotate_speed")
        
        row = layout.row()
        row.prop(props, "rotate_direction")

        row = layout.row()
        row.operator("rokuro.rotate")

def register():
    bpy.utils.register_class(BlenderRokuroProps)
    bpy.utils.register_class(BlenderRokuroPanel)
    bpy.utils.register_class(BlenderRokuroRotate)

    bpy.types.WindowManager.rokuro = bpy.props.PointerProperty(type=BlenderRokuroProps)


def unregister():
    bpy.utils.unregister_class(BlenderRokuroProps)
    bpy.utils.unregister_class(BlenderRokuroPanel)
    bpy.utils.unregister_class(BlenderRokuroRotate)

    try:
        del bpy.types.WindowManager.rokuro
    except:
        pass

def my_hundler(scene):
    cf = scene.frame_current
    r = (cf * 10)
    bpy.context.object.rotation_euler[2] = math.radians(r)
  
    bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
    
if __name__ == "__main__":
    register()

#    bpy.app.handlers.frame_change_pre.append(my_hundler)