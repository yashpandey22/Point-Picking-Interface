import numpy as np
import copy
import open3d as o3d
import subprocess
import os

def pick_points(pcd):
    vis = o3d.visualization.VisualizerWithEditing()
    vis.create_window()
    vis.add_geometry(pcd)
    vis.run()  # user picks points
    vis.destroy_window()
    return vis.get_picked_points()

path = input(r"Enter the path of point cloud: ")
while(os.path.exists(path) == False):
    path = input("Path entered does not exists, please enter again: ")
    
pcd = o3d.io.read_point_cloud(path)
pick_points(pcd)

