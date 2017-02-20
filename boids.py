from matplotlib import pyplot as plt
from matplotlib import animation
import random
#plt.rcParams['animation.ffmpeg_path'] ='D:\\ffmpeg\\bin\\ffmpeg.exe'

boid_count = 50
fly_strength = 0.01
speed_formation_strength = 0.125
limit_x = [-450.0, 50.0]
limit_y = [300.0,600.0]
limit_velo_x = [0,10.0]
limit_velo_y = [-20.0,20.0]
nearby_distance = 100
formation_distance = 10000

# Deliberately terrible code for teaching purposes
boids_x=[random.uniform(limit_x[0],limit_x[1]) for x in range(boid_count)]
boids_y=[random.uniform(limit_y[0],limit_y[1]) for x in range(boid_count)]
boid_x_velocities=[random.uniform(limit_velo_x[0],limit_velo_x[1]) for x in range(boid_count)]
boid_y_velocities=[random.uniform(limit_velo_y[0],limit_velo_y[1]) for x in range(boid_count)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

def update_boids(boids):
    xs,ys,xvs,yvs=boids
    # Fly towards the middle
    for i in range(len(xs)):
        for j in range(len(xs)):
            xvs[i]=xvs[i]+(xs[j]-xs[i])*fly_strength/len(xs)
    for i in range(len(xs)):
        for j in range(len(xs)):
            yvs[i]=yvs[i]+(ys[j]-ys[i])*fly_strength/len(xs)
    # Fly away from nearby boids
    for i in range(len(xs)):
        for j in range(len(xs)):
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < nearby_distance:
                xvs[i]=xvs[i]+(xs[i]-xs[j])
                yvs[i]=yvs[i]+(ys[i]-ys[j])
    # Try to match speed with nearby boids
    for i in range(len(xs)):
        for j in range(len(xs)):
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < formation_distance:
                xvs[i]=xvs[i]+(xvs[j]-xvs[i])*speed_formation_strength/len(xs)
                yvs[i]=yvs[i]+(yvs[j]-yvs[i])*speed_formation_strength/len(xs)
    # Move according to velocities
    for i in range(len(xs)):
        xs[i]=xs[i]+xvs[i]
        ys[i]=ys[i]+yvs[i]

figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   boid_zip = list(zip(boids[0],boids[1]))
   scatter.set_offsets(boid_zip)


anim = animation.FuncAnimation(figure, animate, frames=200, interval=50)

#mywriter = animation.FFMpegWriter()

if __name__ == "__main__":
	plt.show()