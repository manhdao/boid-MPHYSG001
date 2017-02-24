from .boids import Flock
from nose.tools import assert_equal, assert_true
import os
import numpy as np
import yaml

with open('config.yaml', 'rb') as f:
    conf = yaml.load(f.read())    # load the config file

flock_params = conf['flock_params']
boid_params = conf['boid_params']
animation_params = conf['animation_params']

def test_initialize_flock_helper():
	"""Test shape of array and whether the values are in range"""

	test_flock = Flock(flock_params, boid_params)
	assert_equal(test_flock.positions.shape, (2,flock_params['boid_count']))

	assert_true(test_flock.positions[0,0] <= 50)

	assert_true(test_flock.velocities[0,10] >= 0)


def test_fly_middle_helper():
	"""Test the fly_middle function"""

	boid_data=yaml.load(open(
        os.path.join(os.path.dirname(__file__),
        'fixture\\fly_middle_fixture.yaml')))
	before=np.asarray(boid_data['before'])
	pos = before[0:2,:]
	vel = before[2:4,:]

	Flock.fly_middle_helper(pos,vel,fly_middle_strength = 0.01)

	after = np.concatenate((pos, vel),axis=0)

	#Test 2 particular numbers in the 2 velocity arrays
	assert_equal(np.asarray(boid_data['after'])[2,5],after[2,5])
	assert_equal(np.asarray(boid_data['after'])[3,20],after[3,20])


def test_fly_away_helper():
	"""Test the fly_away function"""

	boid_data=yaml.load(open(
        os.path.join(os.path.dirname(__file__),
        'fixture\\fly_away_fixture.yaml')))
	before=np.asarray(boid_data['before'])
	pos = before[0:2,:]
	vel = before[2:4,:]
	Flock.fly_away_helper(pos,vel,100)
	after = np.concatenate((pos, vel),axis=0)

	#Test 2 particular numbers in the 2 velocity arrays
	assert_equal(np.asarray(boid_data['after'])[2,28],after[2,28])
	assert_equal(np.asarray(boid_data['after'])[2,3],after[2,3])


def test_match_speed_helper():
	"""Test the match_speed function"""

	boid_data=yaml.load(open(
        os.path.join(os.path.dirname(__file__),
        'fixture\\match_speed_fixture.yaml')))
	before=np.asarray(boid_data['before'])
	pos = before[0:2,:]
	vel = before[2:4,:]
	Flock.match_speed_helper(pos,vel,10000,0.125)
	after = np.concatenate((pos, vel),axis=0)

	#Test 2 particular numbers in the 2 arrays
	assert_equal(np.asarray(boid_data['after'])[3,25],after[3,25])
	assert_equal(np.asarray(boid_data['after'])[0,7],after[0,7])


def test_update_boids():
	"""Test the update_boids function"""

	boid_data=yaml.load(open(
        os.path.join(os.path.dirname(__file__),
        'fixture\\update_boid_fixture.yaml')))
	before=np.asarray(boid_data['before'])
	pos = before[0:2,:]
	vel = before[2:4,:]

	Flock.update_boids_helper(pos,vel,0.01,100,10000,0.125)
	after = np.concatenate((pos, vel),axis=0)

    #Test 2 particular numbers in the 2 arrays
	assert_equal(np.asarray(boid_data['after'])[3,8],after[3,8])
	assert_equal(np.asarray(boid_data['after'])[0,6],after[0,6])