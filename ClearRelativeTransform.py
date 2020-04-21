import bpy
import bmesh
import mathutils
import math

bl_info = {
    "name": "Clear Relative Transform",
    "description": "Updates the transform of the object to be relative to the identity of the parent's transform.",
    "author": "Márcio Rosa, ",
    "version": (1, 0),
    "blender": (2, 82, 0),
    "location": "3D View (Object Mode) > Search menu (F3 key) > Clear Relative Transform",
    "warning": "",
    "category": "Object"}

# Updates the transform of the object to be relative to the identity of the parent's transform.
class ClearRelativeTransformOperator(bpy.types.Operator):
    '''Updates the transform of the object to be relative to the identity of the parent's transform.'''
    bl_idname = "object.clear_relative_transform_operator"
    bl_label = "Clear Relative Transform"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return len(context.selected_objects) > 0 and context.object.mode == 'OBJECT'

    def execute(self, context):
        for obj in context.selected_objects:
            obj.matrix_basis = obj.matrix_parent_inverse @ obj.matrix_basis
            obj.matrix_parent_inverse.identity()
        return {'FINISHED'}
    
def register():
    bpy.utils.register_class(ClearRelativeTransformOperator)

def unregister():
    bpy.utils.unregister_class(ClearRelativeTransformOperator)
    
if __name__ == "__main__":
    register()
