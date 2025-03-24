import argparse

def get_args():
	parser = argparse.ArgumentParser(
		description="A Simple Arg Parser",
		epilog="This is where you might put something"
	)

	# Required Args
	parser.add_argument(
		"-x", action="store", required=True, help="help text for arg x"
	)

	# Optional Args
	parser.add_argument("-y", help="Help Text for arg Y", default=False	)
	parser.add_argument("-z", help="Help tesst for arg z", type=int)

	print(parser.parse_args())


if __name__ == "__main__":
	get_args()