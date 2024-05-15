# Lambda
# Funktionen ohne def und Name
# Werden generell nur einmal verwendet als Funktionsparameter

def hallo():
	print("Hallo")

halloLambda = lambda: print("Hallo")  # anonyme Methode

def run(func):
	func()

run(hallo)
run(halloLambda)

# ----------------------------------

# map und filter
# Listen verarbeiten
# Verwenden beide jeweils einen Funktionsparameter um zu definieren, was mit den Elementen passieren soll

# filter
# Filtert eine Liste
bis100 = list(range(100))

# Alle Elemente, welche durch 3 teilar sind
ergebnis = []
for i in bis100:
	if i % 3 == 0:
		ergebnis.append(i)
print(ergebnis)

# Mit filter
def teilbarDurch3(zahl) -> bool:
	return zahl % 3 == 0

# Macht im Hintergrund eine Schleife die bei jedem Element die gegebene Funktion ausführt
print(list(filter(teilbarDurch3, bis100)))

# Mit Lambda-Expression statt einer dedizierten Funktion
print(list(filter(lambda zahl: zahl % 3 == 0, bis100)))

# Mit LC
print([z for z in bis100 if z % 3 == 0])

# ----------------------------------

# map
# Wandelt jedes Element der Liste in einer andere Form um

# bis100 in 2^x Form darstellen

hochX = []
for z in bis100:
	hochX.append(2 ** z)
print(hochX)

# Mit map
def xHoch2(zahl) -> int:
	return 2 ** zahl

print(list(map(xHoch2, bis100)))

# Mit Lambda-Expression
print(list(map(lambda x: 2 ** x, bis100)))

# Mit LC
print([2 ** z for z in bis100])