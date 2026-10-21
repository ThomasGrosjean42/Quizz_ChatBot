"""
Quiz façon Akinator sur les personnages de l'univers Mario.
Le programme pose des questions oui/non et parcourt un arbre de décision
jusqu'à trouver le personnage. S'il se trompe, il apprend le nouveau
personnage pour la prochaine partie.

Projet de Licence 3 – Thomas Grosjean
"""


class Node:
    def __init__(self, question=None, yes_node=None, no_node=None, character=None):
        self.question = question
        self.yes_node = yes_node
        self.no_node = no_node
        self.character = character

    def is_leaf(self):
        return self.character is not None


def build_tree():
    # Chaque personnage n'apparaît qu'une seule fois dans l'arbre
    # et peut être trouvé en suivant un seul chemin de réponses.

    # --- Branche « casquette » ---
    casquette_verte = Node("Sa casquette est-elle verte ?",
                           yes_node=Node(character="Luigi"),
                           no_node=Node(character="Wario"))
    casquette_rouge = Node("Sa casquette est-elle rouge ?",
                           yes_node=Node(character="Mario"),
                           no_node=casquette_verte)

    # --- Branche « princesses » ---
    robe_jaune = Node("Porte-t-elle une robe jaune et orange ?",
                      yes_node=Node(character="Daisy"),
                      no_node=Node(character="Rosalina"))
    robe_rose = Node("Porte-t-elle une robe rose ?",
                     yes_node=Node(character="Peach"),
                     no_node=robe_jaune)

    # --- Autres personnages ---
    noeud_rose = Node("Porte-t-il un nœud sur la tête ?",
                      yes_node=Node(character="Birdo"),
                      no_node=Node(character="Goomba"))
    champignon = Node("Sa tête ressemble-t-elle à un champignon ?",
                      yes_node=Node(character="Toadette"),
                      no_node=noeud_rose)
    cravate = Node("Porte-t-il une cravate rouge ?",
                   yes_node=Node(character="Donkey Kong"),
                   no_node=champignon)
    mechant = Node("Est-ce le méchant principal de la série ?",
                   yes_node=Node(character="Bowser"),
                   no_node=cravate)

    princesse = Node("Le personnage est-il une princesse ?",
                     yes_node=robe_rose,
                     no_node=mechant)

    return Node("Le personnage porte-t-il une casquette ?",
                yes_node=casquette_rouge,
                no_node=princesse)


def ask_yes_no(question):
    """Repose la question tant que la réponse n'est pas oui ou non."""
    while True:
        answer = input(question + " (oui/non) : ").strip().lower()
        if answer in ("oui", "o"):
            return True
        if answer in ("non", "n"):
            return False
        print("Je n'ai pas compris, répondez par oui ou non.")


def learn(leaf):
    """Ajoute un nouveau personnage à l'arbre quand le programme s'est trompé."""
    new_name = input("À quel personnage pensiez-vous ? ").strip()
    if not new_name:
        return
    question = input(f"Donnez une question oui/non qui distingue {new_name} de {leaf.character} : ").strip()
    if not question.endswith("?"):
        question += " ?"
    answer_for_new = ask_yes_no(f"Pour {new_name}, la réponse est-elle oui ?")

    old_leaf = Node(character=leaf.character)
    new_leaf = Node(character=new_name)

    # La feuille devient une question, avec l'ancien et le nouveau personnage en dessous
    leaf.question = question
    leaf.character = None
    leaf.yes_node, leaf.no_node = (new_leaf, old_leaf) if answer_for_new else (old_leaf, new_leaf)
    print(f"Merci ! Je connais maintenant {new_name}.")


def play_game(root):
    current = root
    while not current.is_leaf():
        current = current.yes_node if ask_yes_no(current.question) else current.no_node

    if ask_yes_no(f"Votre personnage est-il {current.character} ?"):
        print("J'ai trouvé !")
    else:
        learn(current)


if __name__ == "__main__":
    print("Pensez à un personnage de l'univers Mario, je vais essayer de le deviner.\n")
    root_node = build_tree()
    while True:
        play_game(root_node)
        if not ask_yes_no("\nVoulez-vous rejouer ?"):
            print("À bientôt !")
            break
        print()
