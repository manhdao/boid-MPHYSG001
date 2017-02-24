from matplotlib import pyplot as plt
from matplotlib import animation
from boids import Flock


def simulate(animation_params, flock_params, boid_params):
    flock = Flock(flock_params, boid_params)
    axes_min, axes_max = animation_params['axes_min'], animation_params['axes_max']

    figure = plt.figure()
    axes = plt.axes(xlim=(axes_min, axes_max), ylim=(axes_min, axes_max))
    scatter = axes.scatter(flock.positions[0], flock.positions[1])

    def animate(frame):
        flock.update_boids()
        scatter.set_offsets(flock.positions.transpose())

    anim = animation.FuncAnimation(figure, animate, frames=animation_params['frames'],
                                        interval=animation_params['interval'])
    
    plt.show()