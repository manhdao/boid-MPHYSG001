from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random
import yaml


def update_boids(boids):
    xs,ys,xvs,yvs=boids

    # Fly towards the middle
    middle_x = np.mean(xs)
    x_direction_to_middle = xs - middle_x
    xvs -= x_direction_to_middle * fly_middle_strength

    middle_y = np.mean(ys)
    y_direction_to_middle = ys - middle_y
    yvs -= y_direction_to_middle * fly_middle_strength
            
        
    # Fly away from nearby boids
    separations_x = xs[np.newaxis,:] - xs[:,np.newaxis]
    distances_x = separations_x * separations_x
    separations_y = ys[np.newaxis,:] - ys[:,np.newaxis]
    distances_y = separations_y * separations_y
    sum_distances = distances_x + distances_y
    faraway = sum_distances > nearby_distance
    separations_if_close_x = np.copy(separations_x)
    separations_if_close_x[:,:][faraway] =0
    separations_if_close_y = np.copy(separations_y)
    separations_if_close_y[:,:][faraway] =0
    xvs += np.sum(separations_if_close_x,1)
    yvs += np.sum(separations_if_close_y,1)
    
    
    # Try to match speed with nearby boids
    formations_far = sum_distances > formation_distance
    velocity_difference_x = xvs[np.newaxis,:] - xvs[:,np.newaxis]
    velocity_difference_y = yvs[np.newaxis,:] - yvs[:,np.newaxis]
    velocity_if_close_x = np.copy(velocity_difference_x)
    velocity_if_close_x[:,:][formations_far] =0
    velocity_if_close_y = np.copy(velocity_difference_y)
    velocity_if_close_y[:,:][formations_far] =0
    xvs -= np.mean(velocity_if_close_x, axis=0) * speed_formation_strength
    yvs -= np.mean(velocity_if_close_y, axis=0) * speed_formation_strength

                
    # Move according to velocities
    xs += xvs
    ys += yvs