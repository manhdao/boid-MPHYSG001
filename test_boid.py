import boids as bs
from nose.tools import assert_equal
import os
import numpy as np
import yaml


def test_update_boids():
	#Test the update_boids function
    boid_data=yaml.load(open(
        os.path.join(os.path.dirname(__file__),
        'update_boid_fixture.yaml')))
    before=np.asarray(boid_data['before'])
    pos = before[0:2,:]
    vel = before[2:4,:]
    bs.update_boids(pos,vel)
    after = np.concatenate((pos, vel),axis=0)
    assert_equal(np.asarray(boid_data['after'][3,8]),after[3,8])