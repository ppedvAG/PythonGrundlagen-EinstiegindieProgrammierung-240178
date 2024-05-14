# Main Methode
# Der Startpunkt vom Skript
# Befindet sich generell am Ende eines Python Skripts
# if __name__ == "__main__": ...

# __name__
# __main__, wenn das Skript direkt ausgeführt wird
# Der Name des Skripts selbst, wenn es durch ein anderes Skript ausgeführt wird
print(__name__)

# Modul Suchpfad
# Definiert, wo das import Statement Module sucht
import sys
for p in sys.path:
	print(p)

# Projektverzeichnis
# C:\Users\lk3\source\repos\Python_Grundkurs_2024_05_13
# C:\Users\lk3\source\repos\Python_Grundkurs_2024_05_13

# Standardumgebung
# C:\Users\lk3\AppData\Local\Programs\Python\Python312\python312.zip
# C:\Users\lk3\AppData\Local\Programs\Python\Python312\DLLs
# C:\Users\lk3\AppData\Local\Programs\Python\Python312\Lib
# C:\Users\lk3\AppData\Local\Programs\Python\Python312

# venv
# C:\Users\lk3\source\repos\Python_Grundkurs_2024_05_13\venv
# C:\Users\lk3\source\repos\Python_Grundkurs_2024_05_13\venv\Lib\site-packages

# Wenn innerhalb dieser Pfade das Modul nicht gefunden werden kann -> ModuleNotFoundError
sys.path.append("C:\\Users\\lk3\\Desktop")

# __init__.py
# Wenn ein Skript innerhalb des gleichen Ordners importiert wird, wird der Inhalt von __init__ ausgeführt
import M007_Test.XYZ

# Externe Pakete
# Pakete von außen können in unser Projekt installiert werden
# Zwei Optionen
# - Python Packages
# - pip install <Paket>
# py -m ensurepip --upgrade

if __name__ == "__main__":
	print("Skript wurde direkt gestartet")