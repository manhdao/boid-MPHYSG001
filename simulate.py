from matplotlib import pyplot as plt
from matplotlib import animation
from model import Flock
import yaml


def simulate(animation_params, boids):
    axes_min, axes_max = animation_params['axes_min'], animation_params['axes_max']

    figure = plt.figure()
    axes = plt.axes(xlim=(axes_min, axes_max), ylim=(axes_min, axes_max))
    scatter = axes.scatter(boids[0], boids[1])

    def animate(frame):
        update_boids(boids)
        boid_zip = list(zip(boids[0],boids[1]))
        scatter.set_offsets(boid_zip)

    anim = animation.FuncAnimation(figure, animate, frames=animation_params['frames'],
                                        interval=animation_params['interval'])
    
    plt.show()