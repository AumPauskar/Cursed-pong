def get_window_size():
	import json
	with open('config.json') as file:
		data = json.load(file)
		return (data['window-size-x'], data['window-size-y'])

def get_window_title():
	import json
	with open('config.json') as file:
		data = json.load(file)
		return data['window-title']