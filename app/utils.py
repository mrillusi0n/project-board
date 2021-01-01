from random import randint

def get_random_color():
	sat = 81
	light = 71
	hue = randint(0, 360)

	return f'hsl({hue}, {sat}%, {light}%)'