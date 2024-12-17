def schaltjahr(jahr):
    # Prüfe, ob das Jahr ein Schaltjahr ist
    if jahr % 400 == 0:
        return True  # Ist durch 400 teilbar, also Schaltjahr
    elif jahr % 100 == 0:
        return False  # Ist durch 100 teilbar, aber nicht durch 400, also kein Schaltjahr
    elif jahr % 4 == 0:
        return True  # Ist durch 4 teilbar, also Schaltjahr
    else:
        return False  # Trifft keine der Bedingungen, also kein Schaltjahr

# Beispielaufrufe zur Überprüfung der Funktion
if __name__ == "__main__":
    test_jahre = [1900, 2000, 2024, 2023]  # Liste der zu überprüfenden Jahre
    for jahr in test_jahre:
        ergebnis = schaltjahr(jahr)  # Prüfe, ob das Jahr ein Schaltjahr ist
        if ergebnis:  # Wenn True, dann Schaltjahr
            print(f"Das Jahr {jahr} ist ein Schaltjahr.")
        else:  # Andernfalls kein Schaltjahr
            print(f"Das Jahr {jahr} ist kein Schaltjahr.")