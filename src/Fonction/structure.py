import json
import pathlib

racine = pathlib.Path().home()
dos_conf = racine / ".PygeIDE"

fichier_liste_prog = "pyge_sys_ide.json"
bouton = {
    "icon": None,
    "chemin": "",
    "nom": "",
}

init_prog = {
    "projet_nom": "",
    "projet_dos": "",
    "projet_main": "",
    "projet_icon": None,
}


def base_init():
    if not dos_conf.exists(): dos_conf.mkdir(exist_ok=True)
    if not (dos_conf / fichier_liste_prog).exists():
        with open((dos_conf / fichier_liste_prog), 'w', encoding="utf-8") as f:
            json.dump([], f, indent=4)


if __name__ == "__main__":
    base_init()
