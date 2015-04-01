import bpy
import random

class Duplicator(bpy.types.Operator):
    """Duplicate and shift object in space"""
    bl_idname= "object.duplicate_range"
    bl_label= "Duplicate Range"
    bl_options = {'UNDO', 'REGISTER'}
    
    x_dups = bpy.props.IntProperty(default=1)
    y_dups = bpy.props.IntProperty(default=1)
    jiggle = bpy.props.FloatProperty(default=1.0)
    spread = bpy.props.FloatProperty(default=1.0)
    
    def execute(self, context):
        duplicate_range(self.x_dups, self.y_dups, self.jiggle, self.spread, context)
        return {"FINISHED"}
    
    

def duplicate_range(x, y, jiggle, spread, context):
    original = context.object

    selected = []
    selected += [original]
    for _ in range(x):
        
        bpy.ops.object.duplicate_move(TRANSFORM_OT_translate={"value": (spread,0,0)})
        selected += [context.selected_objects[0]]
        
    selected[-1].select = False
    all = selected[:]
    for item in selected:
        item.select = True
        for _ in range(y):
            bpy.ops.object.duplicate_move(TRANSFORM_OT_translate={"value":(0,0,spread)})
            # add jiggle
            all += [context.selected_objects[0]]
            item.select = False
        bpy.ops.object.select_all(action="DESELECT")
          

    for item in all:
        item.select = True
        item.location.x += random.random() * jiggle
        item.location.y += random.random() * jiggle
        item.location.z += random.random() * jiggle
        item.select = False

bpy.utils.register_class(Duplicator)