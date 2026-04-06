"""
DIGM 131 - Assignment 1: Procedural Scene Builder
==================================================

OBJECTIVE:
    Build a simple 3D scene in Maya using Python scripting.
    You will practice using maya.cmds to create and position geometry,
    and learn to use descriptive variable names.

REQUIREMENTS:
    1. Create a ground plane (a large, flat polygon plane).
    2. Create at least 5 objects in your scene.
    3. Use at least 2 different primitive types (e.g., cubes AND spheres,
       or cylinders AND cones, etc.).
    4. Position every object using descriptive variable names
       (e.g., house_x, tree_height -- NOT x1, h).
    5. Add comments explaining what each section of your code does.

GRADING CRITERIA:
    - [20%] Ground plane is created and scaled appropriately.
    - [30%] At least 5 objects are created using at least 2 primitive types.
    - [25%] All positions/sizes use descriptive variable names.
    - [15%] Code is commented clearly and thoroughly.
    - [10%] Scene is visually coherent (objects are placed intentionally,
            not overlapping randomly).

TIPS:
    - Run this script from Maya's Script Editor (Python tab).
    - Use maya.cmds.polyCube(), maya.cmds.polySphere(), maya.cmds.polyCylinder(),
      maya.cmds.polyCone(), maya.cmds.polyPlane(), etc.
    - Use maya.cmds.move(x, y, z, objectName) to position objects.
    - Use maya.cmds.scale(x, y, z, objectName) to resize objects.
    - Use maya.cmds.rename(oldName, newName) to give objects meaningful names.
"""
"""
DIGM 131 - Assignment 1: Procedural Scene Builder
Author: Lillian Kager
Date: April 3, 2026

Description:
This Python script uses Maya commands to build a 3D scene. 
The scene includes a ground plane, a building, trees, a car, a road, and a flower box with randomized flowers. 
All objects are positioned using descriptive variable names, and colors are applied via a helper function. 
"""

#Importing the necessary module to use Maya's commands and the random module.
import maya.cmds as cmds
import random 

# ---------------------------------------------------------------------------
# Clear the scene so we start fresh each time the script runs.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.file(new=True, force=True)

# Ground Plane

ground_width = 50
ground_depth = 50
ground_y_position = 0

ground = cmds.polyPlane(
    name="ground_plane",
    width=ground_width,
    height=ground_depth,
    subdivisionsX=1,
    subdivisionsY=1,
)[0]

# Move the ground plane so its top surface sits at y=0.
cmds.move(0, ground_y_position, 0, ground)

# Example Object 1 -- a simple building (cube)
# This is provided as an example. Study it, then add your own objects below.

building_width = 4.2
building_height = 9
building_depth = 4.2
building_x = -8
building_z = 5

building = cmds.polyCube(
    name="building_01",
    width=building_width,
    height=building_height,
    depth=building_depth,
)[0]

cmds.move(building_x, building_height / 2.0, building_z, building)

# Object 2 : A tree (cylinder for trunk, and a sphere for foliage)

# Setting the variables for the trunk dimensions and position.
tree1_trunk_height = random.randint(2,7) # Random height for the first tree trunk to add some variation.
tree1_trunk_radius = 0.5
tree1_trunk_x = 5
tree1_trunk_z = -3
tree1_trunk = cmds.polyCylinder(
    name="tree_trunk_01",
    height=tree1_trunk_height,
    radius=tree1_trunk_radius,
    subdivisionsX=20,
    subdivisionsY=1,
    subdivisionsZ=1,
)[0]

# Moving the trunk so its base sits on the ground plane.
cmds.move(tree1_trunk_x, tree1_trunk_height / 2.0, tree1_trunk_z, tree1_trunk)

# Setting the variables for the foliage dimensions and position.
tree1_foliage_radius = 2
tree1_foliage_x = tree1_trunk_x
tree1_foliage_y = tree1_trunk_height + tree1_foliage_radius / 2
tree1_foliage_z = tree1_trunk_z
tree1_foliage = cmds.polySphere(
    name="tree_foliage_01",
    radius=tree1_foliage_radius,
    subdivisionsX=20,
    subdivisionsY=20,
)[0]

# Moving the foliage so that it sits on top of the trunk.
cmds.move(tree1_foliage_x, tree1_foliage_y, tree1_foliage_z, tree1_foliage)

# Object 3 : A second tree (A cylinder for trunk, and a cone for foliage)

# Using the same type for the trunk as the first tree, but changing the foliage to a cone for variety.
tree2_trunk_height = random.randint(2,6) # Random height for the second tree trunk to add some variation.
tree2_trunk_radius = 0.3
tree2_trunk_x = 5
tree2_trunk_z = 3
tree2_trunk = cmds.polyCylinder(
    name="tree_trunk_02",
    height=tree2_trunk_height,
    radius=tree2_trunk_radius,
    subdivisionsX=20,
    subdivisionsY=1,
    subdivisionsZ=1,
)[0]

# Moving the trunk so its base sits on the ground plane.
cmds.move(tree2_trunk_x, tree2_trunk_height / 2.0, tree2_trunk_z, tree2_trunk)

tree2_foliage_radius = 1.5
tree2_foliage_height = 3
tree2_foliage_x = tree2_trunk_x
tree2_foliage_y = tree2_trunk_height + tree2_foliage_height / 2
tree2_foliage_z = tree2_trunk_z
tree2_foliage = cmds.polyCone(
    name="tree_foliage_02",
    radius=tree2_foliage_radius,
    height=tree2_foliage_height,
    subdivisionsX=20,
    subdivisionsY=1,
)[0]
# Moving the foliage so that it sits on top of the trunk.
cmds.move(tree2_foliage_x, tree2_foliage_y, tree2_foliage_z, tree2_foliage)

# Object 4: An awning for the building (A polycube rotated to be a sloped roof with cylindrical columns under it.)

#Setting variables for the awning dimensions and position.
awning_width = 4
awning_height = 0.5
awning_depth = 4
awning_x = building_x + building_width/1.5
awning_y = building_height / 2
awning_z = building_z

# Creating the awning using a polyCube and naming it.
awning = cmds.polyCube(
    name="awning_01",
    width=awning_width,
    height=awning_height,
    depth=awning_depth,
)[0]

# Rotating the awning to create a sloped roof effect.
cmds.rotate(0, 0, -30, awning)

# Moving the awning so it sits on top of the building.
cmds.move(awning_x, awning_y, awning_z, awning)

# Setting the variables for the columns dimensions and position.
column_height = 3.5
column_radius = 0.2
column1_x = building_x + 4
column1_z = building_z - 1.5
column1 = cmds.polyCylinder(
    name="awning_column_01",
    height=column_height,
    radius=column_radius,
    subdivisionsX=20,
    subdivisionsY=1,
    subdivisionsZ=1,
)[0]

# Moving the first column so its base sits on the ground plane and is positioned just under the awning.
cmds.move(column1_x, column_height / 2.0, column1_z,
            column1)

# Creating the second column with the same dimensions as the first one and positioning it on the other side of the awning.
column2_x = building_x + 4
column2_z = building_z + 1.5
column2 = cmds.polyCylinder(
    name="awning_column_02",
    height=column_height,
    radius=column_radius,
    subdivisionsX=20,
    subdivisionsY=1,
    subdivisionsZ=1,
)[0]

# Moving the second column so its base sits on the ground plane and its positioned just under the awning.
cmds.move(column2_x, column_height / 2.0, column2_z,
            column2)

# Object 5: A car (polyCubes for the body, and rotated cylinders for the wheels)

# Setting the variables for the wheels dimensions and position.
wheel_radius = 0.5
wheel_height = 0.3
left_weel_x = 1
right_weel_x = -1
wheel_z = 0

# Creating the four wheels using polyCylinders and naming them.
wheel1 = cmds.polyCylinder(
    name="car_wheel_01",
    height=wheel_height,
    radius=wheel_radius,
    subdivisionsX=20,
    subdivisionsY=1,
    subdivisionsZ=1,
)[0]
wheel2 = cmds.polyCylinder(
    name="car_wheel_02",
    height=wheel_height,
    radius=wheel_radius,
    subdivisionsX=20,
    subdivisionsY=1,
    subdivisionsZ=1,
)[0]
wheel3 = cmds.polyCylinder(
    name="car_wheel_03",
    height=wheel_height,
    radius=wheel_radius,
    subdivisionsX=20,
    subdivisionsY=1,
    subdivisionsZ=1,
)[0]
wheel4 = cmds.polyCylinder(
    name="car_wheel_04",
    height=wheel_height,
    radius=wheel_radius,
    subdivisionsX=20,
    subdivisionsY=1,
    subdivisionsZ=1,
)[0]

# Rotating the wheels to lay flat on the ground.
for wheel in [wheel1, wheel2, wheel3, wheel4]:
    cmds.rotate(180, 0, 90, wheel)

# Moving the wheels so they sit on the ground plane and are positioned under where the car body will be.
cmds.move(left_weel_x, wheel_radius+0.1, wheel_z, wheel1)
cmds.move(left_weel_x, wheel_radius+0.1, wheel_z + 2.3, wheel2)
cmds.move(right_weel_x, wheel_radius+0.1, wheel_z, wheel3)
cmds.move(right_weel_x, wheel_radius+0.1, wheel_z + 2.3, wheel4)

# Setting the variables for the car body dimensions and position.
body_width = 2
body_height = 1
body_depth = 4.2
body_x = 0
body_y = wheel_radius + body_height / 2 + 0.1
body_z = 1.35

# Creating the car body using a polyCube and naming it.
car_body = cmds.polyCube(
    name="car_body_01",
    width=body_width,
    height=body_height,
    depth=body_depth,
)[0]

# Moving the car body so it sits on top of the wheels and is positioned correctly.
cmds.move(body_x, body_y, body_z, car_body)

#Making the front of the cab using an angled, thin polycube.
front_cab_width = 2
front_cab_height = 1
front_cab_depth = 0.2
front_cab_x = 0
front_cab_y = body_y + front_cab_height - 0.2
front_cab_z = body_z + 1.3
front_car_cab = cmds.polyCube(
    name="car_cab_01",
    width=front_cab_width,
    height=front_cab_height,
    depth=front_cab_depth,
)[0]

# Rotating the cab to create a sloped front windshield effect.
cmds.rotate(-30, 0, 0, front_car_cab)
# Moving the cab so it sits on top of the front of the car body and is positioned
cmds.move(front_cab_x, front_cab_y, front_cab_z, front_car_cab)

#Making the back of the cab using an angled, thin polycube.
back_cab_width = 2
back_cab_height = 1
back_cab_depth = 0.2
back_cab_x = 0
back_cab_y = body_y + back_cab_height - 0.2
back_cab_z = body_z - 1.7
back_car_cab = cmds.polyCube(
    name="car_cab_02",
    width=back_cab_width,
    height=back_cab_height,
    depth=back_cab_depth,
)[0]

# Rotating the cab to create a sloped back windshield effect.
cmds.rotate(30, 0, 0, back_car_cab)
# Moving the cab so it sits on top of the back of the car body and is positioned
cmds.move(back_cab_x, back_cab_y, back_cab_z, back_car_cab)

#Making the top of the cab using a flat, thin polycube.
top_cab_width = 2
top_cab_height = 0.2
top_cab_depth = 2.66
top_cab_x = 0
top_cab_y = body_y + 1.2
top_cab_z = body_z - 0.2
top_car_cab = cmds.polyCube(
    name="car_cab_03",
    width=top_cab_width,
    height=top_cab_height,
    depth=top_cab_depth,
)[0]

# Moving the cab so it sits on top of the car body and is positioned correctly.
cmds.move(top_cab_x, top_cab_y, top_cab_z, top_car_cab)

#Finally, making a cab divider using a thin polycube to separate the front and back of the cab.
divider_width = 2
divider_height = 0.8
divider_depth = 0.2
divider_x = 0
divider_y = body_y + 0.8
divider_z = body_z
cab_divider = cmds.polyCube(
    name="car_cab_divider_01",
    width=divider_width,
    height=divider_height,
    depth=divider_depth,
)[0]

# Moving the divider so it sits between the front and back cabs and is positioned correctly.
cmds.move(divider_x, divider_y, divider_z, cab_divider)

# (Optional): Add more objects to make your scene more interesting!

#First, adding a road that cuts in front of the building using a polyCube.
road_width = 7
road_height = 0.1
road_depth = 50
road_x = building_x + 8
road_y = road_height / 2
road_z = building_z - 5 
road = cmds.polyCube(
    name="road_01",
    width=road_width,
    height=road_height,
    depth=road_depth,
)[0]

# Moving the road so it sits on the ground plane and is positioned in front of the building.
cmds.move(road_x, road_y, road_z, road)
    
#Next, i'm duplicating tree 01 and tree 02 so they line the road.
tree_trunk_03 = cmds.duplicate("tree_trunk_01")[0]
cmds.move(5, tree1_trunk_height / 2, 9, "tree_trunk_03")
tree_foliage_03 = cmds.duplicate("tree_foliage_01")[0]
cmds.move(5, tree1_foliage_y, 9, tree_foliage_03)

tree_trunk_04 = cmds.duplicate("tree_trunk_02")[0]
cmds.move(5, tree2_trunk_height / 2, -9, "tree_trunk_04")
tree_foliage_04 = cmds.duplicate("tree_foliage_02")[0]
cmds.move(5, tree2_foliage_y, -9, tree_foliage_04)

#I want to add colors to my scene, and with some research i found that the best way to do so is to make a helper function.
def apply_color(obj, name, r, g, b):
    mat = cmds.shadingNode('lambert', asShader=True, name=name) #Creating a new lambert material with the specified name.
    cmds.setAttr(mat + ".color", r, g, b, type="double3") #Setting the color of the material using the provided RGB values.
    cmds.select(obj) #Selecting the object to which the material will be applied.
    cmds.hyperShade(assign=mat) #Applying the material to the selected object.

#Applying color to all the trees with a for loop.
for i in range(1, 5):
    trunk = cmds.ls(f"tree_trunk_0{i}")[0]
    foliage = cmds.ls(f"tree_foliage_0{i}")[0]
    
    apply_color(trunk, f"trunk_mat_{i}", random.randint(70,100)/255, random.randint(40,65)/255, random.randint(20,40)/255)
    apply_color(foliage, f"leaf_mat_{i}", random.randint(20,50)/255, random.randint(80,105)/255, random.randint(20,40)/255)

#Making the road dark gray using the helper function. 
apply_color(road, "road_mat", 0.1, 0.1, 0.1)
#Making the plane green using the helper function.
apply_color(ground, "ground_mat", 90/255, 160/255, 60/255)
#Making the building beige using the helper function.
apply_color(building, "building_mat", 210/255, 180/255, 140/255)
#Making the awning blue using the helper function.
apply_color(awning, "awning_mat", 73/255,157/255,208/255)

#Making the car wheels black.
for i in range(1, 5):
    wheel = cmds.ls(f"car_wheel_0{i}")[0]
    apply_color(wheel, f"wheel_mat_{i}", 0, 0, 0)

#Making the car body and cab red.
apply_color(car_body, "car_body_mat", 1, 0, 0)
apply_color(top_car_cab, "top_cab_mat", 1, 0, 0)
apply_color(front_car_cab, "front_cab_mat", 1, 0, 0)
apply_color(back_car_cab, "back_cab_mat", 1, 0, 0)
apply_color(cab_divider, "divider_mat", 1, 0, 0)

#Now, Im going to make a flower box. It will be made of four polycube walls and a polycube base to represent dirt inside. 
flower_box_width = 3 
flower_box_height = 0.5 
flower_box_depth = 6 
flower_box_x = building_x 
flower_box_y = flower_box_height / 2 
flower_box_z = building_z - 10 
flower_box_base = cmds.polyCube( name="flower_box_base", width=flower_box_width, height=flower_box_height, depth=flower_box_depth, )[0] 
cmds.move(flower_box_x, flower_box_y, flower_box_z, flower_box_base)

# Helper function to create one flower at a given x, z
def create_flower(x, z, name):
    flower_stem_height = 0.5
    flower_stem_radius = random.randint(5, 10) / 100
    # Stem
    flower_stem = cmds.polyCylinder(
        name=f"{name}_stem",
        height=flower_stem_height,
        radius=flower_stem_radius,
        subdivisionsX=20,
        subdivisionsY=1,
        subdivisionsZ=1,
    )[0]
    # y-coordinate = top of dirt
    stem_y = flower_box_y + flower_box_height / 2 + flower_stem_height / 2
    cmds.move(x, stem_y, z, flower_stem)

    # Flower head
    flower_head_radius = random.randint(1, 10) / 100
    flower_head = cmds.polySphere(
        name=f"{name}_head",
        radius=flower_head_radius,
        subdivisionsX=20,
        subdivisionsY=20,
    )[0]
    head_y = stem_y + flower_stem_height / 2 + flower_head_radius / 2
    cmds.move(x, head_y, z, flower_head)

    # Coloring the stem a random green and the flower head a random bright color.
    apply_color(flower_stem, f"{name}_stem_mat", random.randint(20,50)/255, random.randint(80,105)/255, random.randint(20,40)/255) # Green stem
    flower_colors = [(1, 0, 0), (1, 0.75, 0.8), (1, 1, 0), (1, 0.5, 0)]
    apply_color(flower_head, f"{name}_head_mat", *random.choice(flower_colors))

# Fill the flower box
for i in range(100):
    flower_x = random.uniform(flower_box_x - flower_box_width / 2 + 0.1,
                              flower_box_x + flower_box_width / 2 - 0.1)
    flower_z = random.uniform(flower_box_z - flower_box_depth / 2 + 0.1,
                              flower_box_z + flower_box_depth / 2 - 0.1)
    create_flower(flower_x, flower_z, f"flower_{i+1}")

#Finally, coloring the box brown.
apply_color(flower_box_base, "flower_box_mat", 88/255, 57/255, 39/255)

#Making a really tiny layer on top of the box to represent the soil surface, and coloring it a darker brown.
soil_layer = cmds.polyCube(
    name="soil_layer",
    width=flower_box_width - 0.4,
    height=0.1,
    depth=flower_box_depth - 0.4,
)[0]
cmds.move(flower_box_x, flower_box_y + flower_box_height / 2 + 0.05, flower_box_z, soil_layer)
apply_color(soil_layer, "soil_layer_mat", 40/255, 20/255, 10/255)

# ---------------------------------------------------------------------------
# Frame All -- so the whole scene is visible in the viewport.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.viewFit(allObjects=True)
print("Scene built successfully!")
