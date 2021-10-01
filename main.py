from pynput import keyboard

def setup():
	left = keyboard.Key.left
	down = keyboard.Key.down
	right = keyboard.Key.right
	up = keyboard.Key.up

	def on_press(key):
		if key == left:
			print("Step on left")
		elif key == down:
			print("Step on down")
		if key == right:
			print("Step on right")
		if key == up:
			print("Step on up")

	def on_release(key):
		return

	# non-blocking fashion
	listener = keyboard.Listener(on_press=on_press, on_release=on_release)
	listener.start()

def loop():
	while True:
		pass

def main():
	setup()
	loop()

if __name__ == "__main__":
    main()