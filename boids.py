from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random

boid_count = 50
fly_middle_strength = 0.01
speed_formation_strength = 0.125
limit_x = [-450.0, 50.0]
limit_y = [300.0,600.0]
limit_velo_x = [0,10.0]
limit_velo_y = [-20.0,20.0]
nearby_distance = 100
formation_distance = 10000

# Deliberately terrible code for teaching purposes
boids_x = (np.ones(boid_count)*(limit_x[0]) + np.random.rand(1, boid_count)*(limit_x[1]-limit_x[0]))
boids_y = (np.ones(boid_count)*(limit_y[0]) + np.random.rand(1, boid_count)*(limit_y[1]-limit_y[0]))
boid_x_velocities=(np.ones(boid_count)*(limit_velo_x[0]) + np.random.rand(1, boid_count)*(limit_velo_x[1]-limit_velo_x[0]))
boid_y_velocities=(np.ones(boid_count)*(limit_velo_y[0]) + np.random.rand(1, boid_count)*(limit_velo_y[1]-limit_velo_y[0]))

boids = np.concatenate((boids_x,boids_y,boid_x_velocities,boid_y_velocities),axis = 0)


def update_boids(boids):
    xs,ys,xvs,yvs=boids

    # Fly towards the middle
    middle_x = np.mean(xs)
    x_direction_to_middle = xs - middle_x
    xvs -= x_direction_to_middle * fly_middle_strength

    middle_y = np.mean(ys)
    y_direction_to_middle = ys - middle_y
    yvs -= y_direction_to_middle * fly_middle_strength
            
        
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
    
    
    # Try to match speed with nearby boids
    formations_far = sum_distances > formation_distance
    velocity_difference_x = xvs[np.newaxis,:] - xvs[:,np.newaxis]
    velocity_difference_y = yvs[np.newaxis,:] - yvs[:,np.newaxis]
    velocity_if_close_x = np.copy(velocity_difference_x)
    velocity_if_close_x[:,:][formations_far] =0
    velocity_if_close_y = np.copy(velocity_difference_y)
    velocity_if_close_y[:,:][formations_far] =0
    xvs -= np.mean(velocity_difference_x) * speed_formation_strength
    yvs -= np.mean(velocity_difference_y) * speed_formation_strength

                
    # Move according to velocities
    xs += xvs
    ys += yvs

figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   boid_zip = list(zip(boids[0],boids[1]))
   scatter.set_offsets(boid_zip)


anim = animation.FuncAnimation(figure, animate, frames=200, interval=50)

if __name__ == "__main__":
	plt.show()