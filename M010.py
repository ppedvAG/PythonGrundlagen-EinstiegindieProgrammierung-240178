# Vererbung

# Oberklassen werden als Elternteil von beliebig vielen Unterklassen definiert
# Unterklassen erben alle möglichen Member (Variablen, Funktionen)

from M009 import Fahrzeug

# In der Klammer kann die Oberklasse angegeben werden
# PKW ist eine Spezifizierung von Fahrzeug
# Hier sollen weitere Felder/Methoden hinzugefügt werden, die einen PKW auszeichnen
class PKW(Fahrzeug):
	def __init__(self, name: str, preis: int, maxV: int, anzSitze: int):
		# Wenn __init__ der Oberklasse nicht aufgerufen wird, werden die Felder aus Fahrzeug nicht gesetzt (Name, Preis, ...)
		# Mit super() kann auf die Implementation in der Oberklasse zugegriffen werden
		super().__init__(name, preis, maxV)
		self.anzSitze = anzSitze

	# Beschreibung überschreiben um Sitzplätze auszugeben
	def beschreibung(self) -> str:
		fahrzeugText = super().beschreibung()
		return fahrzeugText + f" Er hat {self.anzSitze} Sitzplätze."

class Schiff(Fahrzeug):
	def beschreibung(self) -> str:
		return super().beschreibung()

pkw = PKW("VW", 20_000, 250, 5)
pkw.starteMotor()
pkw.beschleunige(50)
print(pkw.beschreibung())
pkw.beschleunige(-50)
pkw.stoppeMotor()

schiff = Schiff("Titanic", 20_000_000, 50)
print(schiff.beschreibung())
print(schiff.name)