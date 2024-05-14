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