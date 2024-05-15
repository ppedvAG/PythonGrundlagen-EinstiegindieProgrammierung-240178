# Klassen und Objekte
# Bauplan für komplexe Objekte

# int: Ganze Zahl
# float: Kommazahl
# string: Zeichenkette
# Person: ?

# Klasse: Bauplan, enthält Funktionen und Variablen (ohne konkrete Werte)
# Objekt: Instanz von der Klasse, Funktionen können über Objekte verwendet werden und Objekte haben konkrete Werte

# -----------------------------------------------------------------------------

# Person
# Vorname, Nachname, Alter
class Person:
	"""
	docstring: Dokumentation für den Code definieren
	Mit \""" am Anfang und \""" am Ende kann eine Klasse/Funktion beschrieben werden

	Die Person Klasse
	"""

	def __init__(self, vorname: str, nachname: str, alter: int = 0):
		"""
		__init__

		Wird in anderen Sprachen als Konstruktor bezeichnet

		Beschreibt welche Attribute Objekte von dieser Klasse haben

		Übernimmt vom Benutzer Eingaben (Standardwerte) für das entsprechende Objekt

		:param vorname: Der Vorname der Person
		:param nachname: Der Nachname der Person
		:param alter: Das Alter der Person
		"""
		self.vorname = vorname
		self.nachname = nachname
		self.alter = alter

	# Klassenmethode
	# Objekte bekommen diese Methode und können diese benutzen
	# self immer als erster Parameter
	def sprechen(self, text: str):
		print(f"{self.vorname} {self.nachname} sagt: {text}")

	def laufen(self, distanz):
		pass  # pass: Platzhalter für späteren Code (macht nichts)

	# __str__
	# Wird in anderen Sprachen als ToString bezeichnet
	# Kann hier überschrieben werden
	# Alle mit __ können überschrieben
	def __str__(self):
		return f"{self.vorname} {self.nachname} {self.alter}"

# -----------------------------------------------------------------------------

# Objekt
# Hier kann jetzt von der Person Klasse ein konkretes Objekt erstellt werden

person = Person("Max", "Mustermann", 30)  # Objekt erstellen mit <Klassenname>()
# person.vorname = "Max"
# person.nachname = "Mustermann"
# person.alter = 30
person.sprechen("Hallo")

person2 = Person(vorname="Max", nachname="Mustermann")

# Neue Attribute hinzufügen
# Sollte vermieden werden
person.adresse = "Zuhause"
print(person.adresse)
del person.adresse

# Vor __str__ Überschreibung
print(person)  # <__main__.Person object at 0x0000022E26DBD610>

# Nach __str__ Überschreibung
print(person)  # Max Mustermann 30

# Übung 1:
# 1. Erstelle eine Fahrzeug-Klasse
# 2. Diese Klasse soll typische Eigenschaften eines Fahrzeuges enthalten: (in __init__)
#     - Fahrzeug-Name
#     - Preis
#     - Maximale Geschwindigkeit
#     - Derzeitige Geschwindigkeit
#     - Motorzustand (An/Aus)
# 3. Die Klasse soll auch folgende Methoden enthalten:
#     - Beschleunigen (Erhöhe bzw Verringere die Derzeitige Geschwindigkeit aber übersteige nicht das Maximum) -> Parameter int (Wieviel soll beschleunigt werden)
#     - StarteMotor (Setze Motorzustand auf True, funktioniert nur wenn das Auto noch nicht gestartet ist)
#     - StoppeMotor (Motor kann nur gestoppt werden, wenn das Auto nicht fährt)
#     - Beschreibung (Gibt alle Informationen über die Klasse wieder)
# 4. Erstelle eine Instanz der Klasse und nutze die Beschreibungs Funktion (Konkrete Werte)
class Fahrzeug:
	def __init__(self, name:str, preis:int, maxV: int):
		self.name = name
		self.preis = preis
		self.maxV = maxV
		self.aktV = 0
		self.motorStatus = False

	def starteMotor(self):
		if not self.motorStatus:
			self.motorStatus = True
		else:
			print("Fehler")

	def stoppeMotor(self):
		if self.motorStatus:
			self.motorStatus = False
		else:
			print("Fehler")

	def beschleunige(self, a):
		if not self.motorStatus:
			print("Fehler")
			return

		if self.aktV + a > self.maxV:
			print("Fehler")
			return

		if self.aktV + a < 0:
			print("Fehler")
			return

		self.aktV += a

	def beschreibung(self) -> str:
		return f"{type(self).__name__} {self.name} kostet {self.preis}€ und kann maximal {self.maxV}km/h fahren." + \
				f" Es fährt gerade {self.aktV}km/h." if self.motorStatus else ""

fzg = Fahrzeug("VW", 20_000, 250)
fzg.starteMotor()
fzg.beschleunige(50)
fzg.beschleunige(500)
print(fzg.beschreibung())
fzg.beschleunige(-50)
fzg.stoppeMotor()