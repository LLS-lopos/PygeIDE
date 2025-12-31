import sys

from PySide6.QtCore import Slot
from PySide6.QtGui import QGuiApplication, QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QCheckBox, QWidgetAction
from theme.theme import Theme

class IDE(QMainWindow):
    def __init__(self, parent=None, largeur=800, hauteur=600):
        super().__init__(parent)
        moniteur = QGuiApplication.primaryScreen()
        taille_moniteur = moniteur.size()
        calcul_l = (taille_moniteur.width()//2) - (largeur//2)
        calcul_h = (taille_moniteur.height()//2) - (hauteur//2)
        self.setWindowTitle("PyGame IDE")
        self.setGeometry(int(calcul_l), int(calcul_h), largeur, hauteur)

        self.centre()

    def centre(self):
        # Créer un widget central
        zone_centre = QWidget()
        self.setCentralWidget(zone_centre)

        # Configurer les différents éléments de l'interface
        self.barre_menu()

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
        menu_theme = Theme()
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

    @Slot()
    def fonc_Quitter(self):
        """
        Fermer l'application.

        Détruit la fenêtre principale et quitte l'application.
        """
        self.destroy()
        sys.exit()

if __name__ == "__main__":
    app = QApplication([])
    win = IDE()
    win.show()
    sys.exit(app.exec())