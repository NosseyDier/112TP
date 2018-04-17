import copy
import numpy as np

class Piece(object):
	def __init__(self, profile, blocks, position, color):
		self.profile = profile
		self.blocks = blocks
		self.x = position[0]
		self.y = position[1]
		self.color = color

	def __eq__(self, other):
		return (type(self) == type(other) and self.profile == other.profile and self.x == other.x and \
			self.y == other.y and self.blocks == other.blocks and self.color == other.color)

	def __repr__(self):
		return str(self.profile)

	def flipUpDown(self):
		newProf = copy.deepcopy(self.profile)
		for i in range(len(self.profile)):
			newProf[len(newProf) - i - 1] = self.profile[i]
		self.profile = newProf

	def flipLR(self):
		npProfile = np.array(self.profile)
		npProfile = np.fliplr(npProfile)
		npProfile.tolist()
		self.profile = npProfile

	def rotateLeft(self):
		npProfile = np.array(self.profile)
		npProfile = np.rot90(npProfile, 1, (1,0))
		npProfile.tolist()
		self.profile = npProfile

	def rotateRight(self):
		npProfile = np.array(self.profile)
		npProfile = np.rot90(npProfile, 1, (0,1))
		npProfile.tolist()
		self.profile = npProfile

