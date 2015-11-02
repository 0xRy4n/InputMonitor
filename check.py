import events, interact, time

interact.choose()
time.sleep(1)
auditor = events.Auditor()
listener = events.Listener(auditor)
