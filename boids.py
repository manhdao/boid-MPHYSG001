from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random
import yaml

with open('config.yaml', 'rb') as f:
    conf = yaml.load(f.read())    # load the config file

flock_params = conf['flock_params']
boid_params = conf['boid_params']

#flock_params
boid_count = flock_params['boid_count']
fly_middle_strength = flock_params['fly_middle_strength']
nearby_distance = flock_params['nearby_distance']
formation_distance = flock_params['formation_distance']
speed_formation_strength = flock_params['speed_formation_strength']


def fly_middle(positions, velocities):
	positions=np.asarray(positions)
	velocities=np.asarray(velocities)

	# Fly towards the middle
	middle = np.mean(positions, 1)
	direction_to_middle = positions - middle[:,np.newaxis]
	velocities -= direction_to_middle * fly_middle_strength


def fly_away(positions, velocities):
	positions=np.asarray(positions)
	velocities=np.asarray(velocities)

	# Fly away from nearby boids
	separations = positions[:,np.newaxis,:] - positions[:,:,np.newaxis]
	distances = separations * separations
	sum_distances = np.sum(distances, 0)

	far_away = sum_distances > nearby_distance
	separations_if_close = np.copy(separations)
	separations_if_close[0,:,:][far_away]= 0
	separations_if_close[1,:,:][far_away]= 0

	velocities += np.sum(separations_if_close,1)



def match_speed(positions, velocities):
	positions=np.asarray(positions)
	velocities=np.asarray(velocities)

	# Try to match speed with nearby boids
	separations = positions[:,np.newaxis,:] - positions[:,:,np.newaxis]
	distances = separations * separations
	sum_distances = np.sum(distances, 0)

	formations_far = sum_distances > formation_distance
	velocity_difference = velocities[:,np.newaxis,:] - velocities[:,:,np.newaxis]

	velocity_if_close = np.copy(velocity_difference)
	velocity_if_close[0,:,:][formations_far]= 0
	velocity_if_close[1,:,:][formations_far]= 0

	velocities -= np.mean(velocity_if_close, 1) * speed_formation_strength

	positions += velocities



def update_boids(positions, velocities):
    fly_middle(positions, velocities)
    fly_away(positions, velocities)
    match_speed(positions, velocities)