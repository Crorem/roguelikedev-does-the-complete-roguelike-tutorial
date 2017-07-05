import libtcodpy as ltc

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 24
LIMIT_FPS = 20

ltc.console_set_custom_font("terminal8x12_gs_ro.png",ltc.FONT_LAYOUT_ASCII_INROW)
ltc.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/ltc tutorial', False)
playerx = SCREEN_WIDTH/2
playery = SCREEN_HEIGHT/2

def handle_keys():
	global playerx, playery

	#movement keys
	if ltc.console_is_key_pressed(ltc.KEY_ESCAPE):
		return True
	elif ltc.console_is_key_pressed(ltc.KEY_KP7):
		playerx -= 1
		playery -= 1
	elif ltc.console_is_key_pressed(ltc.KEY_KP8):
		playery -= 1
	elif ltc.console_is_key_pressed(ltc.KEY_KP9):
		playerx += 1
		playery -= 1
	elif ltc.console_is_key_pressed(ltc.KEY_KP4):
		playerx -= 1
	elif ltc.console_is_key_pressed(ltc.KEY_KP6):
		playerx += 1
	elif ltc.console_is_key_pressed(ltc.KEY_KP1):
		playerx -= 1
		playery += 1
	elif ltc.console_is_key_pressed(ltc.KEY_KP2):
		playery += 1
	elif ltc.console_is_key_pressed(ltc.KEY_KP3):
		playerx += 1
		playery += 1
	
	return False

while not ltc.console_is_window_closed():
	ltc.console_set_default_foreground(0, ltc.lighter_grey)
	ltc.console_put_char(0, playerx, playery, '@', ltc.BKGND_NONE)
	ltc.console_flush()
	key = ltc.console_wait_for_keypress(True)
	ltc.console_put_char(0, playerx, playery, ' ', ltc.BKGND_NONE)
	if handle_keys():
		break