import boids as bs
from nose.tools import assert_equal
import os
import yaml


def test_update_boids():
	#Test the update_boids function
    boid_data=yaml.load(open(
        os.path.join(os.path.dirname(__file__),
        'update_boids_fixture.yaml')))
    before=boid_data["before"]
    bs.update_boids(before)
    assert_equal(boid_data["after"],before)