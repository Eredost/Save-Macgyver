#-*-coding:UTF-8 -*-
"""This module load items, place randomly on
the window and check the player position"""

import random

import pygame
from pygame.locals import *

from Constantes import *
from Level import *


class Item:

	def __init__(self, item1, item2, item3, level, character):
		
		self.items = [item1, item2, item3]
		self.level = level
		self.character = character
		self.items_pos = []
		self.inventory = []

		for item in self.items:
			
			self.items_pos.append(random.randint(0, len(self.level.blank_cases)))

	def placement(self, window):

		value = 0
		
		for item in self.items:

			blank_case_x = self.level.blank_cases[self.items_pos[value]][0]
			blank_case_y = self.level.blank_cases[self.items_pos[value]][1]

			if item not in self.inventory:
			
				window.blit(item, (blank_case_x, blank_case_y))

				if self.character.pos_x == blank_case_x and \
				   self.character.pos_y == blank_case_y:

					self.inventory.append(item)
			
			value += 1

