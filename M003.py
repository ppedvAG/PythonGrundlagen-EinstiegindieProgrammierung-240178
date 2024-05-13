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

# Übung 1
# Wir haben 3 vorgegebene Listen
list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5, 6]
list3 = [5, 6, 7]
# Finde heraus welche Liste die längste ist (es können auch mehrere Listen die längsten sein)
laengen = [len(list1), len(list2), len(list3)]
maxL = max(laengen)
if len(list1) == maxL:
	print("...")
if len(list2) == maxL:
	print("...")
if len(list3) == maxL:
	print("...")

# Übung 2
# Nimm die oberen drei Listen und überprüfe ob eine der Listen eine der drei Zahlen enthält: 3, 7, 10
gesamt = list1 + list2 + list3
if 3 in gesamt or 7 in gesamt or 10 in gesamt:
	print("...")

if len(set(gesamt).intersection([3, 7, 10])) > 0:
	print("3, 7 oder 10 sind enthalten")

intersect = set(gesamt).intersection([3, 7, 10])
if len(intersect) > 0:
	print(str(intersect) + " ist enthalten")


if 3 in list1 or 7 in list1 or 10 in list1:
	print("list1 hat einer der drei Zahlen")
if 3 in list2 or 7 in list2 or 10 in list2:
	print("list2 hat einer der drei Zahlen")
if 3 in list3 or 7 in list3 or 10 in list3:
	print("list3 hat einer der drei Zahlen")