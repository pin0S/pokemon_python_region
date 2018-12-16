"""
File: session_1.py
Author: Peter Lynch
Email: pete.g.lynch@gmail.com
Github: Github: https://github.com/pin0s
Description: all code for the first lesson
"""

class Trainer:
	def set_name(self, name):
		self.name = name
	def display(self):
		print(self.name)

trainer_1 = Trainer()
trainer_1.set_name("Peter")
trainer_1.display()
