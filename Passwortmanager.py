import os 
import json


print("Herzlich Willkommen!")
print("Ich bin dein Passwortmanager.")
print("")

def prüfe_masterpasswort():
    # Prüfen ob Datei mit Masterpasswort existiert
    if os.path.exists("masterpasswort.txt"):
        print("Bitte gib dein Masterpasswort ein: ")
        eingabe = input("Masterpasswort: ")

        # gespeichertes Passwort aus der Datei lesen
        with open("masterpasswort.txt", "r") as Datei_lesen:
            gespeichertes_masterpasswort = Datei_lesen.read().strip()

        # Vergleich der Eingabe mit dem gespeicherten Passwort
        if eingabe == gespeichertes_masterpasswort:
            print("Zugang erlaubt. Willkommen!")
        else:
            print("Passwort falsch. Das Programm wird beendet!")
            exit()

    # Wenn KEINE Datei existiert, dann ein neues Masterpasswort erstellen
    else:
        print("Es gibt noch kein Masterpasswort. Bitte lege ein neues Masterpasswort fest:")
        input1 = input("Gib das neue Masterpasswort ein: ")
        input2 = input("Gib das Masterpasswort zur Bestätigung erneut ein: ")

        if input1 == input2:
            with open("masterpasswort.txt", "w") as Datei_schreiben_masterpasswort:
                Datei_schreiben_masterpasswort.write(input1)
            print("Masterpasswort wurde gespeichert.")
        else:
            print("Die Passwörter stimmen nicht überein. Das Programm wird beendet!")
            exit()

# Funktion aufrufen
prüfe_masterpasswort()

# Menu erstellen

def Menu():

    while True:
        print("Was möchtest du tun? ")
        print("")
        print("1. Passwörter anzeigen lassen ")
        print("2. Neues Passwort hinzufügen ")
        print("3. altes Passwort löschen ")
        print("4. Masterpasswort ändern ")
        print("5. Beenden ")

    
        wahl = input("Wähle: ")
        wahl = wahl.strip()
        print("DEBUG:", repr(wahl))

    if wahl == "1":
            print("noch nicht fertig!", repr(wahl))

    elif wahl == "2":
            print("noch nicht fertig!")

    elif wahl == "3":
            print("noch nicht fertig!")

    elif wahl == "4":
            print("noch nicht fertig!")

    elif wahl == "5":
            exit()


Menu()

# Liste für gespeicherte Passwörter
Gesamtliste = []
# Passwörter in Liste Laden 
def lade_passwörter():
    if os.path.exists("Passwörter.json"):
        with open("Passwörter.json", "r") as Passwortliste_lesen:
            global Gesamtliste
            Gesamtliste = json.load(Passwortliste_lesen)
            print("Passwörter wurden geladen.")
            
            
# Passwörter hinzufügen 
def passwörter_hinzufügen():
    input_passwort = input("Passwort zum Speichern eingeben: ")
    input_benutzername = input("Benutzername zum Speichern eingeben: ")
    input_webseite = input("Webseite zum Speichern eingeben: ")
    Datenbank = {
        "Passwort": input_passwort,
        "Benutzername": input_benutzername,
        "Webseite": input_webseite
    }
    Gesamtliste.append(Datenbank)
    with open("Passwörter.json", "w") as Datenbank_speichern:
        json.dump(Gesamtliste, Datenbank_speichern, indent=4)
        print("Daten wurden gespeichert.")
        print(Gesamtliste)
    





lade_passwörter()
passwörter_hinzufügen()
