# In-/Output

# input(Text)
# Gibt dem User die Möglichkeit, eine Konsoleneingabe zu machen
# name = input("Gib deinen Namen ein: ")
# print(f"Dein Name ist {name}")
#
# zahl = input("Gib eine Zahl ein: ")
# zahl = float(zahl)
# print(f"Deine Zahl hoch 2 ist {zahl ** 2}")

# Escape Sequenzen
# Undruckbare Zeichen
# https://learn.microsoft.com/en-us/cpp/c-language/escape-sequences?view=msvc-170

# \n, \r: Zeilenumbruch
print("\n \r")
# \t: Tab
print("\t")
print('\'')  # Einzelnes Hochkomma
print("\"")  # Doppeltes Hochkomma
print("\\")  # Backslash (bei Pfaden)
print("\u2222")  # Unicode Zeichen

# open
# Interaktion mit Dateien
file = open("M008.txt", mode="w")
file.write("Hallo\n")  # Schreibe einen Text in den Buffer
file.write("Hallo\n")  # Schreibe einen Text in den Buffer
file.write("Hallo")  # Schreibe einen Text in den Buffer
file.flush()  # Schreibe den Inhalt des Buffers in das unterliegende File
file.close()  # Schließe das File

file = open("M008.txt", mode="r")
content = file.readlines()
print(content)
file.close()

# with-Statement
# Schließt den unterliegenden Stream am Ende des Blocks automatisch
with open("M008.txt", mode="w") as file2:
	file2.write("Hallo2\n")
	file2.write("Hallo2\n")
	file2.write("Hallo2")
# flush() und close() passieren hier automatisch

# rstring (rawstring)
# Nimmt den String genau so wie er geschrieben steht (ignoriert Escape-Sequenzen)
# pfad = "C:\Users\lk3\source\repos\Python_Grundkurs_2024_05_13\venv\Scripts\python.exe"  # Fehler
pfad = r"C:\Users\lk3\source\repos\Python_Grundkurs_2024_05_13\venv\Scripts\python.exe"
print(pfad)

# JSON
import json
liste = [1, 2, 3, 4, 5]

jsonListe = json.dumps(liste)  # Konvertiere zu einem String
with open("Json.json", "w") as j:  # In ein File schreiben
	json.dump(liste, j)

json.loads(jsonListe)  # Aus einem String laden
with open("Json.json", "r") as j:  # Aus einem File laden
	json.load(j)

# Übung 1:
# Funktion die dem User die Möglichkeiten (w, r, a) gibt
# User soll eine davon auswählen über input()
# Wenn der User keine valide Möglichkeit eingibt, soll die Eingabe wiederholt werden
# Danach soll einfach das File geöffnet werden
# Bonus: Frage den Benutzer nach dem File, welches geöffnet werden soll
def file():
	while True:
		eingabe = input("Gib einen Modus ein (w, r, a): ")
		if eingabe.lower() in ["w", "r", "a"]:
			pfad = input("Gib einen Dateipfad ein: ")
			with open(pfad, eingabe) as file:
				pass
			break

# Übung 2:
# Erstelle ein Programm, das zwei Integer oder Floats abfragt
# Gib dem Nutzer die Möglichkeit per Tastendruck zwischen Addition, Subtraktion, Multiplikation und Division zu wählen.
# -> Zahl zwischen 1 und 4 -> Rechenoperation auswählen
# Bei Ungültiger Eingabe soll der Benutzer erneut nach seiner Entscheidung gefragt werden.
# Lasse das Ergebnis inklusive der Berechnung in der Konsole ausgeben
# Frage nach Ende der Operation ob der Benutzer eine neue Berechnung durchführen will
def rechner():
	while True:
		while True:
			zahl1 = input("Gib eine Zahl ein: ")
			if zahl1.isnumeric():
				zahl1 = int(zahl1)
				break

		while True:
			zahl2 = input("Gib eine weitere Zahl ein: ")
			if zahl2.isnumeric():
				zahl2 = int(zahl2)
				break

		while True:
			rechenoperation = input("Gib eine Rechenoperation ein: \n1: Addition\n2: Subtraktion\n3: Multiplikation\n4: Division")
			if rechenoperation.isnumeric():
				rechenoperation = int(rechenoperation)
				if rechenoperation in [1, 2, 3, 4]:
					break

		if rechenoperation == 1:
			print(f"{zahl1} + {zahl2} = {zahl1 + zahl2}")
		if rechenoperation == 2:
			print(f"{zahl1} - {zahl2} = {zahl1 - zahl2}")
		if rechenoperation == 3:
			print(f"{zahl1} * {zahl2} = {zahl1 * zahl2}")
		if rechenoperation == 4:
			print(f"{zahl1} / {zahl2} = {zahl1 / zahl2}")

		neueBerechnung = input("Neue Berechnung durchführen (Y)?")
		if neueBerechnung.lower() != "y":
			break

rechner()