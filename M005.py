# List Comprehension
# Aus einem Ausdruck mit einer Schleife eine Liste erzeugen
liste = []
for i in range(10):
	liste.append(i)
print(liste)

print([i for i in range(10)])  # Schleife schreiben -> Buchstabe links

print(list(range(10)))

# Aufgabe: Jede Zahl in der Range von 0 bis 10 quadrieren
print([i ** 2 for i in range(10)])

print([f"{i}^2={i ** 2}" for i in range(1, 11)])

print([(i, f"{i}^2={i ** 2}", i ** 2) for i in range(1, 11)])

# Aufgabe: Jedes Zeichen aus einem String UPPERCASE ausgeben
text = "Ich bin ein Text"
print([z.upper() for z in text])

# Leerzeichen filtern
m = [z.upper() for z in text if z != " "]
m.sort()
print(m)

# Aufgabe: Alle Potenzen die durch 2 teilbar sind
print([i ** 2 for i in range(1, 21) if (i ** 2) % 2 == 0])

print([2 ** i for i in range(1, 32)])
print([f"2^{i}={2 ** i}" for i in range(1, 32)])

# Aufgabe: kleines 1x1 mit LC
print([f"{x} * {y} = {x * y}" for x in range(1, 11) for y in range(1, 11)])

# Booleans als Ergebnis
print([i % 3 == 0 for i in range(1, 100)])

# FizzBuzz als Einzeiler
print(["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else
       "Fizz" if i % 3 == 0 else
       "Buzz" if i % 5 == 0 else
       i for i in range(1, 100)])

# Übung 1
# Schreibe eine List-Comprehension die nur Zahlen aus einer Range von 1 bis inklusive 30 in die neue Liste packt, falls die Zahl durch 6 teilbar ist
# Bevor die Zahl in die neue Liste gepackt wird, soll sie um 12 erhöht werden
print([i + 12 for i in range(1, 31) if i % 6 == 0])

# Übung 2
# Schreibe eine List-Comprehension die aus einem Text alle Kleinbuchstaben nimmt und Groß in die Liste schreibt
text = "Ich bin ein Text"
print([z.upper() for z in text if z.islower()])

# Übung 3
# Schreibe eine List-Comprehension die aus einem Text alle Anfangsbuchstaben nimmt
print([wort[0] for wort in text.split(" ")])
print([z for z in text.title() if z.isupper()])

# Übung 4
# Schreibe eine List-Comprehension die aus einem Text alle Wörter nimmt die 3 oder weniger Zeichen haben
print([wort for wort in text.split(" ") if len(wort) <= 3])