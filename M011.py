# Fehlerbehandlung

# from M009 import Fahrzeug
# fzg = Fahrzeug()

# try: Führe den Code aus. Wenn ein Fehler auftritt, führe den Code im entsprechenden except-Block aus und lass das Skript weiterlaufen
try:
	eingabe = input("Gib eine Zahl ein: ")
	x = int(eingabe)

	# Wenn die Eingabe des Users 0 ist, wollen wir einen Fehler werfen
	if x == 0:
		raise ZeroDivisionError("Die Eingabe darf nicht 0 sein")
	print(10 / x)
except ValueError:  # Fange einen bestimmten Fehler (hier ValueError)
	print("Umwandlung gescheitert")
except TypeError:
	print("Die Eingabe darf nicht None sein")
except Exception as e:  # Fange alle anderen Fehler
	# Exceptions können mit as <Name> einen Namen bekommen und dadurch können wir Informationen aus dem Fehler auslesen
	print("Anderer Fehler")
	print(type(e).__name__)
	print(e)  # Die Python interne Fehlermeldung

	# Traceback ausprinten
	import traceback

	for z in traceback.format_exception(e):
		print(z)
else:
	# Wird ausgeführt, wenn kein Fehler aufgetreten ist
	print("Konvertierung erfolgreich")
finally:
	# Wird immer ausgeführt
	print("Konvertierung fertig")

print("Hallo")

# raise
# Eigenen Fehler verursachen, das Skript abstürzen lassen
# Besser als print(...), weil print in der GUI/Web nicht funktioniert
from M009 import Fahrzeug


class Flugzeug(Fahrzeug):
	def __init__(self, name, preis, maxV):
		super().__init__(name, preis, maxV)

	def starteMotor(self):
		if not self.motorStatus:
			self.motorStatus = True
		else:
			raise SystemError("Motor ist bereits gestartet")


flugzeug = Flugzeug("Boeing 737", 123_456_789, 1000)
flugzeug.starteMotor()
try:
	flugzeug.starteMotor()
except SystemError as e:
	# Statt print könnte hier auch in ein TextFeld, in eine DB, eine Mobilbenachrichtigung, ... gemacht werden
	print(e)

# Übung 1
# Erstelle ein Programm, das den User nach zwei Integern fragt
# Falls der User zwei Integer eingibt sollen diese addiert und das Ergebnis in der Konsole ausgegeben werden und das Programm kann beendet werden
# Falls der Benutzer einen falschen Typen eingibt soll das Programm ihn darauf hinweisen, das nur Integer akzeptiert werden und ihn erneut nach den Zahlen fragen
while True:
	try:
		z1 = int(input("Gib eine Zahl ein: "))
		z2 = int(input("Gib eine Zahl ein: "))
		print(z1 + z2)
		break
	except ValueError:
		print("Keine Zahl eingegeben")

# Übung 2
# Definiere eine beliebige Liste
# Erstelle ein Programm, das den User fragt, das wievielte Element in der Konsole ausgegeben werden soll
# Falls die Zahl außerhalb des Listen-Indexes liegt soll ein Fehler geworfen und der User darauf hingewiesen werden
test = [1, 2, 3, 4]
try:
	stelle = int(input("Gib eine Stelle ein: "))
	print(test[stelle])
except ValueError:
	print("Keine Zahl eingegeben")
except IndexError:
	print("Die Zahl liegt nicht innerhalb der Grenzen der Liste")


# Übung 3
# Füge der beschleunigen Funktion deiner Fahrzeug-Klasse aus Modul 9 eine eigene Exception hinzu:
#    - Sie soll geworfen werden, falls die Höchstgeschwindigkeit überschritten wird
class VelocityException(Exception):
	pass


# raise VelocityException("Die neue Geschwindigkeit ist zu hoch")

# Übung 4
# Erweitere den Rechner aus Übung 7:
# Erstelle eine Klasse namens Rechner und füge dieser zwei Methoden hinzu: Berechne und InputLesen
# Die Berechne Methode soll drei Parameter empfangen (Zahl 1, Zahl 2, Rechenart) und die Berechnung ausführen
# Die InputLesen Methode soll in einer Endlosschleife vom Benutzer Werte einlesen, bis dieser eine Zahl eingegeben hat
# Prüfe bei dieser Methode mittels try-except, ob die Eingabe des Benutzers valide ist (Exception bei der int(...) Methode abfangen)
# Verwende danach drei mal die InputLesen Methode um die Werte zu erhalten und im Anschluss die Berechne Methode um die Berechnung mit den Werten durchzuführen
class Rechner:
	def berechne(self, zahl1, zahl2, rechenoperation):
		if rechenoperation == 1:
			print(f"{zahl1} + {zahl2} = {zahl1 + zahl2}")
		elif rechenoperation == 2:
			print(f"{zahl1} - {zahl2} = {zahl1 - zahl2}")
		elif rechenoperation == 3:
			print(f"{zahl1} * {zahl2} = {zahl1 * zahl2}")
		elif rechenoperation == 4:
			print(f"{zahl1} / {zahl2} = {zahl1 / zahl2}")
		else:
			print("Keine gültige Rechenoperation eingegeben")

	def inputLesen(self, text):
		while True:
			try:
				eingabe = input(text)
				zahl = int(eingabe)
				return zahl
			except ValueError:
				print("Keine Zahl eingegeben")


r = Rechner()
z1 = r.inputLesen("Gib eine Zahl ein: ")
z2 = r.inputLesen("Gib eine weitere Zahl ein: ")
art = 0
while art not in [1, 2, 3, 4]:
	art = r.inputLesen("Gib eine Rechenoperation ein: \n1: Addition\n2: Subtraktion\n3: Multiplikation\n4: Division")
r.berechne(z1, z2, art)
