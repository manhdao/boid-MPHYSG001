# USING BOIDS
---------------

Boids is a programme that implements the formation of a flock of boids, which moves according to 3 behaviors: They try to fly to the middle of the flock, they avoid collision, and they match their speed with close boids.

1. [Input](#Input)

	* [Config](#Config)
	* [Simulate Action](#Simulate Action)


2. [Objects](#Objects)

	* [Class Flock](#Class Flock)

		* [Fly Middle](#Fly Middle)

		* [Fly Away](#Fly Away)

		* [Match Speed](#Match Speed)

		* [Update Boids](#Update Boids)

	* [Simulate](#Simulate)
	
2. [Output](#Output)

3. [Tests](#Tests)



<br>

## <a id="Input"></a>1. Input

### <a id="Config"></a>Config

Parameters to create a flock of boids are already set in config.yaml

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

Number of boids can be changed directly in the command, with "-n" option:
```
python boid_command.py -n 15
```
Besides the number of boids, other parameters can only be changed by editing config.yaml, or calling config in a dict and modify it.


### <a id="Simulate Action"></a>Simulate Action

Action of the flock can be changed directly in the command, with "-a" option:
```
python boid_command.py -a fly_middle
```
There are 3 options matching 3 functions: fly_middle, fly_away, match_speed


## <a id="Objects"></a>2. Objects

### <a id="Class Flock"></a>2. Class Flock

When you create a Flock instance, the initial positions and velocities of the boids are already random. In this class, many helper and @staticmethod functions are used to be able to test with fixed numbers. The test are exclusively written for those functions

#### <a id="Fly Middle"></a>2. Fly Middle

Fly Middle method calculate the centroid point of the flock and move boids toward it.
```
middle = np.mean(positions, 1)
direction_to_middle = positions - middle[:,np.newaxis]
velocities -= direction_to_middle * fly_middle_strength
```

#### <a id="Fly Away"></a>2. Fly Away

Fly Away method calculates distance between boids, check which ones that are too close to each other, and update their velocities beased on average differences in distances of the close ones.

#### <a id="Match Speed"></a>2. Match Speed

Match Speed method calculates distance between boids, check which ones that are close to each other, and update their velocities beased on average differences in velocities of the close ones.

#### <a id="Update Boids"></a>2. Update Boids

Update Boids just runs all Fly Middle, Fly Away, and Match Speed consecutively.