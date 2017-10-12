Problem:- 
	Write a custom random number generation algo which should be 73% biased to the higher number.
	
Solution:-
	Aglorithm- 1
		Random Number Generation:-
			I've created A random number generation Algorithm by using LCG(Linear Congruential Generator)
			
			function random(range)
				step 1 -: Get a seed value ( I've used time() value as seed)
				step 2 -: decide value of a and c 
				step 3 -: set value of m   = range + 1   # To include the last number as well
				step 4 -: generate number using formula int(a * seed_value + c) % m 
				step 5 -: return number
				step 6 -:  end
			
	Algorithm- 2
		Biased Random Number Generation :-
		
			A Biased random number generation function with 73% biased toward higher number
		function biased_random()
			step 1 -:  Get value for start and stop
			step 2 -:  num = random(99) get a random number 
			step 3 -:  width = stop - start   get value of width
			step 4 -:  rnd = random(width)  get another random value using width as range
			step 5 -:  check num is greater or equal to 27 
			step 6 -:	if true:
			step 7 -:      return start + width/2 + rnd/2  to return biased random number 
			step 8 -:   else:
			step 9 -:     return start  + rnd/2  to return biased random number 
			step 10 -:  end
	