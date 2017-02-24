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


if __name__ == "__main__":
	simulate(animation_params, flock_params, boid_params)






