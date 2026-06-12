Projet : NLP Analyse émotionnelle


Détection des émotion humaines à partir de courtes phrases.

Introduction:
Dans ce projet personnel qui a pour objectif d'améliorer mes compétences dans le domaine du machine learning, j'ai entraîné un modèle  de régression logistique afin d'identifier l'émotion dominante dans une phrase courte.  L'application streamlit sera nécessaire pour tester le modèle sur différents échantillons de phrase correspondant à six classes d'émotions Pour ce faire , on transforme le texte brut en une émotion interprétable.
Les émotions sujet à détection:
Joie
Tristesse
Amour
Peur
Surprise
Colère
C'est un modèle qui pourrait potentiellement intégrer une application telle qu'un outil d'analyse ou bien un système interactif.

Etape de la création du modèle
J'ai choisi la création d'une simple pipeline qui à pour charge de:
Nettoyer le texte
Utilisation de la Vectorisation TF-IDF sur la colonne "text" pour le praitraitement
Utilisation d'une GridSearch parmi 3 Pipelines contenant chacun un modèle séléctionnés pour notre cas d'usage.( LogisticRegression, LinearSVC, MultinomialNB). 
Entrainement final avec la pipeline qui à obtenu le meilleurs score. A savoir la régréssion de logisitque.
Création d'un Streamlit permettant de tester le modèle en effectuant un prompt. Elle affichera la classe correspondant au texte une statistique de mesure sur les différentes classes
Une déploiement Docker à était effectuer afin de permettre de tester plus facilement l'application

Mesure de Performance
Oberservation: 
Selon les résultats en dessous le modèle est très performant et généralise bien sur la l'ensemble des classes. Cependant, des faiblesses sur certaines émotions sont à noter, comme celui de la peur qui doit être confondu avec l'émotion surprise, qui d'ailleurs est l'émotion  la plus difficile à reconnaitre.
Acuracy:  89% 
Macro F1-score :  85%
Weighted F1-score 89%

Matrice de confusion:
On peut observer:
Les émotions fortes (tristesse, joie, colère) sont très bien capturées
Les confusions se produisent surtout entre émotions proches (peur, surprise)
Le modèle reste cohérent et stable

Exemple d'utilisation:
Dans le prompt, écrire une courte phrase en anglais. Puis appuyer sur le bouton analyser afin d'afficher la classe de l'émotion correspondant à la phrase. 

Déploiement dans le Docker
Activer le Docker
ligne de commande à entrer dans l'invite de commande Ubuntu:
docker build -t nlp_emotion_app .                 (Pour construire l'image dans le Docker)
docker images                                                   (Vérifier si l'image a bien été construite)
docker run -p 8501:8501 nlp_emotion_app     (Lancer l'interface)

Par la suite, pour ouvrir l'interface streamlit:
Dans une nouvelle fenêtre, entrez dans la barre URL : http://localhost:8501

Structure du projet
-NLP-AnalyseSentiment/ 
??? data/ 
? 
??? model/ ? 
           ??? sentiment_model.pkl ?
 ??? notebooks/ ? 
            ??? 1_EDA.ipynb?
            ??? 2_Prepro_ML.ipynb.ipynb ?
 ??? app.py
 ??? Dockerfile 
??? requirements.txt
??? README.md

Technologies utilisées
 Python
Numpy / Pandas
Scikil-learn
NLP
Streamlit
Docker

Conclusion
Ce projet personnel assez basique m'a permis de monter en compétence dans le domaine du NLP, surtout sur la manière de nettoyer et de prétraiter les données. Ça était pour moi une bonne expérience enrichissante. Cela m'a permis de concevoir une application interactive basée sur un modèle léger et efficace, adaptée à l’analyse d’émotions dans des textes courts. Les évolutions possibles incluent l’ajout de la prise en charge du français, soit via un dataset d’émotions francophone, soit par la création d’un jeu de données dédié, ou encore par la traduction automatique des phrases avant leur traitement par le modèle.

Auteur du projet:   Johann JOURNAUX

