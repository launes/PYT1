# String
mein_name = "Matthias"
dein_name = 'Nick'

mein_spitzname = "Matthias, der 'Löwe'"
mein_spitzname = 'Matthias, der "Löwe"'

fehler = "Hallo"

dies_ist_mehrzeilig = """
Dies ist ein mehrzeiliger
Kommentar als String.

Das geht gaz einfach. 
"""

# Integer
# meineZahl
meine_zahl = 2

# f-String: Sorgt dafür, dass Variablen mit { } in einen String
# integriert werden können
meine_string_variable = f"Meine Lieblingszahl ist : {meine_zahl}"

# Variablen klein schreiben, nach "Pascal-Case"
# Diese Zahlen können "beliebig groß" sein. 
# Es wird soviel Speicher reserviert, wie gebraucht wird.
meine_binaere_zahl = 0b1101

# Variable nimmt nun eine Zahl an, war vorher ein String
# Python erlaubt Neuzuweisungen, der Typ kann sich jederzeit ändern. 
fehler = 86

# Es ergibt sich das Problem des Name shadowings hieraus.
print = 2
print("Hallo", "Welt", 6) 
# Funktionen sind in Python ein eigener Datentyp

del print
# print(type(type))

# Es gibt einzelne, geschützte Worte
# def = 8

# Float
meine_kommazahl = 8.986 # , wird in einer Argumentliste verwendet
# Zertifizierungsfrage 
# Was ist die Ausgabe ? 
print(8.9e2)
print(8.9e-2)

# Boolean
sonne = False
kalt = True

false = False

# Listenliterale (dynamisch, beliebige Typen)
meine_liste = [ 2,3,4,5,"Matthias" ] 

# Tupel (immutabel, d.h. nicht veränderbar) "konstant"
mein_tupel = (6,7,8,9) 

# Es gibt keine Konstanten in Python !
eine_konstante_variable = (8,) 

type(eine_konstante_variable)
# Vorrangoperator ()

# Zuordnung Schlüssel-/Wertpaar, Zugriff über Schlüssel
dictionary = { "Nick" : 30_000,
              "Matthias" : 4_000 }

# Menge ohne Mehrfacheinträge
set_literal = { 9,0,3,9 }

