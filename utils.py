"""
utility functions used for landslide use case
"""
import os
import numpy as np
import xesmf as xe


# installation function
def install_api_key():
    home_dir = os.path.expanduser('~')
    work_dir = os.getcwd()

    # create Topography API key file
    topo_key = input('Enter Your OpenTopography API Key: ')
    topo_config_path = os.path.join(work_dir,'.opentopography.txt')

    with open(topo_config_path,'w') as topo_config_file:
        topo_config_file.write(topo_key)
    print('OpenTopography API Key file is created at {}.'.format(topo_config_path))

    # create CDS API key file
    cds_key = input('Enter Your CDS API Key: ')
    cds_url = 'https://cds.climate.copernicus.eu/api/v2'
    cds_config_content = 'url: {} \nkey: {}'.format(cds_url, cds_key)
    cds_config_path = os.path.join(home_dir, '.cdsapirc')

    with open(cds_config_path, 'w') as cds_config_file:
        cds_config_file.write(cds_config_content)

    print('CDS API Key file is created at {}'.format(cds_config_path))


# regirdding function
def regrid_data(src_grid, src_coor, dest_coor, regrid_method='nearest_s2d'):
    regridder = xe.Regridder(src_coor, dest_coor, regrid_method)
    dest_grid = regridder(src_grid)

    return dest_grid


# calculate subsurface flow function
def cal_subsurface_flow_depth(soil_depth, soil_water_layer, layer_threshold=[0, 0.07, 0.28, 1, 2], porosity=0.5):
    shape = [len(soil_water_layer), *soil_depth.shape]
    soil_depth_layer = np.empty(shape, soil_depth.dtype)

    for i in range(0, len(soil_water_layer)):
        soil_layer = np.copy(soil_depth)
        soil_layer[soil_layer >= layer_threshold[i + 1]] = layer_threshold[i + 1]
        soil_layer[soil_layer <= layer_threshold[i]] = layer_threshold[i]
        soil_layer = soil_layer - layer_threshold[i]
        soil_depth_layer[i] = soil_layer

    water_depth_layer = soil_water_layer * soil_depth_layer/porosity

    subsurface_flow_depth = np.sum(water_depth_layer, axis=0)

    return subsurface_flow_depth


# define safety factor function
def cal_safety_factor(slope_angle, subsurface_flow_depth, soil_depth,
                      root_cohesion=5000, soil_cohesion=5000, soil_bulk_density=1300,
                      water_density=1000, gravity_acceleration=9.806,
                      soil_internal_friction_angle=35):

    # calculate tan φ
    tan_fi = np.tan(soil_internal_friction_angle * np.pi / 180) 

    # calculate hw/hs
    relative_wetness = subsurface_flow_depth / soil_depth 

    # left term
    left_term = (root_cohesion + soil_cohesion) / (soil_depth * soil_bulk_density * gravity_acceleration) / np.sin(
        slope_angle)

    # right term
    right_term = np.cos(slope_angle) * tan_fi * (1 - relative_wetness * water_density / soil_bulk_density) / np.sin(
        slope_angle)

    # safety factor
    safety_factor = left_term + right_term

    return safety_factor
