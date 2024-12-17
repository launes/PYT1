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

jahr = int(input("Geben Sie das Jahr ein: "))

if schaltjahr(jahr):
    print(f"{jahr} ist ein Schaltjahr.")
else:
    print(f"{jahr} ist kein Schaltjahr.")