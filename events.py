import pythoncom, pyHook, collections.OrderedDict

class Auditor:

	def __init__(self, windowName = None):
		applicationFilter = windowName


	def audit(self, data):
		if applicationFilter is not None:
			# Filter out event data that didn't take place in the window specified by windowName
			if data["WindowName"] == applicationFilter:
				transcribe(data)

		else:
			transcribe(data)

	# Write data passed by Listener to data file.
	def transcribe(data):
		dataFile = open("eventData.dat", 'a')

		firstWrite = True
		for key, value in data.items():	

			if not firstWrite:
				dataFile.write(">> {}|{}".format(key, value))

			else:
				dataFile.write(":: {}\n".format(value))
				firstWrite = False


class Listener:

	hookManager = pyHook.HookManager()

	def __init__(self):

		# Specifies the functions that handle events
		hookManager.MouseAll = _onMouseEvent
		hookManager.KeyDown = _onKeyBoardEvent

		# Hooks onto inputs
		hookManager.HookMouse()
		hookManager.hookKeyboard()

		pythoncom.PumpMessages() # Lets program sit forever, and wait for events.


	# Grabs Mouse Event Data
	def _onMouseEvent(event):
		mouseEventData = OrderedDict(("Time", event.Time),
									("MessageName", event.MessageName),
									("Message", event.Message),
									("Window", event.Window),
									("WindowName", event.WindowName),
									("Position", event.Position),
									("Wheel": event.Wheel),
									("Injected":event.Injected)
									)

		return(eventData)


	# Grabs Keyboard Event Data
	def _onKeyBoardEvent(event):
		keybdEventData = OrderedDict(("MessageName", event.MessageName),
									("Message", event.Message),
									("Time", event.Time),
									("Window", event.Window)
									('Ascii', chr(event.Ascii),
									('Key', event.Key)
									('KeyID', event.KeyID),
									('ScanCode'), event.ScanCode),
									('Extended'), event.Extended),
									('Injected'), event.Injected),
									('Alt', event.Alt),
									('Transition', event.Transition)
									)

		return(keybdEventData)

