from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np


class Flock(object):
	def __init__(self, flock_params, boid_params):
		"""Initialise a flock with boid and flock information"""
		
		self.boid_count = flock_params['boid_count']
		self.fly_middle_strength = flock_params['fly_middle_strength']
		self.nearby_distance = flock_params['nearby_distance']
		self.formation_distance = flock_params['formation_distance']
		self.speed_formation_strength = flock_params['speed_formation_strength']


		lower_pos_limit = np.array([boid_params['min_x_position'],boid_params['min_y_position']])
		upper_pos_limit = np.array([boid_params['max_x_position'],boid_params['max_y_position']])
		lower_vel_limit = np.array([boid_params['min_x_velocity'],boid_params['min_y_velocity']])
		upper_vel_limit = np.array([boid_params['max_x_velocity'],boid_params['max_y_velocity']])

		self.positions = lower_pos_limit[:,np.newaxis] + \
		np.random.rand(2, self.boid_count)*(upper_pos_limit - lower_pos_limit)[:,np.newaxis]
		self.velocities = lower_vel_limit[:,np.newaxis] + \
		np.random.rand(2, self.boid_count)*(upper_vel_limit - lower_vel_limit)[:,np.newaxis]


	#I define helper functions so that Flock can call fly_middle or fly_away if need to

	def fly_middle(self):
		fly_middle_helper(self.positions,self.velocities,self.fly_middle_strength)

	
	@staticmethod
	def fly_middle_helper(positions, velocities, fly_middle_strength):

		# Fly towards the middle
		middle = np.mean(positions, 1)
		direction_to_middle = positions - middle[:,np.newaxis]
		velocities -= direction_to_middle * fly_middle_strength



	def fly_away(self):
		fly_away_helper(self.positions, self.velocities, self.nearby_distance)

	
	@staticmethod
	def fly_away_helper(positions, velocities, nearby_distance):
		positions=np.asarray(positions)
		velocities=np.asarray(velocities)

		# Fly away from nearby boids
		separations = positions[:,np.newaxis,:] - positions[:,:,np.newaxis]
		distances = separations * separations
		sum_distances = np.sum(distances, 0)

		far_away = sum_distances > nearby_distance
		separations_if_close = np.copy(separations)
		separations_if_close[0,:,:][far_away]= 0
		separations_if_close[1,:,:][far_away]= 0

		velocities += np.sum(separations_if_close,1)



	def match_speed(self):
		match_speed_helper(self.positions, self.velocities, 
						self.formation_distance, self.speed_formation_strength)

	
	@staticmethod
	def match_speed_helper(positions, velocities, formation_distance, speed_formation_strength):
		positions=np.asarray(positions)
		velocities=np.asarray(velocities)

		# Try to match speed with nearby boids
		separations = positions[:,np.newaxis,:] - positions[:,:,np.newaxis]
		distances = separations * separations
		sum_distances = np.sum(distances, 0)

		formations_far = sum_distances > formation_distance
		velocity_difference = velocities[:,np.newaxis,:] - velocities[:,:,np.newaxis]

		velocity_if_close = np.copy(velocity_difference)
		velocity_if_close[0,:,:][formations_far]= 0
		velocity_if_close[1,:,:][formations_far]= 0

		velocities -= np.mean(velocity_if_close, 1) * speed_formation_strength

		positions += velocities



	def update_boids(self):
		self.update_bodis_helper(self.positions, self.velocities, 
							self.fly_middle_strength, self.nearby_distance, 
							self.formation_distance, self.speed_formation_strength)
		

	def update_boids_helper(positions, velocities, 
					fly_middle_strength, nearby_distance, formation_distance, speed_formation_strength):
		Flock.fly_middle_helper(positions, velocities, fly_middle_strength)
		Flock.fly_away_helper(positions, velocities, nearby_distance)
		Flock.match_speed_helper(positions, velocities, formation_distance, speed_formation_strength)


		

    

















