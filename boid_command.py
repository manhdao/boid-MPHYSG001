#!/usr/bin/env python
from argparse import ArgumentParser
from boids import update_boids
from simulate import simulate
import yaml
import numpy as np


with open('config.yaml', 'rb') as f:
    conf = yaml.load(f.read())    # load the config file

flock_params = conf['flock_params']
boid_params = conf['boid_params']
animation_params = conf['animation_params']

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


#generate boids
positions = np.array([min_x_position,min_y_position])[:,np.newaxis] + \
			np.random.rand(2, boid_count)*(np.array([max_x_position,max_y_position]) - np.array([min_x_position,min_y_position]))[:,np.newaxis]
velocities = np.array([min_x_velocity,min_y_velocity])[:,np.newaxis] + \
			np.random.rand(2, boid_count)*(np.array([max_x_velocity,max_y_velocity]) - np.array([min_x_velocity,min_y_velocity]))[:,np.newaxis]


if __name__ == "__main__":



	simulate(animation_params, positions, velocities)






