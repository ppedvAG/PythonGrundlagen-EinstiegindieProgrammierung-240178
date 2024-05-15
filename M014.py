# UnitTests
import unittest

class Rechner:
	def addiere(self, x, y):
		return x + y

	def subtrahiere(self, x, y):
		return x - y

# Tests regelmäßig ausführen um frühzeitig Fehler erkennen und auszubessern
class RechnerTests(unittest.TestCase):
	def testeRechner(self):
		# Arrange, Act, Assert

		# Arrange: Test aufbauen (Objekte erstellen, Urzustand herstellen)
		r = Rechner()

		# Act: Zu testenden Code ausführen
		summe = r.addiere(3, 4)

		# Assert: Test auswerten (prüfen ob das Ergebnis korrekt ist)
		self.assertEqual(7, summe)

	def testeSubtrahiere(self):
		r = Rechner()
		diff = r.subtrahiere(5, 2)
		self.assertEqual(3, diff)

if __name__ == "__main__":
	unittest.main()