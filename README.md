# Quizz ChatBot – Devine le personnage Mario

Projet de Licence 3 Informatique : un premier modèle de chatbot en Python, sous la forme d'un quiz façon Akinator.
Vous pensez à un personnage de l'univers Mario, le programme pose des questions oui/non jusqu'à le trouver.

## Lancer le jeu

```bash
python3 Projet_IA.py
```

Aucune bibliothèque à installer.

## Fonctionnement

Le programme parcourt un **arbre de décision binaire** : chaque nœud est une question, chaque feuille un personnage.
Selon la réponse (oui ou non), il descend dans la branche correspondante.

Personnages connus au départ : Mario, Luigi, Wario, Peach, Daisy, Rosalina, Bowser, Donkey Kong, Toadette, Birdo et Goomba.

- **Réponses souples** : « oui », « o », « non » ou « n ». Une réponse incomprise est simplement redemandée.
- **Vérification** : le programme demande s'il a trouvé le bon personnage.
- **Apprentissage** : s'il se trompe, il demande le bon personnage et une question pour le distinguer, puis l'ajoute à l'arbre. Le nouveau personnage est reconnu dès la partie suivante, tant que le programme reste ouvert.
- **Rejouer** sans relancer le programme.

## Exemple

```
Le personnage porte-t-il une casquette ? (oui/non) : oui
Sa casquette est-elle rouge ? (oui/non) : non
Sa casquette est-elle verte ? (oui/non) : oui
Votre personnage est-il Luigi ? (oui/non) : oui
J'ai trouvé !
```

Thomas Grosjean
