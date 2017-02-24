#!/usr/bin/env python
from argparse import ArgumentParser
from boids import Flock
from simulate import simulate
import yaml
import numpy as np


with open('config.yaml', 'rb') as f:
    conf = yaml.load(f.read())    # load the config file

flock_params = conf['flock_params']
boid_params = conf['boid_params']
animation_params = conf['animation_params']


def process()
	parser = ArgumentParser(description = 'Implement a flock of boids')
	parser.add_argument('-n', '--number', required=False, help='Number of boids', dest='number')
	parser.add_argument('-a', '--action', required=False, dest='action',
		help='Specify the action: fly_middle, fly_away, match_speed. Default is update_boids')

	args = parser.parse_args()

	if args.number:
		#Update flock_params with new boid count
		flock_params['boid_count'] = args.number 

	simulate(animation_params, flock_params, boid_params, args.action)

if __name__ == "__main__":
	process()



