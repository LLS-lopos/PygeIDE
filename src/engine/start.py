import pygame


class RunPyGame:
    def __init__(self, nom="PyGame", taille=(800, 600), fps=60):
        super().__init__()
        self.running = True
        self.ecran = (pygame.display.set_mode(taille))
        pygame.display.set_caption(nom)

        self.n_fps = pygame.time.Clock()
        self.fps = fps

    def boucle_event(self):
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                print("Fermeture du jeu...")
                self.running = False
                return

    def affichage(self):
        self.ecran.fill((0, 0, 0))

    def mise_a_jour(self):
        pygame.display.flip()
        self.n_fps.tick(self.fps)

    def demarer(self):
        while self.running:
            self.boucle_event()
            self.affichage()
            self.mise_a_jour()
        pygame.quit()


if __name__ == "__main__":
    pygame.init()
    jeu = RunPyGame()
    jeu.demarer()