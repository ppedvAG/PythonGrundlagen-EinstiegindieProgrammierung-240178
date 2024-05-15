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

# Übung 2
# Definiere eine beliebige Liste
# Erstelle ein Programm, das den User fragt, das wievielte Element in der Konsole ausgegeben werden soll
# Falls die Zahl außerhalb des Listen-Indexes liegt soll ein Fehler geworfen und der User darauf hingewiesen werden

# Übung 3
# Füge der beschleunigen Funktion deiner Fahrzeug-Klasse aus Modul 9 eine eigene Exception hinzu:
#    - Sie soll geworfen werden, falls die Höchstgeschwindigkeit überschritten wird

# Übung 4
# Erweitere den Rechner aus Übung 7:
# Erstelle eine Klasse namens Rechner und füge dieser zwei Methoden hinzu: Berechne und InputLesen
# Die Berechne Methode soll drei Parameter empfangen (Zahl 1, Zahl 2, Rechenart) und die Berechnung ausführen
# Die InputLesen Methode soll in einer Endlosschleife vom Benutzer Werte einlesen, bis dieser eine Zahl eingegeben hat
# Prüfe bei dieser Methode mittels try-except, ob die Eingabe des Benutzers valide ist (Exception bei der int(...) Methode abfangen)
# Verwende danach drei mal die InputLesen Methode um die Werte zu erhalten und im Anschluss die Berechne Methode um die Berechnung mit den Werten durchzuführen