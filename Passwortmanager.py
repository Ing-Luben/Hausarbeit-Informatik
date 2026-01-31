# Daten Importieren
import os 
import json
import sqlite3



# Passwörter über SQLite hinzufügen NEU
def eintrag_speichern(db_pfad: str, website: str, benutzername: str, passwort: str):
    verbindung = sqlite3.connect(db_pfad)
    datenbank_cursor = verbindung.cursor()

    datenbank_cursor.execute("""
                             Insert into einträge (website, benutzername, passwort)
                             Values (?, ?, ?)
                             """, (website, benutzername, passwort))
    
    
    verbindung.commit()
    verbindung.close() 

    


# Datenbank initialisieren 
def datenbank_initialisieren():
    verbindung = sqlite3.connect("passwortmanager.db")
    cursor = verbindung.cursor()

    

    cursor.execute("""
                   Create table if not exists einträge (
                   id integer primary key autoincrement,
                   website text
                   benutzername text
                   passwort text
                   );
                   """)
    verbindung.commit()
    verbindung.close()

    print("Datenbank wurde geladen!")


db_pfad = "passwortmanager.db"
datenbank_initialisieren()
# Begrüßung
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

prüfe_masterpasswort()


Gesamtliste = []

# Passwörter hinzufügen 

def lade_importdatei(pfad: str) -> list[dict]:
    with open(pfad, "r", encoding="utf-8") as datei:
              daten = json.load(datei)

    spalten = [spalte["name"] for spalte in daten["columns"]]

    einträge = []
    for zeile in daten["rows"]:
        eintrag = dict(zip(spalten, zeile))
        einträge.append(eintrag)

    return einträge


# Passwörter anzeigen lassen
def Passwörter_Anzeigen():
    if Gesamtliste: 
        print("Öffne Passwortliste!\n")

        for nummer, eintrag in enumerate(Gesamtliste, start=1):
            print(F"{nummer}. {eintrag}")
           
    else:
        print("Diese Liste ist leer!")
    Beenden = input("Drücke Enter, um wieder ins Menu zu gelangen! \n")
 
# Passwörter löschen
def Passwörter_Löschen():
    if Gesamtliste:
        Input_löschen = input("Welches Passwört möchstes du löschen? ")
        Input_löschen = Input_löschen.strip()
        Input_löschen = int(Input_löschen) 
        Gesamtliste.pop(Input_löschen - 1)
        with open("Passwörter.json", "w") as Datensatz_löschen:
            json.dump(Gesamtliste, Datensatz_löschen)
    
    else:
        print("Keine Passwörter zum löschen vorhanden!")
        exit()


# Masterpaswort ändern


# Menu Abfrage nach Befehl
def Menu():

    while True:
        print("Was möchtest du tun? ")
        print("")
        print("1. Passwörter anzeigen lassen ")
        print("2. Neues Passwort hinzufügen ")
        print("3. bestehendes Passwort löschen ")
        print("4. Masterpasswort ändern ")
        print("5. Daten importieren")
        print("6. Beenden")

    
        wahl = input("Wähle: ")
        wahl = wahl.strip()

        if wahl == "1":
            Passwörter_Anzeigen()
            

        elif wahl == "2":
            passwörter_hinzufügen()
            
            
        elif wahl == "3":
            Passwörter_Löschen()

        elif wahl == "4":
            print("noch nicht fertig!")


        elif wahl == "5":
            basisordner = os.path.dirname(os.path.abspath(__file__))
            json_Pfad = os.path.join(basisordner, "Test Datenbank - Kopie.json")

            daten = lade_importdatei(json_Pfad)

            print(f"{len(daten)} Einträge geladen!")
            input("Drücke enter, um wieder ins Menu zu gelangen")

        elif wahl == "6":
            exit()

        



Menu()






# Alt: wird durch SQLite ersetzt
def lade_passwörter():
    if os.path.exists("Passwörter.json"):
        with open("Passwörter.json", "r") as Passwortliste_lesen:
            global Gesamtliste
            Gesamtliste = json.load(Passwortliste_lesen)
            print("Passwörter wurden geladen.")
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