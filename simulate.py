from matplotlib import pyplot as plt
from matplotlib import animation
from boids import update_boids
import yaml


def simulate(animation_params, positions, velocities):
    axes_min, axes_max = animation_params['axes_min'], animation_params['axes_max']

    figure = plt.figure()
    axes = plt.axes(xlim=(axes_min, axes_max), ylim=(axes_min, axes_max))
    scatter = axes.scatter(positions[0,:], positions[1,:])

    def animate(frame):
        update_boids(positions, velocities)
        scatter.set_offsets(positions.transpose())

    anim = animation.FuncAnimation(figure, animate, frames=animation_params['frames'],
                                        interval=animation_params['interval'])
    
    plt.show()