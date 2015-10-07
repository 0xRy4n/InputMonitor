import pythoncom, pyHook

class EventListener:

	hookManager = pyHook.HookManager()

	def __init__(self):
		hookManager.MouseAll = onMouseEvent
		hookManager.KeyDown = onKeyBoardEvent
		hookManager.HookMouse()
		hookManager.hookKeyboard()
		pythoncom.PumpMessages() # Lets program sit forever, and wait for events.


	# Grabs Mouse Event Data
	def onMouseEvent(event):
		mouseEventData = {
						"MessageName":event.MessageName,
						"Message":event.Message,
						"Time":event.Time,
						"Window":event.Window,
						"WindowName":event.WindowName,
						"Position":event.Position,
						"Wheel":event.Wheel,
						"Injected":event.Injected
						}

		return(eventData)

	# Grabs Keyboard Event Data
	def onKeyBoardEvent(event):
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
						'Injected':event.Injected,
						'Alt':event.Alt,
						'Transition':event.Transition
						}

		return(keybdEventData)
