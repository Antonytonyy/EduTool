# GUIDE D'UTILISATION D'EDU TOOL :

Note : Ce projet a été soumis au concours Trophées NSI
<br/>
*Tous les commentaires en italique comme celui-ci s'adresse pour le jury afin qu'ils puissent effectuer les tests de fonctionement*

Utilisation d'Edu Tool au sein d'établissement scolaire :
-----------------

Le logiciel Edu Tool a été créé pour être utilisable dans les réseaux de tous les établissements scolaires (il suffit seulement que les ordinateurs professeurs et élèves puissent communiquer par le biais d'un dossier). C'est un outil pédagogique innovant permettant quasi instantanément le partage de dossiers du professeur vers ses élèves. Il offre un gain de temps considérable dans la transmission des documents que les professeurs souhaitent partager à leurs élèves (cours, évaluations, QCM)
Ainsi, pour l'utiliser au sein de l'établissement scolaire, il convient de suivre les instructions ci-après.

Téléchargement et placement des fichiers :
-----------------
Afin d'exécuter le logiciel Edu Tool, il est nécessaire d'avoir pour logiciel d'exploitation Windows.
<br/>
Tout d'abord, il vous faudra télécharger le dossier ET sur votre ordinateur, puis le positionner dans l'architecture de votre ordinateur (le dossier ET devra se trouver au sein du lieu auquels les ordinateurs élèves et les ordinateurs professeurs peuvent accéder).
<br/>
*Il suffira pour le test de télécharger le dossier ET et de le placer à un endroit quelquonque de votre ordinateur*
<br/>
Puis il vous faudra télécharger, les deux fichiers python : ET Eleve.py et ET Prof.py . Il vous faudra les ouvrir dans un logiciel pouvant exécuter les programmes python (Nous vous conseillons d'utiliser VSCode ou Pyzo).

Modules :
-----------------
Afin d'exécuter ce code, il est nécessaire d'avoir les modules Python suivants:
-	Tkinter
-	Tkinter filedialog
-	Tkinter askopenfile
-	Shutil
-	Os
-	Getpass
-	Time
-	Random


Fichiers classe.txt et prof.txt :
-----------------

Il doit y avoir dans le dossier Classe au moins une liste d’élèves et un fichier texte appelé prof.txt (le dossier Classe se trouve dans le dossier ET).
<br/>
Le fichier prof.txt sera donc comme ceci:

>id_prof_1  
id_prof_2  
...

*Pour ce test, vous pouvez seulement mettre un identifiant de votre choix, cet identifiant sera rappelé dans le fichier prof.py . Il est en fait impossible d'être professeur et élève simultanément dans ce projet. Le fichier prof.txt devra donc être comme ceci:*
>id_de_votre_choix


Le fichier de la liste d'élèves doit être composé en première ligne de l’identifiant du professeur, puis une ligne vierge, puis tous les identifiants des élèves de la classe. Il peut y avoir un nombre infini de fichier liste d'élèves, tous pouvant prendre un nom de votre choix, il est envisageable qu'il y ait des listes d'élèves pour chaque classe, pour chaque spécialité... Ces fichiers devront donc prendre cette forme :

>id_prof  
>  
>id_eleve1  
id_eleve2  
id_eleve3  
id_eleve4  
id_eleve5  
...

<br/>

*Concernant la liste d’élèves, il vous faudra également en créer une avec en première ligne l’identifiant du professeur que vous avez créé auparavant, puis votre identifiant à la place des identifiants élèves. Pous pouvez soit modifier le fichier existant NSI gr1.txt en ajoutant votre identifiant soit en rajouter un nouveau que vous venez de créer. Votre fichier aura ainsi cette forme:*

>id_prof_que_vous_avez_créer  
>  
>votre_identifiant  

Modification des chemins dans le code :
-----------------

Ce code fonctionne sous l'architecture de notre lycée. Or tous les lycées français n'ont pas la même architecture. Quelques modifications s'imposent alors :
<br/>
Pour le fichier ET prof.txt : 
- l16, il faut saisir le chemin absolu du dossier ET (ex: "I:/public/ET")
- l18, il faut saisir le chemin absolu du fichier prof.txt (ex: "I:/public/ET/prof.txt")
<br/>

Pour le fichier ET eleve.txt : 
- l11, il faut saisir le chemin absolu pour accéder au fichier prof.txt (ex: "I:/public/ET/prof.txt")
- l13, il faut saisir le chemin absolu pour accéder au dossier Partage (ex: "I:/public/ET/Partage/")
- l15, il faut saisir le chemin où seront stockés les fichiers du partage, (il vous vaudra modifier la ligne de code tout en gardant "getpass.getuser()" afin que ce lieu soit propre à chaque élève).
<br/>

*Pour le test, vous devrez réaliser l'ensemble des modifications précédentes, ainsi que les suivantes qui sont seulement spécifiques au test :*
Pour le fichier ET prof.txt : 
- l20, il faut saisir l’identifiant du professeur fictif (nom qui a été inscrit dans les fichiers de configuration avant) (ex: albert.einstein)
- l65, il faut mettre des « # » devant cette ligne et les trois suivantes, pour le test vous exécuterez le code élève et le code professeur, néanmoins si lorsque vous quittez la fenêtre professeur, tous les fichiers se suppriment, vous ne pourrez pas utiliser le code élève, ainsi pour le test il faut donc empêcher la suppression des fichiers à la fermeture de la fenêtre.
<br/>

Pour le fichier ET eleve.txt : 
- l15, vous pourrez seulement écrire un lieu au choix de votre ordinateur (ex: "C:/Users/antoine/Documents/")

<br/>
Attention : Il faut veiller à respecter le chemin des dossiers et fichiers
<br/>
Certains nécessitent un / à la fin du chemin alors que d'autres n'en nécessitent pas
<br/>

Exécution du code :
-----------------

Désormais l'ensemble du code est fonctionnel sur votre architecture réseau, il vous suffira donc de donner le fichier ET prof.py à tous les enseignants de votre établissement et le fichier ET Eleve.py à tous les élèves de votre établissement.


Explication du code et explication pour l'utilisation :
-----------------
Partie professeur:
<br/>
Lors de l'exécution du code, une fenêtre nommée Etu Tool et composée de deux onglets apparait.
<br/>

![imagepartag](https://github.com/Antonytonyy/EduTool/blob/main/Img/Onglet%20partage.png)  
<br/>
Le professeur peut alors partager des fichiers à ses élèves, dans ce cas il sélectionne un à un les fichiers qu'il souhaite partager. Il ajoute un titre à son partage puis sélectionne le groupe destinataire des fichiers (ce groupe devra être un de ceux créés précédemment lors de la configuration dans le dossier ET/Classe/). Puis il appuie sur le bouton "Envoyer les fichiers". Cette action aura pour conséquence de copier les documents dans le dossier Partage ainsi que de créer un document appelé partage nom_du_professeur.txt . Quant au bouton "Arrêter le partage", il permet de stopper la diffusion des documents et permet de "reset la page". (cela enlève tout l'affichage, et remet la fenêtre à l'état initial)
<br/>

![imagepartag](https://github.com/Antonytonyy/EduTool/blob/main/Img/Onglet%20QCM.png)  
<br/>
Le professeur peut également faire réaliser un QCM à sa classe. Dans ce cas, il sélectionne un QCM (QCM qu'il a créé avec le bouton créer un nouveau QCM), sélectionne le groupe qui va réaliser le QCM (ce groupe devra être un de ceux créés précédemment lors de la configuration dans le dossier ET/Classe/). Enfin il envoie le QCM à ses élèves. Cette action copiera le QCM dans le dossier QCM et créera un fichier QCM nom_du_professeur.txt qui contiendra le nom du QCM ainsi que le groupe auquel le QCM est destiné. Enfin quand le professeur rafraichit les réponses de ses élèves, le programme parcourt le dossier QCM afin de regarder si un élève a envoyé ses réponses. Dans ce cas, il affiche les réponses de l'élève et détermine une note sur 20.
Le bouton "Réinitialiser le QCM" permet de stopper le QCM, et "reset la page". (cela enlève tout l'affichage, et remet la fenêtre à l'état initial)
<br/>

![imagepartag](https://github.com/Antonytonyy/EduTool/blob/main/Img/Onglet%20creation%20QCM.png)
<br/>
Lorsque le professeur souhaite créer un QCM, il doit d'abord cliquer sur le bouton "Créer un Nouveau QCM", ce qui lui ouvrira une fenetre dans lequel il devra ajouter des questions, des choix, les bonnes réponses serons listés à la suite, exemple ci dessous. Une fois fini, il devra cliquer sur le bouton "Sauvegarder" et une fenêtre s'ouvrira pour lui proposer où enregistrer le fichier. Le QCM sera nommée "QCM nom_du_qcm.txt", les reponses quant à elles seront appelés, "QCM nom_du_qcm co.txt".  

`/!\ Il faut veiller à garder le fichier des réponses dans le même dossier que le fichier du QCM /!\`
<br/>

Partie élève:
<br/>
Lors de l'exécution du code, deux fenêtres apparaissent.
<br/>
Pour le QCM, si le professeur a envoyé un QCM à ses élèves, alors une fenêtre s’ouvre sur l’ordinateur de l’élève avec en affichage le titre du QCM et l’indication de temps pour la réalisation de ce dernier. Puis l’élève doit saisir son nom et son prénom. Si les deux endroits d’écriture (widget Entry) ne sont pas vides alors l’élève peut cliquer sur « Commencer le QCM »; si au moins l’un des deux est vide on affiche « nom et/ou prénom non valide ». L’action de commencer le QCM lance le chronomètre et affiche l’ensemble des questions. 
Pour chacune des questions, il y a le titre de la question, l’ensemble des réponses proposées, une indication sur le nombre de réponses et un bouton « sauvegarder les réponses ». L’élève, après avoir pris connaissance de la question et de son type (une seule réponse/plusieurs réponses), sélectionne la/les réponses puis clique sur "Sauvegarder les réponses". Cela enregistre les réponses de l’élève et le bouton « question n » correspondant devient vert. Quand l’élève a fini son QCM et clique sur « Soumettre réponses » ou que le temps est écoulé, le programme crée un fichier nommé « nom_QCM id_de_l’eleve.txt », ce fichier est placé dans le dossier QCM, et comporte en première ligne l’identifiant de l’élève, en deuxième ligne le nom de l’élève entré précédemment au début du QCM, le prénom de l’élève entré précédemment au début du QCM puis toutes les réponses aux questions. Enfin la fenêtre est détruite.
<br/>


Pour le partage de document, si le professeur a partagé des documents, le programme copie les documents du partage dans l’ordinateur de l’élève et procède à l’affichage de l’ensemble des documents du partage. Si l’élève clique sur l’un des documents, ce dernier s’ouvre avec le logiciel par défaut grâce à la fonction « os.startfile » (pour un fichier .docx si l’on clique dessus, le fichier s’ouvre avec LibreOffice par exemple).

La suite du projet :
-----------------
Ce projet tel qu'il est ici présenté constitue la deuxième version d'Edu Tool.
<br/>
La nouvelle version, Edu Tool v3 est déja en cours de développement et de nouvelles fonctionnalités telles que la possibilité au professeur de partager son écran seront présentes dans cette nouvelle version.



