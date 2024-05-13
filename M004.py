# Schleifen
# Code mehrmals ausführen

# Zwei Schleifen
# while-Schleife
# for-Schleife

a = 0
b = 10

while a < b:
	print(a)  # Einrückungen beachten!
	a += 1
print("Nach der Schleife")

# Endlosschleife
while True:
	print("Endlos")
	a += 1
	if a > 500:
		break  # break: Beendet die Schleife

a = 0
while a < b:
	a += 1
	if a == 5:
		continue  # continue: Aller Code nach dem Keyword wird überspringen/Springe zum Schleifenkopf zurück
	print(a)

# for-Schleife
# Muss in Python immer über eine Liste iterieren
# z.B.: Range, List, Tuple, String, Set, Dict, ...

liste = [1, 2, 3, 4, 5]
for element in liste:
	print(element)

# "Klassische for-Schleife"
for i in range(5):
	print(liste[i])

# Schleife über einen String
text = "Das ist ein Text"
for zeichen in text:
	print(zeichen)

# Schleife über Dictionary
testDict = {
	"Modell": "VW",
	"Typ": "Polo",
	"Baujahr": 2015
}

# Key und Value in einer Variable
for kv in testDict.items():
	print(kv[0])
	print(kv[1])

for k, v in testDict.items():
	print(k)
	print(v)

for k in testDict.keys():
	print(k)

for v in testDict.values():
	print(v)

# test = [([1, 2, 3], [4, 5, 6]), ([6, 5, 4], [3, 2, 1]), (1, 2)]
# for a, b, c in test:
# 	print(a)
# 	print(b)
# 	print(c)

# else bei Schleife
# Wird ausgeführt, wenn die Schleife erfolgreich abgelaufen ist (ohne break beendet wurde)
for i in range(10):
	print(i)
else:
	print("Schleife ohne Fehler abgelaufen")

# fstring
# Formatted String
# Code in einen String einbauen
# Mit { } Code einbauen
for i in range(10):
	print("Die Zahl ist: " + str(i))
	print("Die Zahl hoch 2 ist: " + str(i ** 2))
	print(str(i) + "^2=" + str(i ** 2))

	print(f"Die Zahl ist: {i}")
	print(f"Die Zahl hoch 2 ist: {i ** 2}")
	print(f"{i}^2={i ** 2}")

# Verschachtelte Schleifen
for i in range(10):
	for j in range(10):
		print(i + j)  # Gesamt: 100 Durchläufe (10x10)

# Übung 1:
# FizzBuzz
# 1. Schleife schreiben, die von 1 bis inklusive 100 hochzählt
# 2. Wir müssen in der Schleife jede Zahl auf ihre Teilbarkeit prüfen:
# Falls sie durch 3 teilbar ist, soll in der Konsole "Fizz" ausgegeben werden
# Falls sie durch 5 teilbar ist, soll in der Konsole "Buzz" ausgegeben werden
# Falls sie sowohl durch 3 als auch 5 teilbar ist, soll in der Konsole "FizzBuzz" ausgegeben werden
# Falls sie weder durch 3 noch 5 teilbar ist, soll die Zahl selbst in der Konsole ausgegeben werden
# 1, 2, Fizz, 4, Buzz, ..., 14, FizzBuzz
for i in range(100):
	if i % 3 == 0 and i % 5 == 0:
		print("FizzBuzz")
	elif i % 5 == 0:
		print("Buzz")
	elif i % 3 == 0:
		print("Fizz")
	else:
		print(i)


# Übung 2:
# Schreibe eine Schleife die dir alle Zahlen von 1 bis 200 zur Verfügung stellt
# Lass dir jede Zahl erst in der kardinalen und dann daneben in der ordinalen Schreibweise darstellen
# Der Modulo Operator ist hier sehr nützlich
# Zahl + Endung 'st', 'nd', 'rd' oder 'th'
# 1st, 2nd, 3rd, 4th, ..., 21st, 22nd, 23rd, 24th
# Bonus: Berücksichtige alle Zahlen die mit 11, 12 oder 13 enden

for i in range(1, 200):
	if i % 10 == 1 and i % 100 != 11:
		endung = "st"
	elif i % 10 == 2 and i % 100 != 12:
		endung = "nd"
	elif i % 10 == 3 and i % 100 != 13:
		endung = "rd"
	else:
		endung = "th"
	print(f"{i}{endung}")

# Übung 3:
# Stoppuhr
# Bevor die Minute hochtickt, müssen die Sekunden einmal eine vollkommene Umdrehung hinter sich gebracht haben
# time.sleep(Float) Funktion hier nützlich

# Übung 4:
# Erstelle eine Schleife die das kleine Einmaleins von 1 bis 10 berechnet, und jeden einzelnen
# Schritt in der Konsole ausgibt
# "1 x 1 = 1"
# "1 x 2 = 2"
# ...
# "5 x 5 = 25"
# ...
# "7 x 4 = 28"
# ...
# "10 x 10 = 100"
