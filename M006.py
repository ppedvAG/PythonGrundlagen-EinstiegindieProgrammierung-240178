# Funktionen
# Code wiederverwenden

# x = 5
# y = 12
# print(f"{x} + {y} = {x + y}")
#
# x = 3
# y = 5
# print(f"{x} + {y} = {x + y}")
#
# x = 9
# y = 4
# print(f"{x} + {y} = {x + y}")

# Code in eine Funktion geben um diesen wiederverwenden zu können (kein Copy - Paste)
def addiere(x, y):
	print(f"{x} + {y} = {x + y}")  # Einrückungen beachten!

addiere(5, 12)
addiere(3, 5)
addiere(9, 4)

# Bei Parametern kann nicht erzwungen werden, welche Typen übergeben werden können
addiere(2.5, 4.8)
addiere("Hallo", "Welt")
addiere([1, 2, 3], [4, 5, 6])
# addiere([1, 2, 3], "Welt")

def addiere(x: int, y: int):
	print(f"{x} + {y} = {x + y}")

addiere(3, 4)
addiere("Hallo", "Welt")  # Typen können nicht erzwungen werden

def addiere(x: int | float, y: int | float):
	if type(x) in [int, float] and type(y) in [int, float]:
		print(f"{x} + {y} = {x + y}")

addiere("Hallo", "Welt")
addiere(4, 9.3)

def subtrahiere(x: int, y: int):
	return x - y

differenz = subtrahiere(7, 3)
print(differenz)

# Der Rückgabetyp kann auch definiert werden
def subtrahiere(x: int, y: int) -> float:
	return x - y

# Optionale Parameter
# Parameter mit einem Standardwert versehen, Standardwert kann überschrieben werden
def multipliziere(x: int = 0, y: int = 0):
	print(x * y)

multipliziere()
multipliziere(4)
multipliziere(4, 3)

def printPerson(vorname = None, nachname = None, alter = None, adresse = None, beruf = None, gehalt = None):
	print("...")

# Bestimmte Parameter direkt ansprechen, und andere Parameter überspringen
printPerson(vorname="Max", nachname="Mustermann")
printPerson(beruf="Python Entwickler", gehalt=1_500_000)

# Arbitrary Arguments
# Beliebig viele Parameter übergeben
def multipliziere(*numbers: int) -> int:
	ergebnis = 1
	for zahl in numbers:
		ergebnis *= zahl
	return ergebnis

multipliziere()
multipliziere(2, 3)
multipliziere(2, 3, 4)
multipliziere(2, 3, 4, 5, 6, 7, 8, 9)

zahlen = [1, 2, 3, 4, 5]

multipliziere(zahlen)  # Passt nicht, muss zerlegt werden

# a, b, c, d, e = zahlen
# multipliziere(a, b, c, d, e)

# *: Unpacking Operator, zerlegt beliebige Listen in ihre Einzelteile
print(multipliziere(*zahlen))


# Arbitrary Keyword Arguments
# Beliebig viele benannte Argumente übergeben
def printTeilnehmer(**tn):
	for vorname, nachname in tn.items():
		print(f"{vorname} {nachname}")

printTeilnehmer(TN1="Lukas", TN2="Udo", TN3="Michael")

teilnehmer = {
	"TN1": "Lukas",
	"TN2": "Udo",
	"TN3": "Michael"
}

printTeilnehmer(**teilnehmer)  # Unpacking Operator wie oben, nur mit einem Dictionary

# Übung 1:
# Wir wollen eine Funktion erstellen, die beliebig viele Zahlen als Parameter erhalten kann
# Und uns die größte dieser Zahlen zurückgibt
def maximum(*numbers):
	m = numbers[0]
	for z in numbers:
		if z > m:
			m = z
	return m
	# return max(numbers)

print(maximum(3, 2, 8, 1, 5, 8, 2, 5))
print(maximum(-3, -2, -8, -1, -5, -8, -2, -5))

# Übung 2:
# Wir wollen eine Funktion erstellen, die einen String als Parameter erhält
# Die Funktion soll dann in der Konsole ausgeben, aus wie vielen Klein- und Großbuchstaben der String besteht
# Die Funktion soll zusätzlich zählen wie viele Sonderzeichen (Nummern inkludiert) enthalten sind und das ebenfalls ausgeben
# Sonderzeichen: 4 | Groß: 3 | Klein: 12
def countCase(text: str):
	k, g, s = 0, 0, 0
	for z in text:
		if z.islower():
			k += 1
		elif z.isupper():
			g += 1
		else:
			s += 1
	print(f"Sonderzeichen: {s}, Groß: {g}, Klein: {k}")
countCase("Das ist ein Text!")

# Übung 3
# Schreibe eine Funktion, die eine Liste von Strings als Parameter empfängt
# Diese Funktion soll die Strings als eine Aufzählung zusammenbauen und am Ende zurück geben
# Dabei sollen alle Teilnehmer mit einem Komma und der letzte Teilnehmer mit einem "und" angehängt werden
# Beispiele:
# Parameter: []
# Keine Parameter angegeben
# Parameter: ["Teilnehmer"]
# Teilnehmer
# Parameter: ["Teilnehmer1", "Teilnehmer2"]
# Teilnehmer1 und Teilnehmer2
# Parameter: ["Teilnehmer1", "Teilnehmer2", "Teilnehmer3", "Teilnehmer4"]
# Teilnehmer1, Teilnehmer2, Teilnehmer3 und Teilnehmer4
def teilnehmerZusammenbauen(*tn: str):
	if tn is None or len(tn) == 0:
		print("Keine Parameter angegeben")
	elif len(tn) == 1:
		print(tn[0])
	else:
		kombination = ""
		for t in tn[0:-1]:
			kombination += t + ", "
		kombination = kombination.rstrip(", ")
		kombination += " und " + tn[-1]
		print(kombination)
		print("".join([t + ", " for t in tn[0:-1]]).rstrip(", ") + " und " + tn[-1])

teilnehmerZusammenbauen()
teilnehmerZusammenbauen("T1")
teilnehmerZusammenbauen("T1", "T2")
teilnehmerZusammenbauen("T1", "T2", "T3", "T4", "T5")