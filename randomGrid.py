import bpy
from random import randint
from random import uniform

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

numberObj = 600
rangeFromOrigin = 10
for i in range(0, numberObj):
    x = randint(0 - rangeFromOrigin,0 + rangeFromOrigin)
    y = randint(0 - rangeFromOrigin,0 + rangeFromOrigin)
    z = randint(0 - rangeFromOrigin,0 + rangeFromOrigin)
    bpy.ops.mesh.primitive_cube_add(location=(x,y,z))
    obj= bpy.context.active_object
    mat_name = 'mat' + str(i)
    mat = bpy.data.materials.new(name= mat_name)
    r = uniform(0,1)
    g = uniform(0,1)
    b = uniform(0,1)
    mat.diffuse_color = (r,g,b)
    obj.data.materials.append(mat)
    
