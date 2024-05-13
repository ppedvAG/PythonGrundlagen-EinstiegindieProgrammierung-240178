# List
# Typ, welcher mehrere Werte halten kann

# Liste kann beliebig viele Elemente haben
testList = [1, 2, 3, 4]
print(testList)  # print funktioniert in Python auch auf Listentypen

# Liste kann verschiedene Typen enthalten
testList = [1, 2, "Hallo", True]
print(testList)

# Index
print(testList[0])
print(testList[0:2])
print(testList[-1])

print(len(testList))

# Listenfunktionen
testList.append(3)  # Neues Element am Ende anhängen
print(testList)

testList.append([1, 2, 3])  # Append kann auch verschachtelte Listen erzeugen
print(testList)

testList.extend([1, 2, 3])  # Extend packt die Liste aus
print(testList)

testList.remove([1, 2, 3])  # Remove entfernt das erste Vorkommen des gegebenen Elements
print(testList)

testList.pop(0)  # Pop entfernt ein Element am gegebenen Index
print(testList)

testList += [1]  # += funktioniert wie extend (benötigt eine Liste)
print(testList)

print([1, 2, 3] * 5)

# Tupel
# Funktioniert wie List, kann aber nicht verändert werden
testTupel = (1, 2, 3, 4)
print(testTupel)
print(testTupel[0])
print(len(testTupel))

# Tupel verändern
x = list(testTupel)
x.append(5)
testTupel = tuple(x)
print(testTupel)

# Unpacking
# Listen zerlegen in einzelne Variablen
a, b, c, d, e = testTupel  # Hier müssen 5 Variablen sein
print(a)
print(b)
print(c)
print(d)
print(e)

# Range
# Bereich von X bis Y
print(range(100))  # Nur ein Generator
print(range(5, 100))
print(range(5, 100, 5))  # Schrittgröße mitangeben

print(list(range(100)))  # Nur ein Generator
print(list(range(5, 100)))
print(list(range(5, 100, 5))) # Schrittgröße mitangeben

print(range(0, 1_000_000_000))

# Set
# Funktioniert wie List, aber jedes Element muss eindeutig sein
testSet = {1, 2, 3}
print(testSet)

testSet.add(4)
print(testSet)

testSet.add(4)  # Wird nicht hinzugefügt (kein Fehler)
print(testSet)

testSet.remove(1)
print(testSet)

# Dict
# Funktioniert wie Set, aber jedes Element hat einen Schlüssel
testDict = {
	"Modell": "VW",
	"Typ": "Polo",
	"Baujahr": 2015
}

print(testDict["Typ"])  # Das Dictionary hat String-basierte Schlüssel

testDict["KM"] = 50_000  # Neues Element hinzufügen
testDict["KM"] = 100_000  # Neues Element hinzufügen
print(testDict)

testDict.setdefault("KM", 150_000)  # Fügt den Key hinzu, wenn er noch nicht existiert
print(testDict)

print(testDict.items())  # Alle Items als eine Liste von Tupeln
print(testDict.keys())
print(testDict.values())

# Konvertierungen
# Variablen umformen (ein Typ zum anderen Typ)
y = [1, 2, 3]  # list
z = tuple(y)
u = set(y)
d = list(testDict)
print(d)

print(int(2.5))
print(str(2.5))
print(bool(1))
print(bool(0))
print(bool(testList))  # Prüft ob die Liste leer ist
print(bool([]))
print(bool(None))