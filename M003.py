# Kontrollstrukturen

# if-Anweisung
z1 = 4
z2 = 7
if z1 > z2:
	print("z1 ist größer als z2")  # Einrückungen beachten!

if z1 > z2:
	print("z1 ist größer als z2")  # Einrückungen beachten!
elif z1 < z2:
	print("z2 ist größer als z1")
else:
	print("z1 gleich z2")
print("Nach der Else")  # Keine Einrückung: Nach der Else, eine Einrückung: In der Else

# Vergleichsoperatoren
# ==, !=, <, >=, >, <=

# Logische Operatoren
# and, or, not
# is, in

if z1 > z2 and z1 > 5:
	print("Zwei Bedingungen")

if z1 > z2 and not z1 > 5:
	print("Not")

# &: Und
# |: Oder
# ~: Nicht
if z1 > z2 & ~(z1 > 5):
	print("Test")

# in
# Prüft, ob ein Wert in einer Liste ist
liste = [1, 2, 3, 4, 5]
if 2 in liste:
	print("Zwei ist in der Liste enthalten")

if 2 not in liste:
	print("Zwei ist nicht in der Liste enthalten")

# is
# Vergleicht zwei Speicheradressen (Sind zwei Objekte gleich?)
liste2 = [1, 2, 3, 4, 5]
if liste is liste2:
	print("Liste1 und Liste2 sind das gleiche Objekt")

# Ternary Operator
# Macht if/elif/else kompakter

# if z1 > z2:
# 	print("z1 ist größer als z2")  # Einrückungen beachten!
# elif z1 < z2:
# 	print("z2 ist größer als z1")
# else:
# 	print("z1 gleich z2")

print("z1 ist größer als z2") if z1 > z2 else print("z2 ist größer als z1") if z1 < z2 else print("z1 gleich z2")
print("z1 ist größer als z2" if z1 > z2 else "z2 ist größer als z1" if z1 < z2 else "z1 gleich z2")
# while True:
#       Statement, if, else, ...