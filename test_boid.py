import boid_original as bo
import boids as bs
from nose.tools import assert_equal
import os
import yaml

"""
def test_update_boid_original():
    boid_data=yaml.load(open('update_boid_fixture.yaml'))
    before=boid_data["before"]
    bo.update_boids(before)
    assert_equal(boid_data["after"],before)
"""

def test_update_boids():
	#Test the update_boids function
    boid_data=yaml.load(open('update_boids_fixture.yaml'))
    before=boid_data["before"]
    bs.update_boids(before)
    assert_equal(boid_data["after"],before)