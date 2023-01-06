import os
import sys
import subprocess
import os
import shutil
class cd:                   #Allows changing directories
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)
def controlDict(start_time,end_time,delta_T):
    file = open("system/controlDict", "rt")
    data = file.read()
    data = data.replace('{}'.format("eee"), '{}'.format(str(start_time)))
    data = data.replace('{}'.format("ddd"), '{}'.format(str(end_time)))
    data = data.replace('{}'.format("fff"), '{}'.format(str(delta_T)))
    file.close()
    file = open("system/controlDict", "wt")
    file.write(data)
    file.close()
    print (data)
def transportProperties(nu,alpha,rho):
    file = open("constant/transportProperties", "rt")
    data = file.read()
    data = data.replace('{}'.format('aaa'), '{}'.format(str(nu)))
    data = data.replace('{}'.format('bbb'), '{}'.format(str(alpha)))
    data = data.replace('{}'.format('ccc'), '{}'.format(str(rho)))
    file.close()
    file = open("constant/transportProperties", "wt")
    file.write(data)
    file.close()
    print (data)
def SolidDict(gravity,mask,shape,radius,radiusa,radiusb,ratio,tail_thickness,number_of_particles,positions,rho_material,offset):
    if gravity == True:
        grave_value = -10.0
    else:
        grave_value = 0.0
    if len(str(mask)) != 6:
        print("mask is wrong")
    lines = ["FoamFile","{","    version     2.0;","    format      ascii;","    class       dictionary;",'    location    "constant";',"    object      solids;","}","meta","{","  on_fluid 1;","  on_twod  1;","  gravity  (0.0 {} 0.0);".format(grave_value),"}"]
    materials = ["\nmaterials","{","    material1","    {","      name mat1;","      type General;","      rho {};".format(rho_material),"    }","}"]   
    motions = ["\nmotions","{","    motion1","    {","      name mot;","      type Motion01Mask;","      mask b{};".format(mask),"    }","}"]
    planes = ["\nplanes","{","}"]
    shapes = ["\nshapes","{","    shape1","    {","        name shap;"]
    if shape == "circle":
        shapes = shapes + ["        type Circle;","        radius {};".format(radius),"    }","}"]
    elif shape == "circle-MP-DC-4p":
        shapes = shapes + ["        type Circle;","        radius {};".format(radius),"    }","}"]
    elif shape == "circle-MP-DC-3p":
        shapes = shapes + ["        type Circle;","        radius {};".format(radius),"    }","}"]
    elif shape == "ellipse":
        shapes = shapes + ["        type Ellipse;","        radiusa {};".format(radiusa),"        radiusb {};".format(radiusb),"        com (0 0 0);","    }","}"]
    elif shape == "Circle_Tail":
        shapes = shapes + ["        type Circle_Tail;","        radius {};".format(radius),"        ratio {};".format(ratio),"        thickness {};".format(tail_thickness),"    }","}"]
    else:
        print("shape wrong")
    solids = ["\nsolids","{",]
    if shape == "ellipse":                          #Specifically for my ellipitical periodic problem
        if offset == 0:
            for x in range(number_of_particles):
                if number_of_particles == 2:
                    if x == 0:
                        pos1 = .25 
                        pos2 = .25
                    if x == 1:
                        pos1 = .25 
                        pos2 = .75
                if number_of_particles == 4:
                    if x == 0:
                        pos1 = .25 
                        pos2 = .25
                    if x == 1:
                        pos1 = .25 
                        pos2 = .75
                    if x == 2:
                        pos1 = .75 
                        pos2 = .25
                    if x == 3:
                        pos1 = .75
                        pos2 = .75
                if number_of_particles == 6:
                    if x == 0:
                        pos1 = .25 
                        pos2 = .25
                    if x == 1:
                        pos1 = .25 
                        pos2 = .75
                    if x == 2:
                        pos1 = .75 
                        pos2 = .25
                    if x == 3:
                        pos1 = .75 
                        pos2 = .75
                    if x == 4:
                        pos1 = 1.25 
                        pos2 = .25
                    if x == 5:
                        pos1 = 1.25 
                        pos2 = .75
                solids = solids + ["    solid{}".format(x),"    {","     shp_name shap;","      mot_name mot;","      mat_name mat1;","      pos ({} {} 0.0);".format(pos1,pos2),"      vel (0.0 0.0 0.0);","      euler (0.0 0.0 -45.0);","    }"]
        if offset == 1:
            for x in range(number_of_particles):
                if number_of_particles == 2:
                    if x == 0:
                        pos1 = .45
                        pos2 = .25
                    if x == 1:
                        pos1 = .25 
                        pos2 = .75
                if number_of_particles == 4:
                    if x == 0:
                        pos1 = .25 
                        pos2 = .75
                    if x == 1:
                        pos1 = .45 
                        pos2 = .25
                    if x == 2:
                        pos1 = 1.15 
                        pos2 = .25
                    if x == 3:
                        pos1 = .95
                        pos2 = .75
                if number_of_particles == 6:
                    if x == 0:
                        pos1 = .25 
                        pos2 = .75
                    if x == 1:
                        pos1 = .45 
                        pos2 = .25
                    if x == 2:
                        pos1 = 1.15 
                        pos2 = .25
                    if x == 3:
                        pos1 = .95 
                        pos2 = .75
                    if x == 4:
                        pos1 = 1.85 
                        pos2 = .25
                    if x == 5:
                        pos1 = 1.65 
                        pos2 = .75
                solids = solids + ["    solid{}".format(x),"    {","     shp_name shap;","      mot_name mot;","      mat_name mat1;","      pos ({} {} 0.0);".format(pos1,pos2),"      vel (0.0 0.0 0.0);","      euler (0.0 0.0 -45.0);","    }"] 
        if offset == 2:
            for x in range(number_of_particles):
                if number_of_particles == 2:
                    if x == 0:
                        pos1 = .65
                        pos2 = .25
                    if x == 1:
                        pos1 = .25 
                        pos2 = .75
                if number_of_particles == 4:
                    if x == 0:
                        pos1 = .65 
                        pos2 = .25
                    if x == 1:
                        pos1 = .25 
                        pos2 = .75
                    if x == 2:
                        pos1 = 1.15 
                        pos2 = .75
                    if x == 3:
                        pos1 = 1.55
                        pos2 = .25
                if number_of_particles == 6:
                    if x == 0:
                        pos1 = .65
                        pos2 = .25
                    if x == 1:
                        pos1 = .25 
                        pos2 = .75
                    if x == 2:
                        pos1 = 1.15
                        pos2 = .75
                    if x == 3:
                        pos1 = 1.55 
                        pos2 = .25
                    if x == 4:
                        pos1 = 2.45 
                        pos2 = .25
                    if x == 5:
                        pos1 = 2.05
                        pos2 = .75
                solids = solids + ["    solid{}".format(x),"    {","     shp_name shap;","      mot_name mot;","      mat_name mat1;","      pos ({} {} 0.0);".format(pos1,pos2),"      vel (0.0 0.0 0.0);","      euler (0.0 0.0 -45.0);","    }"] 
        if offset == 3:
            for x in range(number_of_particles):
                if number_of_particles == 2:
                    if x == 0:
                        pos1 = .85
                        pos2 = .25
                    if x == 1:
                        pos1 = .25 
                        pos2 = .75
                if number_of_particles == 4:
                    if x == 0:
                        pos1 = .85 
                        pos2 = .25
                    if x == 1:
                        pos1 = .25 
                        pos2 = .75
                    if x == 2:
                        pos1 = 1.35 
                        pos2 = .75
                    if x == 3:
                        pos1 = 1.95
                        pos2 = .25
                if number_of_particles == 6:
                    if x == 0:
                        pos1 = .85 
                        pos2 = .25
                    if x == 1:
                        pos1 = .25 
                        pos2 = .75
                    if x == 2:
                        pos1 = 1.35 
                        pos2 = .75
                    if x == 3:
                        pos1 = 1.95 
                        pos2 = .25
                    if x == 4:
                        pos1 = 2.45 
                        pos2 = .75
                    if x == 5:
                        pos1 = 3.05 
                        pos2 = .25
                solids = solids + ["    solid{}".format(x),"    {","     shp_name shap;","      mot_name mot;","      mat_name mat1;","      pos ({} {} 0.0);".format(pos1,pos2),"      vel (0.0 0.0 0.0);","      euler (0.0 0.0 -45.0);","    }"]  
    elif shape == "circle-MP-DC-4p":
        for x in range(number_of_particles):
            if number_of_particles == 4:
                if x == 0:
                    pos1 = .5 
                    pos2 = .25
                if x == 1:
                    pos1 = .5 
                    pos2 = .75
                if x == 2:
                    pos1 = .75 
                    pos2 = .5
                if x == 3:
                    pos1 = .25
                    pos2 = .5
            solids = solids + ["    solid{}".format(x),"    {","     shp_name shap;","      mot_name mot;","      mat_name mat1;","      pos ({} {} 0.0);".format(pos1,pos2),"      vel (0.0 0.0 0.0);","      euler (0.0 0.0 -45.0);","    }"] 
    elif shape == "circle-MP-DC-3p":
        for x in range(number_of_particles):
            if number_of_particles == 3:
                if x == 0:
                    pos1 = .4 
                    pos2 = .3
                if x == 1:
                    pos1 = .4 
                    pos2 = .7
                if x == 2:
                    pos1 = .6
                    pos2 = .5
            solids = solids + ["    solid{}".format(x),"    {","     shp_name shap;","      mot_name mot;","      mat_name mat1;","      pos ({} {} 0.0);".format(pos1,pos2),"      vel (0.0 0.0 0.0);","      euler (0.0 0.0 -45.0);","    }"]
    else:
        y = 0
        for x in range(number_of_particles):
            pos1 = positions[y]
            pos2 = positions[y+1]
            solids = solids + ["    solid{}".format(x),"    {","     shp_name shap;","      mot_name mot;","      mat_name mat1;","      pos ({} {} 0.0);".format(pos1,pos2),"      vel (0.0 0.0 0.0);","      euler (0.0 0.0 -45.0);","    }"]
            y = y + 2 
    solids = solids + ["}"]
    file = open("solidDict","w")
    file.write('\n'.join(lines))
    file.write('\n'.join(materials))
    file.write('\n'.join(motions))
    file.write('\n'.join(shapes))
    file.write('\n'.join(solids))
    file.write('\n'.join(planes))
def MeshSizes(nx,ny,xmin,xmax,ymin,ymax):
    file = open("constant/polyMesh/blockMeshDict", "rt")
    data = file.read()
    data = data.replace('{}'.format("aaa"), '{}'.format(xmin))
    data = data.replace('{}'.format("bbb"), '{}'.format(xmax))
    data = data.replace('{}'.format("ccc"), '{}'.format(ymin))
    data = data.replace('{}'.format("ddd"), '{}'.format(ymax))
    data = data.replace('{}'.format("eee"), '{}'.format(nx))
    data = data.replace('{}'.format("fff"), '{}'.format(ny))
    file.close()
    file = open("constant/polyMesh/blockMeshDict", "wt")
    file.write(data)
    file.close() 
def Main(start_time,end_time,delta_T,nu,alpha,rho,gravity,mask,shape,radius,radiusa,radiusb,ratio,tail_thickness,number_of_particles,positions,nx,ny,xmin,xmax,ymin,ymax,rho_material,offset):
    """
    

    Parameters
    ----------
    start_time : start time (has to be 0)
    end_time : any end time
    delta_T : time step
    nu : kinematic visocity
    alpha : Thermal Diffusivity
    rho : Density of the Fluid
    gravity : True or False (True = -10; False = 0)
    mask : mask which specifics rotation and movement in SolidDict
    shape : So far has ellipse (Periodic Ellipse),Circle_Tail (Dr. Nitin), Circle, circle-MP-DC-4p (Dr.Tiara), circle-MP-DC-3p (Dr.Tiara)
    radius : only for circle, circle-MP-DC-4p (Dr.Tiara), circle-MP-DC-3p (Dr.Tiara)
    radiusa : only for ellipse (Periodic Ellipse)
    radiusb : only for ellipse (Periodic Ellipse)
    ratio : only for Circle_Tail (Dr. Nitin)
    tail_thickness : only for Circle_Tail (Dr. Nitin)
    number_of_particles : number of particles
    positions : if shape is ellipse (Periodic Ellipse);Circle, circle-MP-DC-4p (Dr.Tiara); circle-MP-DC-3p (Dr.Tiara) then shape already predetermined and can just place 0
    nx : Number of cells in the X direction
    ny : number of cells in the Y direction
    xmin : small length in x direction
    xmax : large length value in x direction
    ymin : small length value in y direction
    ymax : large length value in y direction
    rho_material : density of the particle
    offset: 0 for false; 1 for true (Periodic Ellipse)
    -------

    """
    if shape == "ellipse":
        ellipse_ratio = (radiusa / radiusb)
        print(ellipse_ratio)
        name = 'Ellipse_Cavity-{}-{}-{}'.format(number_of_particles,int(1/nu),offset)
    if shape == "Circle_Tail":
        name = "Circle_Tail-Re{}".format(int(1/nu))
    if shape == "circle":
        name = "Circle-Re{}".format(int(1/nu))
    if shape == "circle-MP-DC-4p":
        name = "MP-DC-SampleCase-4p-{}".format((1/nu))
    if shape == "circle-MP-DC-3p":
        name = "MP-DC-SampleCase-3p-{}".format((1/nu))
    with cd("Automation"):
        try:
            shutil.copytree('Base_{}'.format(shape), '{}'.format(name))
        except:
            pass
        with cd('{}'.format(name)):
            controlDict(start_time,end_time,delta_T)
            transportProperties(nu,alpha,rho)
            SolidDict(gravity,mask,shape,radius,radiusa,radiusb,ratio,tail_thickness,number_of_particles,positions,rho_material,offset)
            if shape != "Circle_Tail":
                MeshSizes(nx,ny,xmin,xmax,ymin,ymax)
            #subprocess.run('nohup blockMesh')
            #subprocess.run('nohup sdfibm &')
    return

"""
For Running Periodic Ellipse
Main(0,500,.001,Re,.0001,1,False,"000001","ellipse",0,.2,.1,0,0,2,0,200,400,0,.5,0,1,1.1,0) 
Main(0,500,.001,Re,.0001,1,False,"000001","ellipse",0,.2,.1,0,0,4,0,400,400,0,1,0,1,1.1,0) 
Main(0,500,.001,Re,.0001,1,False,"000001","ellipse",0,.2,.1,0,0,6,0,600,400,0,1.5,0,1,1.1,0) 

"""

"""
For Running Driven Cavity Problem
Main(0,250,.001,Re,.0001,1,False,"110001","circle-MP-DC-4p",0.05,0,0,0,0,4,0,400,400,0,1,0,1,1.05)
Main(0,250,.001,Re,.0001,1,False,"110001","circle-MP-DC-3p",0.05,0,0,0,0,3,0,400,400,0,1,0,1,1.05)

"""

