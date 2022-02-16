import json
with open('config.json') as file:
	data = json.load(file)

def get_window_size():
	return (data['window-size-x'], data['window-size-y'])

def get_window_title():
	return data['window-title']

def get_player_delta():
	return data['standard-delta-player']

def get_ball_delta():
	return data['standard-delta-ball']

def get_boundary_player():
	return data['boundary-player']

def get_load_sleep():
	return data['load-sleep']