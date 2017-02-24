from boids import Flock
from nose.tools import assert_equal
import os
import numpy as np
import yaml
from unittest.mock import patch, MagicMock


#@patch.object(Flock'boids.Flock')
def test_fly_middle():
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


def test_fly_away():
	#Test the fly_away function
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


def test_match_speed():
	#Test the match_speed function
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
	#Test the update_boids function
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