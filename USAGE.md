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
	
3. [Output](#Output)

4. [Tests](#Tests)


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

### <a id="Class Flock"></a>Class Flock

In this class, many helper and @staticmethod functions, which don't take any argument from class, are used to be perform maths operations. Thanks to the helper functions, the maths operations can be tested with fixed numbers.

#### <a id="Fly Middle"></a>Fly Middle

fly_middle method calculate the centroid point of the flock and move boids toward it.
```
middle = np.mean(positions, 1)
direction_to_middle = positions - middle[:,np.newaxis]
velocities -= direction_to_middle * fly_middle_strength
```

#### <a id="Fly Away"></a>Fly Away

fly_away method calculates distance between boids, check which ones that are too close to each other, and update their velocities beased on average differences in distances of the close ones.

#### <a id="Match Speed"></a>Match Speed

match_speed method calculates distance between boids, check which ones that are close to each other, and update their velocities beased on average differences in velocities of the close ones.

#### <a id="Update Boids"></a>Update Boids

update_boids just runs all Fly Middle, Fly Away, and Match Speed consecutively.

### <a id="Simulate"></a>Simulate

simulate function uses matplotlib.animation library to create animation.
```
anim = animation.FuncAnimation(figure, animate, frames=animation_params['frames'],
                                        interval=animation_params['interval'])
```

## <a id="Output"></a>3. Output

When you create a Flock instance, the initial positions and velocities of the boids are randomized using np.rand. Each individual method can be called separately to modify the positions and velocities.

## <a id="Tests"></a>4. Tests

Fixture files are used to record the initial positions and velocities, and the results after each individual method modifies them.

In tests, the "before" records are called and pass through the helper methods again, and are compared to "after" records. The test are explicitly written for the helper functions.

2 arbitrary numbers from the 2 set of array are picked out for the actual assert_equal, for example:
```
assert_equal(np.asarray(boid_data['after'])[2,5],after[2,5])
assert_equal(np.asarray(boid_data['after'])[3,20],after[3,20])
```