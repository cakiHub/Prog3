import random

class VokabelTrainer:
    """
    Klasse für einen Vokabel Trainer
    """

    def __init__(self, woerter):
        """
        Das ist der Konstruktor
        """
        self.richtige_antworten = 0
        self.falsche_antworten = 0
        self.woerter = woerter

    def hinzufuegen(self):
        """
        Über diese Methode fügt man neue Würter ein
        """
        print("Geben Sie ein Englisches und dann ein Deutsches Wort ein um die Vokabelsammlung zu erweitern")
        while True:
            neues_wort_e = input("Englisches Wort eingeben und mit Enter bestätigen: ")
            if neues_wort_e in self.woerter:
                print(neues_wort_e, "ist schon vorhanden")
                continue
            break
        while True:
            neues_wort_d = input("Deutsches Wort eingeben und mit Enter bestätigen: ")
            if neues_wort_d in self.woerter.values():
                print(neues_wort_d, "ist schon vorhandne")
                continue
            break
        self.woerter[neues_wort_e] = neues_wort_d

    def trainieren(self):
        """
        Über diese Methode fügt man neue Würter ein
        """
        while True:
            fragen_anzahl = input("Geben Sie eine Zahl ein wie oft Sie abgefragt werden wollen: ")
            # fragen_anzahl = int(fragen_anzahl)
            try:
                fragen_anzahl = int(fragen_anzahl)
            except ValueError:
                continue
            else:
                break
        i = 0
        while i < fragen_anzahl:
            i += 1
            key_wort = random.choice(list(self.woerter.keys()))
            input_wort = input("Übersetze: " + key_wort + " ")

            if input_wort.lower() == self.woerter.get(key_wort).lower():
                print("Richtig!")
                self.richtige_antworten += 1
            else:
                print("Falsch :(")
                self.falsche_antworten += 1

    def zuruecksetzen(self):
        """
        Über diese Methode setzt man die richtige und falsche Antworten zurück
        """
        self.richtige_antworten = 0
        self.falsche_antworten = 0

    def ergebnis_ausgabe(self):
        """
        Über diese Methode gibt man die Anzahl der richtigen und falschen Antworten aus
        """
        print("Sie haben", self.richtige_antworten, "Vokabeln richtig und",
              self.falsche_antworten, "falsch beantwortet")
        weiter_lernen = input("Wollen Sie weiter Vokabeln lernen? Geben Sie j für ja oder n für nein ein: ")
        if weiter_lernen.lower() == "j":
            self.starte_training()
        else:
            print("Ende")
            exit()

    def starte_training(self):
        self.zuruecksetzen()
        self.trainieren()
        self.ergebnis_ausgabe()

woerter = {"House":"Haus", "Cat":"Katze", "Nose":"Nase"}s
dict((k.lower(), v.lower()) for k,v in woerter.items()) # meine wörter in kleinbuchstaben umwandeln
vokTrainer = VokabelTrainer(woerter)
wort_hinzufuegen = input("Wollen Sie ein Wort in Ihr Vokabelsammlung hinzufügen? Geben Sie j für ja oder n für nein ein: ")
if wort_hinzufuegen.lower() == "j":
    vokTrainer.hinzufuegen()
vokTrainer.trainieren()
vokTrainer.ergebnis_ausgabe()
