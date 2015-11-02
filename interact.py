import ctypes, time, random

def alert(delay, title, text):
	time.sleep(delay)
	ctypes.windll.user32.MessageBoxA(0, text, title, 0)

def choose():
	options = ["You have been chosen to have your results recorded.",
				"You have been chosen to have your results discarded."]

	choice = random.randint(0,2)
	if choice < 2:
		alert(1, "Group Placement", options[choice])