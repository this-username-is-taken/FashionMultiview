import bpy
from math import pi

def rotate(object):
    object.rotation_mode = 'XYZ'
    object.rotation_euler[0] = 87*(pi/180.0)
    object.rotation_euler[1] = 0
    object.rotation_euler[2] = 35*(pi/180.0)

def scale(object):
    object.scale = (0.03, 0.03, 0.03)

def get_object_name(name, idx, flag):
    if(flag == False):
        return name
    else:
        return name + '.' + str(idx).zfill(3)

bpy.context.scene.world.light_settings.use_environment_light=True
bpy.context.scene.world.horizon_color[0] = 255
bpy.context.scene.world.horizon_color[1] = 255
bpy.context.scene.world.horizon_color[2] = 255
scene = bpy.data.scenes['Scene']

scene.camera.location = (4, -5.6, 3)
lamb = bpy.data.objects['Lamp']
lamb.location = (6, -8, 15)
rotate(scene.camera)

cube = bpy.data.objects['Cube']
cube.location = (0, -80, 0)
cube.scale = (1, 1, 1)

objects = ["Body", "Bottoms", "Eyelashes", "Eyes", "Shoes", "Tops", "Hair", "default"]

start = 0
end = 1
flag = False

degrees = [87, 120]
camera_locations = [(4.4, -6.16, 3), (5.2, -7.28, 3.3)]

for i in range(start, end):
    file_loc = 'C:\\Users\\Long\\Desktop\\CS229\\data\\OBJs\\' + str(i) + '\\' + str(i) + '.obj'
    bpy.ops.import_scene.obj(filepath=file_loc)    

    for object in objects:
        try:
            body = bpy.data.objects[get_object_name(object, i, flag)]
            rotate(body)
            scale(body)
        except Exception:
            continue

    for pos in range(1, 2):
        scene.camera.location = camera_locations[pos]
        scene.camera.rotation_euler[0] = degrees[pos]*(pi/180.0)
        for degree in range(0, 10):
            for object in objects:
                try:
                    body = bpy.data.objects[get_object_name(object, i, flag)]
                    body.rotation_euler[2] = ((35+degree)%360)*(pi/180.0)
                except Exception:
                    continue
                
            scene.render.filepath = 'C:\\Users\\Long\\Desktop\\CS229\\data\\synthentic3\\' + str(i*2+pos) + '_' + str(degree) + '.jpg'
            scene.render.resolution_x = 1024
            scene.render.resolution_y = 1024
            bpy.ops.render.render( write_still=True )
        
    for object in objects:
        try:
            body = bpy.data.objects[get_object_name(object, i, flag)]
            bpy.data.objects.remove(body, True)
        except Exception:
            continue
        
    flag = True
