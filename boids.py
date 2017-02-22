from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random
import yaml

with open('config.yaml', 'rb') as f:
    conf = yaml.load(f.read())    # load the config file

flock_params = conf['flock_params']
boid_params = conf['boid_params']

#boid_params
min_x_position = boid_params['min_x_position']
max_x_position= boid_params['max_x_position']
min_y_position= boid_params['min_y_position']
max_y_position = boid_params['max_y_position']
min_x_velocity = boid_params['min_x_velocity']
max_x_velocity = boid_params['max_x_velocity']
min_y_velocity = boid_params['min_y_velocity']
max_y_velocity = boid_params['max_y_velocity']

#flock_params
boid_count = flock_params['boid_count']
fly_middle_strength = flock_params['fly_middle_strength']
nearby_distance = flock_params['nearby_distance']
formation_distance = flock_params['formation_distance']
speed_formation_strength = flock_params['speed_formation_strength']


def fly_middle(boids):
	xs,ys,xvs,yvs=boids

	# Fly towards the middle
	middle_x = np.mean(xs)
	x_direction_to_middle = xs - middle_x
	middle_y = np.mean(ys)
	y_direction_to_middle = ys - middle_y

	xvs -= x_direction_to_middle * fly_middle_strength
	yvs -= y_direction_to_middle * fly_middle_strength


def fly_away(boids):
	xs,ys,xvs,yvs=boids

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



def match_speed(boids):
	xs,ys,xvs,yvs=boids

	# Try to match speed with nearby boids
	separations_x = xs[np.newaxis,:] - xs[:,np.newaxis]
	distances_x = separations_x * separations_x
	separations_y = ys[np.newaxis,:] - ys[:,np.newaxis]
	distances_y = separations_y * separations_y
	sum_distances = distances_x + distances_y

	formations_far = sum_distances > formation_distance
	velocity_difference_x = xvs[np.newaxis,:] - xvs[:,np.newaxis]
	velocity_difference_y = yvs[np.newaxis,:] - yvs[:,np.newaxis]
	velocity_if_close_x = np.copy(velocity_difference_x)
	velocity_if_close_x[:,:][formations_far] =0
	velocity_if_close_y = np.copy(velocity_difference_y)
	velocity_if_close_y[:,:][formations_far] =0

	xvs -= np.mean(velocity_if_close_x, axis=0) * speed_formation_strength
	yvs -= np.mean(velocity_if_close_y, axis=0) * speed_formation_strength

	xs += xvs
	ys += yvs



def update_boids(boids):
    fly_middle(boids)
    fly_away(boids)
    match_speed(boids)