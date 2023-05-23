import bpy
import os

# Step 1: Clear existing mesh objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Step 2: Create a new mesh and an object to link it with
mesh = bpy.data.meshes.new(name='PyramidMesh')
obj = bpy.data.objects.new('Pyramid', mesh)

# Link the object to the scene
scene = bpy.context.scene
scene.collection.objects.link(obj)

# Make the object the active object
bpy.context.view_layer.objects.active = obj
obj.select_set(True)

# Step 3: Define the vertices and faces of the pyramid
vertices = [(1, 1, 0), (1, -1, 0), (-1, -1, 0), (-1, 1, 0), (0, 0, 2)] # Pyramid vertices
faces = [(0, 1, 2, 3), (0, 1, 4), (1, 2, 4), (2, 3, 4), (3, 0, 4)] # Pyramid faces

# Step 4: Update the mesh with pyramid data
mesh.from_pydata(vertices, [], faces)
mesh.update()

# Step 5: Center the pyramid in the scene
obj.location = (0, 0, 0)

# Step 6: Export the pyramid model in GLTF format
bpy.ops.export_scene.gltf(filepath="pyramid.gltf")
