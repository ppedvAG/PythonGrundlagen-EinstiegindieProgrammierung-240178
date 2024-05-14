# Module
# Code Bibliotheken, welche in unser Skript eingebunden werden können
# Ein Modul ist nur ein normales Python Skript
# In Python können von Skripten nur einzelne Funktionen oder Klassen importiert werden anstatt das gesamte Skript

# Mehrere Möglichkeiten für Import:
# import <Modul>
# from <Modul> import <Member>
# Aliases, *

# ------------------------------------------------------------------------

# WICHTIG: Gesamtes Skript wird ausgeführt
# import turtle
#
# turtle.color('red', 'yellow')
# turtle.begin_fill()
# turtle.setx(-300)
# while True:
#     turtle.forward(400)
#     turtle.left(170)
#     if abs(turtle.pos()) < 1:
#         break
# turtle.end_fill()
# turtle.done()

# ------------------------------------------------------------------------

# Alias
# Pakete umbenennen
# Bei importierten Paketen muss immer der Name des Pakets angegeben werden

# import turtle as t
#
# t.color('red', 'yellow')
# t.begin_fill()
# t.setx(-300)
# while True:
#     t.forward(400)
#     t.left(170)
#     if abs(t.pos()) < 1:
#         break
# t.end_fill()
# t.done()

# ------------------------------------------------------------------------

# from import
# Mit einem from import können Teile eines Skripts importiert werden
# Wenn ein Member per from importiert wird, ist dieser im Skript eingebunden
# -> Kein Paketname notwendig
from turtle import color, begin_fill, setx, forward, left, pos, end_fill, done
# from turtle import *  # Importiert alle Funktion von turtle

# color('red', 'yellow')
# begin_fill()
# setx(-300)
# while True:
#     forward(400)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

# ------------------------------------------------------------------------

import M006
M006.countCase("Das ist ein Text aus M007")

from M006 import maximum, countCase, teilnehmerZusammenbauen
countCase("Das ist ein Text aus M007")