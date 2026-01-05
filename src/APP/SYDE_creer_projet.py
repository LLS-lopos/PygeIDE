import json

from Fonction.structure import dos_conf, fichier_liste_prog, bouton, init_prog
from PySide6.QtWidgets import QGridLayout, QLineEdit, QPushButton, QWidget, QLabel


class CreerProjet(QWidget):
    def __init__(self):
        super().__init__()
        # Créer la disposition de la fenêtre
        conteneur = QGridLayout()
        conteneur.setContentsMargins(2, 2, 2, 2)
        conteneur.setSpacing(2)

        # Créer les champs de saisie
        self.nom_projet = QLineEdit()
        self.dos_projet = QLineEdit()
        self.qfile_projet = QPushButton("*")
        self.fichier_principal = QLineEdit()
        self.qfile_main = QPushButton("*")

        b_appliquer = QPushButton("Appliqué")
        b_appliquer.clicked.connect(lambda: self.appliquer())

        conteneur.addWidget(QLabel("Nom du projet: "), 0, 0, 1, 1)
        conteneur.addWidget(self.nom_projet, 0, 1, 1, 3)
        conteneur.addWidget(QLabel("Dossier du projet: "), 1, 0, 1, 1)
        conteneur.addWidget(self.dos_projet, 1, 1, 1, 2)
        conteneur.addWidget(self.qfile_projet, 1, 3, 1, 1)
        conteneur.addWidget(QLabel("fichier principal: "), 2, 0, 1, 1)
        conteneur.addWidget(self.fichier_principal, 2, 1, 1, 2)
        conteneur.addWidget(self.qfile_main, 2, 3, 1, 1)

        conteneur.addWidget(b_appliquer, 3, 0, 1, 4)

        self.setLayout(conteneur)

    def appliquer(self):
        nom = self.check_nom()
        chemin = self.check_dossier()
        icon = self.check_icon()
        main = self.check_main()

        file_unique = str(nom) + ".json"
        if not (dos_conf / file_unique).exists():
            (dos_conf / file_unique).touch(exist_ok=True)
        else:
            print(f"le fichier {(dos_conf / file_unique)} existe déjà !!!")
            return
        # créer un fichier individuel par projet
        init_prog["projet_nom"] = nom
        with open((dos_conf / file_unique), 'w', encoding="utf-8") as f:
            json.dump(init_prog, f, indent=4)

        # ajouter l'accès au projet dans le main
        with open((dos_conf / fichier_liste_prog), 'r') as f:
            info: list = json.load(f)
        bouton["nom"] = nom
        info.append(bouton)

        with open((dos_conf / fichier_liste_prog), 'w', encoding="utf-8") as f:
            json.dump(info, f, indent=4)

        self.destroy()

    def check_nom(self):
        if self.nom_projet.text() != "":
            return self.nom_projet.text()

    def check_dossier(self):
        pass

    def check_icon(self):
        pass

    def check_main(self):
        pass
