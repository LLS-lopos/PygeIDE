import pathlib
import sys

from PySide6.QtCore import Slot
from PySide6.QtGui import QGuiApplication, QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout


class IDE(QMainWindow):
    def __init__(self, parent=None, largeur=800, hauteur=600):
        super().__init__(parent)
        moniteur = QGuiApplication.primaryScreen()
        taille_moniteur = moniteur.size()
        self.setWindowTitle("Projet PyGame")
        self.setGeometry(int((taille_moniteur.width() // 2) - (largeur // 2)),
                         int((taille_moniteur.height() // 2) - (hauteur // 2)), largeur, hauteur)

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
        from src.theme.theme import Theme
        menu_theme = Theme(chemin=str(pathlib.Path(__file__).parent.parent / "theme"))
        self.barreMenu.addMenu(menu_theme)
        # Créer l'action de fermer projet
        act_fermer_projet = QAction(QIcon(""), "&Fermer Projet", self)
        act_fermer_projet.setStatusTip("Fermer le projet")
        act_fermer_projet.triggered.connect(self.fermer_projet)
        # Créer l'action de quitter
        act_quitter = QAction(QIcon(""), "&Quitter", self)
        act_quitter.setStatusTip("Quitter le projet")
        act_quitter.setShortcut("Ctrl+Q")
        act_quitter.triggered.connect(self.fonc_Quitter)

        # Associer les actions au menu
        Menu_fichier.addAction(act_fermer_projet)
        Menu_fichier.addSeparator()
        Menu_fichier.addAction(act_quitter)

        # Lier
        self.setMenuBar(self.barreMenu)  # instancier la barre de menu

    @Slot()
    def fermer_projet(self):
        from src.main import Main
        self.run = Main()
        self.run.show()
        print("Fermer Projet")
        self.destroy()

    @Slot()
    def fonc_Quitter(self):
        self.destroy()
        sys.exit()


if __name__ == "__main__":
    app = QApplication([])
    win = IDE()
    win.show()
    sys.exit(app.exec())
