import sys

from PySide6.QtCore import Slot
from PySide6.QtGui import QGuiApplication, QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QGridLayout, QSizePolicy, \
    QLabel

from APP.IDE_principal import IDE
from theme.theme import Theme


class Main(QMainWindow):
    def __init__(self, parent=None, largeur=800, hauteur=600):
        super().__init__(parent)
        moniteur = QGuiApplication.primaryScreen()
        taille_moniteur = moniteur.size()
        self.setWindowTitle("PyGame IDE")
        self.setGeometry(int((taille_moniteur.width() // 2) - (largeur // 2)), int((taille_moniteur.height() // 2) - (hauteur // 2)), largeur, hauteur)

        self.centre()

    def centre(self):
        # Créer un widget central
        zone_centre = QWidget()
        self.setCentralWidget(zone_centre)

        # Configurer les différents éléments de l'interface
        self.barre_menu()

        # Créer une disposition en grille pour les widgets
        grille = QGridLayout(zone_centre)
        # Configurer l'espacement et les marges de la grille
        grille.setSpacing(2)  # Espacement entre les cellules
        grille.setContentsMargins(2, 2, 2, 2)  # Marges autour de la grille

        b_creer = QPushButton("+ Créer")
        b_creer.clicked.connect(lambda: self.creer_projet())
        zone1 = self.projet()
        zone1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        zone2 = self.action_projet()
        zone2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        grille.addWidget(b_creer, 0, 0, 1, 2)
        grille.addWidget(zone1, 1, 0, 1, 1)
        grille.addWidget(zone2, 1, 1, 1, 1)

        grille.setColumnStretch(0, 3)
        grille.setColumnStretch(1, 1)

    def barre_menu(self):
        """
        Configurer la barre de menu principale avec les menus Fichier, Option et Thème.

        Crée des éléments de menu et configure la navigation de base de l'application.
        """
        # Créer la barre de menu
        self.barreMenu = self.menuBar()

        # Ajouter les sous-menus principaux
        Menu_fichier = self.barreMenu.addMenu("&Fichier")

        # Ajouter le menu de thème réutilisable
        menu_theme = Theme(chemin="./theme")
        self.barreMenu.addMenu(menu_theme)

        # Créer l'action de quitter
        act_quitter = QAction(QIcon(""), "&Quitter", self)
        act_quitter.setStatusTip("Fermer le lanceur")
        act_quitter.setShortcut("Ctrl+Q")
        act_quitter.triggered.connect(self.fonc_Quitter)

        # Associer les actions au menu
        Menu_fichier.addSeparator()
        Menu_fichier.addAction(act_quitter)

        # Lier
        self.setMenuBar(self.barreMenu)  # instancier la barre de menu

    def projet(self):
        widget = QWidget()
        layout = QVBoxLayout()

        # bouton/zone : îcone + nom de projet et chemin de fichier complet visible

        layout.addWidget(QLabel("Projet"))

        widget.setLayout(layout)
        return widget

    def action_projet(self):
        widget = QWidget()
        layout = QVBoxLayout()

        edition = QPushButton("édition")
        executer = QPushButton("exécuter")
        renommer = QPushButton("renommer")
        supprimer = QPushButton("supprimer")

        edition.clicked.connect(lambda: self.editer_projet())
        executer.clicked.connect(lambda: self.lancer_projet())
        renommer.clicked.connect(lambda: self.renommer_projet())
        supprimer.clicked.connect(lambda: self.supprimer_projet())

        layout.addWidget(QLabel("Option"))
        layout.addWidget(edition)
        layout.addWidget(executer)
        layout.addWidget(renommer)
        layout.addWidget(supprimer)

        widget.setLayout(layout)
        return widget

    @Slot()
    def creer_projet(self):
        print("Création d'un nouveau Projet")

    @Slot()
    def editer_projet(self):
        self.run = IDE()
        self.run.show()
        print("éditer projet")
        self.destroy()

    @Slot()
    def lancer_projet(self):
        print("exécuter projet")

    @Slot()
    def renommer_projet(self):
        print("renommer projet")

    @Slot()
    def supprimer_projet(self):
        print("supprimer projet")

    @Slot()
    def fonc_Quitter(self):
        self.destroy()
        sys.exit()


if __name__ == "__main__":
    app = QApplication([])
    win = Main()
    win.show()
    sys.exit(app.exec())
