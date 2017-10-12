import time as t 
import sys
import math

class BiasedRandom:

	''' 
		A Random Number generator Class which provide the biased random number
	'''
	def __init__(self, start, stop): 
		''' Instantiation of Class variables '''
		# Initialize variables
		self.start = start   # start range 
		self.stop = stop	 # stop range
	
	def _random(seft , range):
		"""
		A uniform random number generation function using LCG( Linear Congruential Generator)
		using formula  = X_{n+1}=(X_{n}+c) mod m
		"""
		# Initialize variables
		x_value = t.time()    		# Our seed, 
		a = 101427               	# Our "a" base value
		c = 321                  	# Our "c" base value
		m = range + 1             	# Our "m" base value
		return int(a * x_value + c) % m 

	def biased_random(self):
		"""
		A Biased random number generation function with 73% biased toward higher number
		"""
		t.sleep(0.00000000001)
		num = self._random(99)    # getting uniform random number to generate biased one    
		width = (self.stop - self.start)
		rnd = self._random(width)
		
		""" 
		Formula to get biased random number
		"""
		if num >= 27:     #if num is greater than or equal 27 then generated number will be start + half of width + half of random number
			return self.start + math.floor(width/2) + math.ceil(rnd/2)
		else:			  #if num is not greater than 27 then generated number will be start  + half of random number
			return self.start +  math.floor(rnd/2)
	

if len(sys.argv) < 2:    # check if argument is missing
	raise TypeError("Missing arguments") 
if len(sys.argv) is 2:    # if only one argument is supplied
	if not (sys.argv[1]).isdigit():  
		raise ValueError("non-integer argument 1")
	for i in range(100):
	object = BiasedRandom(0,int(sys.argv[1]))   #object instantiation
	print(object.biased_random())				# calling biased number generator function
if len(sys.argv) >= 3:  # if only 2 or more argument is supplied
	if not (sys.argv[1]).isdigit():
		raise ValueError("non-integer argument 1")
	if not (sys.argv[2]).isdigit():
		raise ValueError("non-integer argument 2")
	start = int(sys.argv[1])
	stop = int(sys.argv[2])
	width = stop - start
	if width < 1:
		raise ValueError("First Interger must be smaller to second one")
	object = BiasedRandom(start,stop) #object instantiation
	print(object.biased_random()) # calling biased number generator function
