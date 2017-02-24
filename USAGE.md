# USING BOIDS
---------------

Boids is a programme that implements the formation of a flock of boids, which moves according to 3 functions.

1. [Input](#input)

	* [Config](#config)





<br>

## <a id="Input"></a>Input

Parameters are already set in config.yaml

```
boid_params:
    min_x_position: -450
    max_x_position: 50
    min_y_position: 300
    max_y_position: 600
    min_x_velocity: 0
    max_x_velocity: 10
    min_y_velocity: -20
    max_y_velocity: 20
flock_params:
    boid_count: 50
    fly_middle_strength: 0.01
    nearby_distance: 100
    formation_distance: 10000
    speed_formation_strength: 0.125
animation_params:
    axes_min: -500
    axes_max: 1500
    frames: 200
    interval: 50
```


## Class Flock

* 

