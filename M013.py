# Decorator
# "Wrapper" für eine Funktion mit dem Code vor oder nach Aufruf der entsprechenden Funktion ausgeführt werden kann
# Wird mit @<Name> angehängt an eine Funktion
import time


def hallo():
	print("Hallo")

# Wenn ich dieser Funktion Code hinzufügen möchte, kann ich sie verändern
# Aber vielleicht möchte ich nur "Erweiterungen" machen

# func: Funktion, welche den Decorator mit @ angehängt bekommt
def testDecorator(func):
	def wrapper():  # wrapper Funktion innerhalb von testDecorator definieren
		print("Hallo")
		func()  # hallo() aufrufen
		print("Tschüss")
	return wrapper  # Hier interne Funktion zurückgeben

hallo()  # Output: Hallo

@testDecorator
def hallo():
	print("Hallo")

hallo()  # Output: Hallo\nHallo\nTschüss

# Sinnvolles Beispiel
# Zeitmesser
def stopwatch(func):
	def wrapper():
		startTime = time.time()
		func()
		endTime = time.time()
		print(f"Gesamtzeit: {int((endTime - startTime) * 100) / 100}s")
	return wrapper

@stopwatch
def generiereZahlen():
	list(range(50_000_000))

# generiereZahlen()

# Decorator mit Parameter

def stopwatch(func):
	def wrapper(*args, **kwargs):
		startTime = time.time()
		func(*args, **kwargs)
		endTime = time.time()
		print(f"Gesamtzeit: {int((endTime - startTime) * 100) / 100}s")
	return wrapper

@stopwatch
def genZahlen(maximum):
	list(range(maximum))

genZahlen(50_000_000)

# ----------------------------------------------------

# property
class Quadrat:
	def __init__(self, a):
		# Wenn a gesetzt wird, sollte sich auch die Fläche ändern
		self.a = a
		self._area = 0  # "private"

	@property
	def area(self):
		self._area = self.a * self.a
		return self._area

	# @area.setter
	# def area(self, area):
	# 	self._area = area

q = Quadrat(5)
print(q.area)
q.a = 10
# q.area = 10
print(q.area)
print(q._area)  # Kann trotzdem angegriffen werden