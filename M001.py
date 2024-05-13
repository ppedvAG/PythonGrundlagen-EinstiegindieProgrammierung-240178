# Ich bin ein Kommentar
# Mehrzeilige Kommentare existieren nicht
print("Hello World")

# Variablen
# name = Wert
x = 5  # Variablen nehmen ihren Typen anhand des Inhalts an
x = "Hallo"
print(x)

# Datentypen
# int, float, bool, str, complex

# int
y = 5
y = 321957943206790321460982759023794376924760923485831590  # beliebig große Zahlen in int möglich
print(type(y))

# float
z = 32198401324.2198472198479127438921  # beliebig große Zahlen in float möglich (Vor-/Nachkommastellen)
print(type(z))

# bool
b = False
b = True
print(type(b))

# str
s = "Hallo"
s = 'Hallo'  # Doppelte oder einzelne Hochkomma möglich
print(s)
print(type(s))

# complex (komplexe Zahlen)
c = 5 + 12j  # j für den imaginären Teil
print(c)

# Stringfunktionen
print(s.lower())
print(s.upper())

print(s.isupper())
print(s.islower())

text = "Ich bin ein Text"
print(text.capitalize())
print(text.title())

print(text.isalpha())
print(text.isalnum())
print(text.isnumeric())

print(text.count("t"))  # Anzahl eines bestimmten Zeichens zählen
print(text.lower().count("t"))  # Groß-/kleinschreibung ignorieren

print(text.split(" "))  # Text anhand eines Trennzeichens in eine Liste aufteilen

text.strip()  # Leerzeichen links und rechts wegschneiden

# Strings verbinden
text1 = "Ich bin"
text2 = "ein Text"
print(text1 + " " + text2)

print(text1 * 10)

# Index
# "An der Stelle"
print(text[0])

print(text[0:3])  # Bereich angreifen
print(text[:3])  # Untergrenze weglassen (vom Anfang bis 3)
print(text[3:])  # Obergrenze weglassen (von 3 alle restlichen Zeichen)

print(text[-1])  # Ende angreifen
print(text[-4:-1] + text[-1])
print(text[-4:])

print(text[:])  # Alles nehmen

# len(Objekt)
# Gibt die Länge eines Objekts zurück
len(text)
print(len(text))

print(text, text1, text2)  # mehrere Texte ausgeben mit print
print(text, text1, text2, sep=", ")  # mehrere Texte ausgeben mit print und Separator

print(324895.32589)

# Arithmetik
zahl1 = 4
zahl2 = 7

print(zahl1 + zahl2)  # Nur die Summe bilden und ausgeben
zahl1 += zahl2  # z2 auf z1 aufaddieren (z1 wird verändert)

print(zahl1 - zahl2)
print(zahl1 * zahl2)
print(zahl1 / zahl2)
print(zahl1 % zahl2)

print(34 ** 2)  # Potenzieren
print(9 ** 0.5)  # Wurzel ziehen

print(15 / 7)
print(15 // 7)  # Ganzzahldivision

# Übungen
i = 4
j = 7
k = 10
summe = i + j + k
potenz = summe ** summe
print(potenz)

print(potenz % 2)

v = "Max"
n = "Mustermann"
print((v + n).lower().count("m"))

print("lukas".title())
print("lukas".capitalize())
print(type(v[0]))

print(len(v + n + text))