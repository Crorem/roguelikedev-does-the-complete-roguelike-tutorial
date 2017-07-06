import libtcodpy as ltc

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 24

MAP_WIDTH = 80
MAP_HEIGHT = 21

ltc.console_set_custom_font("terminal8x12_gs_ro.png",ltc.FONT_LAYOUT_ASCII_INROW)
ltc.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/ltc tutorial', False)
con = ltc.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)
playerx = SCREEN_WIDTH/2
playery = SCREEN_HEIGHT/2

color_dark_wall = ltc.Color(0, 0, 100)
color_dark_ground = ltc.Color(50, 50, 150)

def handle_keys():
	global playerx, playery

	#movement keys
	if ltc.console_is_key_pressed(ltc.KEY_ESCAPE):
		return True
	elif ltc.console_is_key_pressed(ltc.KEY_KP7):
		player.move(True, -1, -1)
	elif ltc.console_is_key_pressed(ltc.KEY_KP8):
		player.move(True,  0, -1)
	elif ltc.console_is_key_pressed(ltc.KEY_KP9):
		player.move(True,  1, -1)
	elif ltc.console_is_key_pressed(ltc.KEY_KP4):
		player.move(True, -1,  0)
	elif ltc.console_is_key_pressed(ltc.KEY_KP6):
		player.move(True,  1,  0)
	elif ltc.console_is_key_pressed(ltc.KEY_KP1):
		player.move(True, -1,  1)
	elif ltc.console_is_key_pressed(ltc.KEY_KP2):
		player.move(True,  0,  1)
	elif ltc.console_is_key_pressed(ltc.KEY_KP3):
		player.move(True,  1,  1)
	return False

def make_map():
	global map
	
	map = [[ Tile(False)
		for y in range(MAP_HEIGHT) ]
			for x in range(MAP_WIDTH) ]
	
	map[30][10].blocked = True
	map[30][10].block_sight = True
	map[50][10].blocked = True
	map[50][10].block_sight = True

def render_all():
	for y in range(MAP_HEIGHT):
		for x in range(MAP_WIDTH):
			wall = map[x][y].block_sight
			if wall:
				ltc.console_put_char_ex(con, x, y, '#', ltc.grey, ltc.black)
			else:
				ltc.console_put_char_ex(con, x, y, '.', ltc.grey, ltc.black)
	for object in objects:
		object.draw()
	ltc.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
	ltc.console_flush()

class Object:
	def __init__(self, x, y, char, color):
		self.x = x
		self.y = y
		self.char = char
		self.color = color

	def move(self, relative, x, y):
		if relative:
			tempx = x + self.x
			tempy = y + self.y
		else:
			tempx = x
			tempy = y
		if tempx >= 0 and tempy >= 0 and tempx < MAP_WIDTH and tempy < MAP_HEIGHT and (not map[tempx][tempy].blocked):
			self.x = tempx
			self.y = tempy

	def draw(self):
		ltc.console_set_default_foreground(con, self.color)
		ltc.console_put_char(con, self.x, self.y, self.char, ltc.BKGND_NONE)

	def clear(self):
		ltc.console_put_char(con, self.x, self.y, ' ', ltc.BKGND_NONE)

class Tile:
	def __init__(self, blocked, block_sight = None):
		self.blocked = blocked
		
		if block_sight is None: block_sight = blocked
		self.block_sight = block_sight
		
player = Object(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, '@', ltc.lighter_grey)
npc = Object(SCREEN_WIDTH/2 - 5, SCREEN_HEIGHT/2, '@', ltc.yellow)
objects = [npc, player]
make_map()

while not ltc.console_is_window_closed():
	for object in objects:
		object.draw()
	render_all()
	for object in objects:
		object.clear()
	key = ltc.console_wait_for_keypress(True)
	if handle_keys():
		break