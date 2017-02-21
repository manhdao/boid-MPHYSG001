from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random
import yaml

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

#aniation params
axes_min = animation_params['axes_min']
axes_max = animation_params['axes_max']
frames = animation_params['frames']
interval = animation_params['interval']


# Deliberately terrible code for teaching purposes
boids_x = (np.ones(boid_count)*min_x_position + np.random.rand(1, boid_count)*(max_x_position-min_x_position))
boids_y = (np.ones(boid_count)*min_y_position + np.random.rand(1, boid_count)*(max_y_position-min_y_position))
boid_x_velocities=(np.ones(boid_count)*min_x_velocity + np.random.rand(1, boid_count)*(max_x_velocity-min_x_velocity))
boid_y_velocities=(np.ones(boid_count)*min_y_velocity + np.random.rand(1, boid_count)*(max_y_velocity-min_y_velocity))

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
    xvs -= np.mean(velocity_if_close_x, axis=0) * speed_formation_strength
    yvs -= np.mean(velocity_if_close_y, axis=0) * speed_formation_strength

                
    # Move according to velocities
    xs += xvs
    ys += yvs

figure=plt.figure()
axes=plt.axes(xlim=(axes_min,axes_max), ylim=(axes_min,axes_max))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   boid_zip = list(zip(boids[0],boids[1]))
   scatter.set_offsets(boid_zip)


anim = animation.FuncAnimation(figure, animate, frames=frames, interval=interval)

if __name__ == "__main__":
	plt.show()