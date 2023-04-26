import subprocess
import os
import tkinter as tk
from tkinter import ttk
import getpass
import shutil
import random



prof="I:/public/ET/Classe/prof.txt"#nom du fichier qui contient la liste des proffesseurs

Partage="I:/public/ET/Partage/"#nom du dossier où les operations sont effectuées

chemin_2="C:/Users/"+str(getpass.getuser())+"/Documents/"#chemin du dossier "Documents" de l'utilisateur où serons copiés le fichiers

QCM=Partage.replace("Partage/","QCM/")#chemin d'où sont placé les QCM


Frame_files=[]

with open(prof, "r",encoding="utf-8-sig") as fichiern:#ouvre le fichier prof pour le lire
    nom_prof=fichiern.readlines()#stocke chaques lignes du fichier dans une meme liste
    professeur=[i.rstrip() for i in nom_prof]#recrée une liste qui contiendra le nom des profs tout en retirant à chaques lignes le retour à la ligne ("\n")

print(professeur)

def icones_images():#programme qui crée un dictionnaire prenant en entrée l'extension (".ext") et renvoie l'icone approprié
    global images_app
    fichier_icones=Partage.replace("Partage/","/Icones")#défini le dossier où se sittue les icones (sous formats .png) nommées tel que : "extension.png"
    images_app={}
    try :#permet d'empecher l'ârret du programme à cause d'erreur non prévisible (permission, fichier corrompu,...)
        for i in os.listdir(fichier_icones):#boucle avec i le nom de chaques fichier dans le dossier prédéfini au dessus
            if i.split(".")[-1]=="png":#verifie que l'extension est bien un ".png" (tkinter ne supporte que les .png)
                images_app["."+i[:-4]]=tk.PhotoImage(file=fichier_icones+"/"+i)#ajout au dico de l'image en tant que son nom sans l'extension, c'est à dire l'extension que l'icone représente
    except Exception as e:
        print(e)#affiche le nom de l'erreur pour pouvoir tenir au courant d'eventuels utilisateurs préocupés

def affichage_fichier(liste):#prends en entrée une liste de fichier (de leur chemin absolu ) et l'affiche
    global Frame_files
    def appercu_on(e):#affiche un appercu de l'image (s'active quand la souris passe sur la case )
        global image_,img_appercu
        n=Frames_files.index(e.widget)#recupere l'indice de la case en recherchant l'indice du widget qui a activé l'event dans la liste des Frames qui ont été bind ( Frames_files )
        image_=tk.PhotoImage(file=liste[n])#ouvre l'image dont le chemin se situe à l'indice n
        img_appercu=tk.Label(root,image=image_)#crée un Label avec l'image
        coordon=e.widget.winfo_rootx(),e.widget.winfo_rooty()#récupere les coordonnées du widget qui a activé l'event
        img_appercu.place(x=coordon[0],y=coordon[1])#place le Label selon les coordonnées

    def appercu_off(e):#suprime l'appercu de l'image
        img_appercu.destroy()
    global focus
    def clic(e):#traite l'information de quand un clic est éffectué sur la fenetre
        if focus:#si la souris est sur l'une des cases
            fichier_a_ouvrir =liste[focus-1]# Spécifier le chemin complet du fichier à ouvrir
            if os.path.exists(fichier_a_ouvrir):# Vérifier si le fichier existe avant de l'ouvrir
                os.startfile(fichier_a_ouvrir)# Ouvrir le fichier avec l'application par défaut
            else:
                print("Le fichier n'existe pas.")
    def focus_on(e):#défini la case sur laquelle la souris passe
        global focus
        focus=Frames_files.index(e.widget)+1#on rajoute 1 car en python 0=False,donc sinon pas de différence entre le premier indice et l'absence d'indice
    def focus_off(e):#défini l'absence de case sous laquelle la souris passe
        global focus
        focus=False
    focus=False
    for i in Frame_files :
        i.destroy()
    F_files=tk.Frame(root)#crée un cadre qui contiendras tout
    F_files.grid(row=0,column=0)#le placer en haut à gauche
    Frames_files=[]#initialise la liste des Frames à vide
    root.bind('<Button-1>',clic)#bind la fenetre ,en cas de clic du bouton principal ,avec la fonction clic
    for n,i in enumerate(liste):#pour chaque éléments de la liste
        Frames_files.append(tk.Frame(F_files))#ajouter un frame a la liste
        b=tk.Label(Frames_files[n],text=i.split("/")[-1],font=("Arial",25))#créer un Label qui affichera le nom du fichier
        img=tk.Label(Frames_files[n])#créer un Label qui affichera l'icone
        b.pack()#le pack
        Frames_files[n].bind('<Enter>', focus_on)#bind la le cadre ,en cas d'entree dans le cadre ,avec la fonction focus_on
        Frames_files[n].bind('<Leave>', focus_off)#bind la le cadre ,en cas de sortie du cadre ,avec la fonction focus_off
        if "."+i.split(".")[-1]==".png" or "."+i.split(".")[-1]==".bmp":#si l'extension est un png
            Frames_files[n].bind('<Enter>',appercu_on)#bind la le cadre ,en cas d'entree dans le cadre ,avec la fonction appercu_on
            Frames_files[n].bind('<Leave>',appercu_off)#bind la le cadre ,en cas de sortie du cadre ,avec la fonction appercu_off
        if "."+i.split(".")[-1] in images_app.keys():#si l'extension est présent dans le dico des icones d'extenion
            img['image']=images_app["."+i.split(".")[-1]]#affiche l'image
        elif 'unknown' in images_app.keys():#si l'icone d'extension inconnue est présent dans le dico des icones d'extenion
            img['image']=images_app["unknown"]#affiche l'image
        img.pack()#le pack
        Frames_files[n].grid(row=n%5,column=1+(n//5)*2,padx=10,pady=10)#le place selon des colonnes de 5

def envoyer_reponses():#enregistre les reponses
    envoi = []#envoi sera une liste contenant les lignes de ce qui sera enregistré
    envoi.append(getpass.getuser())#on y ajout l'identifiant dr l'utilisateur
    envoi.append(nom)# le nom qu'il a choisi
    envoi.append(prenom)# le prenom qu'il a choisi

    if type_QCM=="M":#si l'ordre des question est aléatoire
        answers2=[]
        for i in range(len(ord_questions)):#on remet les réponses dans l'ordre
            position = ord_questions.index(i+1)
            answers2.append(answers[position])
    else:
        answers2=answers#sinon on garde le meme ordre

    for i in answers2:#on ajoute a la liste envoi chaque reponse
        envoi.append(i)
    title=titre#on recupere le nom du QCM de depart
    title=title.replace(".txt","")#on lui enleve l'extension
    title=title +" "+getpass.getuser() + ".txt"#on lui rajoute l'identifiant de l'utilisateur et l'extension ( ce sera le nom du fichier reponse : nom_originel_QCM + nom_user + .txt)

    with open(QCM+title, "w") as f:#on crée le fichier en question dans le repertoire indiqué dans la variable QCM
        for element in envoi:#on ecrit les lignes dans le fichier en parcourant la liste envoi
            f.write(str(element) + "\n")
    QCM_root.destroy()#on détruit la fenetre le QCM est fini

def creation_questions():#crée les boutons pour acceder aux questions
    global bouton_questions
    for i in bouton_questions:#détruit tout les boutons déja éxistants ( si il y en a )
        i.destroy()
    bouton_questions=[]#remet la liste des boutons vide
    for i in range(nbquestions):#fait une boucle
        c='white'#couleur initiale blanche
        if Questions_repondues[i]:#si la question est déjà repondu
            c='green'#la couleur sera verte
        bouton_questions.append(tk.Button(QCM_root, text="Question "+str(i+1),bg=c))#creer un bouton nommée selon le nom de la question et avec en fond la couleur c defini au dessus
        bouton_questions[i].bind("<Button>", affichage_reponses)#bind le button, pour executer la fonction affichage reponse en cas de clic dessus
        bouton_questions[i].place(x=50, y=90+35*i)#le place selon les coordonnées adéquates dont l'ordonnée dépend du numero de la question

def sauvegarder():# souvegarde les reponse a la question actuelle
    global answers,Questions_repondues
    A=""
    for n,i in enumerate(var_buttons):#pour chaques elements de la liste var_buttons, qui contient l'etat des boutons (check ou radio) tel que True = coché
        if i:#si le bouton correspondant est coch"
            A+=str(n+1)#on ajoute son numero
    if not Questions_repondues[last_question]:#si la question n'est pas deja repondue
        Questions_repondues[last_question]=True#on le défini en tant que telle
        creation_questions()#on reconstruit les questions car la couleur de celle complétée change
        answers[last_question]=A#on assigne a la liste des reponses a chaques question a l'indice de la question actuelle les reponse de cette derniere


def affichage_reponses(event):#affiche les reponses a cocher
    global last_question,nb_reponses,question,radio_buttons,sauvegarde,type_question,var_buttons
    if event!=0:#si event est different de 0
        x = bouton_questions.index(event.widget)
    else:#event est égal a 0, notemment lors de l'initialisation
        x=0#la question choisie, est alors la premiere
    last_question=x#on assigne a last question, l'indice de la question actuelle
    for i in radio_buttons:#detruit tout les radio_buttons précédents si il y en a
        i.destroy()
    nb_reponses = int(files[titres_questions3[x]+2])#obtient le nb de reponses
    num_réponse = int(titres_questions3[x]+3)#initialise num_reponse
    type_question = files[titres_questions3[x]+1]#obtient le type de la question

    def selection(e):#gere l'event de quand une des reponses est coché
        global x,var_buttons
        x=radio_buttons.index(e.widget)#recupere l'indice de la reponse associé au bouton qui a lancé l'event en cherchant l'indice de ce dernier dans la liste des boutons
        bool = str(e.widget)[:5]==".!che"#vrai si le widget est un check button donc (".!check_button i" selon la syntaxe tkinter avec i son numero)
        if not bool:#si ce n'est pas vrai
            for n,i in enumerate(radio_buttons):#pour chaques radio_buttons dans la liste ( radio_button car pas des check button)
                i['value']=0# on les desactives
                var_buttons[n]=False# on met leur valeur dans la liste var_button est False car desactivé
            radio_buttons[x]['value']=1 # on active le boutons qui a été cliqué
            var_buttons[x]=True# on met la valuer True a celui qui a été cliqué ( Avec des radio_button , une reponse seulement est possible donc seul le dernier coché est activé)
        else:#est un check button
            var_buttons[x]=not(var_buttons[x])# la valeur ( coché ou décoché <=> True ou False ) est l'inverse de son etat précédent donc en logique booléenne not

    if question:#si il existait une question
        question.destroy()#on la detruit
        sauvegarde.destroy()#on detruit aussi le bouton sauvegarde
    question = tk.Label(QCM_root,text=files[int(titres_questions3[x])],font=("Arial", 20))#on crée le label de la question posée (ex: "Combien de ")
    question.place(x=200,y=100)#place au bon endroit
    radio_buttons=[]#on initialise la liste des buttons
    var_buttons=[]#on initialise la liste valeur des buttons
    if type_question == "S":#si la question n'a qu'une seule reponse
        label_question_type.config(text="Une seule réponse")#on cree un label l'indiquant
        for i in range(nb_reponses):#pour chaque reponses
            var_buttons.append(False)#on ajoute False a la liste des variable des boutons( etat initial desactivé)
            radio_buttons.append(tk.Radiobutton(QCM_root, text=files[num_réponse+i],font=("Arial", 16)))#on ajoute le radio bouton
            radio_buttons[i].bind("<Button>", selection)#on le bind pour qu'il active la fonction selection quand cliqué
            radio_buttons[i].place(x=250, y=150+40*i)#on le place
            radio_buttons[i]['value']=0#on met sa valeur a desactivé

    else :#a plusieurs reponses
        label_question_type.config(text="Plusieurs réponses")#on cree un label l'indiquant
        for i in range(nb_reponses):#pour chaque reponses
            var_buttons.append(False)#on ajoute False a la liste des variables des boutons( état initial desactivé )
            radio_buttons.append(tk.Checkbutton(QCM_root, text=files[num_réponse+i],font=("Arial", 16)))#on ajoute le check bouton
            radio_buttons[i].bind("<Button>", selection)#on le bind pour qu'il active la fonction selection quand cliqué
            radio_buttons[i].place(x=250, y=150+40*i)#on le place

    sauvegarde = tk.Button(QCM_root,text="Sauvegarder les réponses",command=lambda:sauvegarder(),font=("Arial", 14))#on crée le bouton pour sauvegarder les reponses
    sauvegarde.place(relx=0.5,y=nb_reponses*40+200,anchor="center")#on le place

def debuter():#Quand le QCM commence
    global nom,prenom
    global debut
    nom=introduction_Entry_nom.get()#recupere le nom dans l'entry correspondant
    prenom=introduction_Entry_prenom.get()#recupere le prennom dans l'entry correspondant
    if nom !="" and prenom !="":#si les deux sont différent des vide
        debut = False#on commence, en sortant de la boucle
    else :
        z=1

def update_timer():#actualise le chronomètre
    global minutes, seconds
    if seconds == 0: #si les secondes sont a 0
        if minutes == 0:#et les minutes a 0
            envoyer_reponses()#le temps est écoulé donc on envoie les réponses
        else:#si les minuste ne sont pas a 0
            minutes -= 1#on enleve une minute
            seconds = 59# on rajoute 59 s (on converti 1min-1s = 60s-1 = 59s)
    else:#si il reste des secondes
        seconds -= 1#on enleve une seconde
    minutes_label.config(text=str(minutes).zfill(2))#on actualise le label des minutes
    seconds_label.config(text=str(seconds).zfill(2))#on actualise le label des secondes
    root.after(1000, update_timer)#on boucle apres 1s

root = tk.Tk()#crée la fenetre principal
root.geometry("1000x800")#la redimensionne
Partage_Label=tk.Label(root,text="AUCUN PARTAGE EN COURS",font=("Arial", 40,"underline"))#crée un label qui s'enlevera en cas de partage
Partage_Label.grid(column=0)
icones_images()
for i in professeur:#pour chaques proffesseurs
    if os.path.exists(Partage+"partage "+i+".txt") == True:#si il y a un fichier partage nomduprof.txt a leur nom
        with open(Partage+"partage "+i+".txt", "r",encoding="utf-8-sig") as fichiern :#l'ouvrir
            file_partage=fichiern.readlines()
            file_partage=[i.rstrip() for i in file_partage]
            fichiers_partage=file_partage[2:]#la liste des chemin des fichiers partagés
            titre=file_partage[0]#le titre du partage
            eleve=file_partage[1]#le chemin de la liste d'eleve
        print(eleve,titre)
        eleve_dans_la_classe = False #initialise la présence de l'eleve dans la classe a False
        id = getpass.getuser()#recupere l'identifiant de l'eleve
        with open(eleve,"r",encoding="utf-8-sig") as fichiern :#ouvre la liste d'eleve en question
            liste_eleve=fichiern.readlines()
            liste_eleve=[i.rstrip() for i in liste_eleve]
            eleve_dans_la_classe= id in liste_eleve[2:]#Vrai si l'id de l'eleve est present dans liste des noms sauf les 2 premiers (qui ne sont pas consacrés aux élèves)
        print(liste_eleve)
        if eleve_dans_la_classe==True:
            root.title(titre)#nomme la fennetre comme le titre du partage
            Partage_Label["text"]=""
            for j in range(len(fichiers_partage)):#copie chaque fichiers partagés
                try:#empeche l'arret du programme en cas d'erreur (le prof se trompe de permission,...)
                    shutil.copy(Partage+fichiers_partage[j],chemin_2)
                except :
                    probleme=1
            affichage_fichier(fichiers_partage)#affiche les fichiers
        else:
            Partage_Label["text"]="Aucun partage en cours"


    print("lol")
    print(QCM+"QCM "+i+".txt")
    print(os.path.exists( QCM+"QCM "+i+".txt"))
    if os.path.exists( QCM+"QCM "+i+".txt"):#si le fichier QCM est present
        nb_reponses=0
        QCM_root = tk.Tk()
        QCM_root.geometry("900x800")
        debut = True#initialise la valeur de la boucle debut a True
        radio_buttons=[]#initialise la liste des boutons radios
        question=False
        nom=""#initialise le nom
        prenom=""#initialise le prenom
        QCM_root.protocol("WM_DELETE_WINDOW", lambda:envoyer_reponses())#en cas de fermeture de la fenetre envoie les reponses
        with open(QCM+"QCM "+i+".txt", "r",encoding="utf-8-sig") as fichiern :#ouvre le fichier qcm correspondant
            files=fichiern.readlines()#cree une liste a partir du fichier en separant les lignes
            files=[i.rstrip() for i in files]#enleve les retour a la ligne "\n"
            titre=files[1]#recupere le titre du QCM
            eleve=files[0]#recupere le chemin de la liste d eleve
        id = getpass.getuser()#recupere l'identifiant de l'eleve
        with open(eleve,"r",encoding="utf-8-sig") as fichiern :#ouvre le fichier de la liste d'eleve
            files=fichiern.readlines()#cree une liste a partir du fichier en separant les lignes
            files=[i.rstrip() for i in files]#enleve les retour a la ligne "\n"
            eleve_dans_la_classe= id in liste_eleve[2:]#Vrai si l'id de l'eleve est present dans liste des noms sauf les 2 premiers (qui ne sont pas consacrés aux élèves)

        if eleve_dans_la_classe:#si eleve est dans la classe
            with open(QCM+titre, "r",encoding="utf-8-sig") as fichiern :#ouvre le QCM
                files=fichiern.readlines()#cree une liste a partir du fichier en separant les lignes
                files=[i.rstrip() for i in files]#enleve les retour a la ligne "\n"
                type_QCM=files[2]#l'ordre du QCM aleatoire ou non

            QCM_root.title(files[4])#met le titre de la fenetre au titre du QCM
            questions = [x+1 for x in range(int(files[0]))]#cree les question
            ord_questions = list(questions)#cree l'ordre des question avant melange
            if files[2] == "M":#si l'ordre est en mode aleatoire
                random.shuffle(ord_questions)#melange les questions
            titres_questions = [6,]#initialise la variable titres questions a 6 (recherche commence a la 6e ligne )

            for i in range(int(files[0])-1):
                titres_questions.append(titres_questions[-1]+int(files[titres_questions[-1]+2])+4)
            titres_questions2 = list(titres_questions)

            for i in range(int(files[0])):
                titres_questions2[i]=titres_questions[ord_questions[i]-1]
            titres_questions3=list(titres_questions2)

            for i in range(int(files[0])):
                titres_questions2[i]=files[titres_questions2[i]]

            introduction_label_1=tk.Label(QCM_root,text="Vous allez débuter un QCM portant sur :",font=("Arial", 16))#creer un label de texte
            introduction_label_titre=tk.Label(QCM_root,text=files[4],font=("Arial", 20,"underline"))#creer le label du titre du QCM

            if files[1]=="-1":#si il n'ya pas de limite de temps
                introduction_label_temps=tk.Label(QCM_root,text="Ce QCM ne dispose pas de limite de temps",font=("Arial", 16))
            else :
                introduction_label_temps=tk.Label(QCM_root,text="Afin de réaliser ce QCM vous disposez de "+str(files[1])+" minutes",font=("Arial", 16))

            introduction_Button_begin=tk.Button(QCM_root,text="Commencer le QCM",command=lambda:debuter(),font=("Arial", 16))#le bouton pour commencer le QCM
            introduction_Entry_nom=tk.Entry(QCM_root,font=("Arial", 14))#cree l'Entry qui recupere le nom choisi
            introduction_Entry_prenom=tk.Entry(QCM_root,font=("Arial", 14))#cree l'Entry qui recupere le prenom choisi
            introduction_label_nom=tk.Label(QCM_root,text="Nom :",font=("Arial", 14))#cree le label "Nom :"
            introduction_label_prenom=tk.Label(QCM_root,text="Prenom :",font=("Arial", 14))#cree le label "Prenom :"
            introduction_label_2 = tk.Label(QCM_root,text="Nom et/ou prénom non valide, veuillez recommencer")#label qui s'affiche lorsque des noms ou prenoms invalide ont ete tapé
            introduction_label_1.place(relx=0.5, y=80, anchor="center")#le place
            introduction_Button_begin.place(relx=0.5,y=460, anchor="center")#le place
            introduction_label_titre.place(relx=0.5,y=140,anchor="center")#le place
            introduction_label_temps.place(relx=0.5,y=220,anchor="center")#le place
            introduction_Entry_nom.place(relx=0.4,y=300)#le place
            introduction_Entry_prenom.place(relx=0.4,y=340)#le place
            introduction_label_nom.place(relx=0.3,y=300)#le place
            introduction_label_prenom.place(relx=0.3,y=340)#le place

            while debut:
                root.update()#update la fenetere root
                QCM_root.update()#update la fenetre QCM_root
            introduction_label_1.destroy()#detruit le widget
            introduction_Button_begin.destroy()#detruit le widget
            introduction_label_titre.destroy()#detruit le widget
            introduction_label_temps.destroy()#detruit le widget
            introduction_Entry_nom.destroy()#detruit le widget
            introduction_Entry_prenom.destroy()#detruit le widget
            introduction_label_nom.destroy()#detruit le widget
            introduction_label_prenom.destroy()#detruit le widget
            introduction_label_2.destroy()#detruit le widget
            if files[1]!="-1":#si il y a une limite de temps ( son absence etant defini par "-1")
                minutes = int(files[1])
                seconds=0

                minutes_label = tk.Label(QCM_root, text=str(minutes).zfill(2), font=("Helvetica", 50))#cree le Label qui indique les minutes restantes
                minutes_label.place(x=680, y=150)#le place

                deuxpoints=tk.Label(QCM_root, text=":", font=("Helvetica", 50))#creer le Label du ":" qui separe les min est s
                deuxpoints.place(x=760, y=150)#le place

                seconds_label = tk.Label(QCM_root, text=str(seconds).zfill(2), font=("Helvetica", 50))#cree le Label qui indique les secondes restantes
                seconds_label.place(x=780, y=150)#le place

                update_timer()#fait entrer dans la boucle timer qui s'autoactive toutes les s

            label_question_type = tk.Label(QCM_root,text = "")#cree le Label qui indique le type de la question ( 1 ou plusieurs reponses )
            label_question_type.place(relx=0.85,y=250,anchor="center")#le palce

            answers=[""for i in range(int(files[0]))]#initialise la liste des reponses de l'utilisateur a chaques question

            txt1=tk.Label(QCM_root,text=files[4],font=("Arial", 30))#creer un label avec le titre du QCM
            txt1.place(relx=0.5 , y=40,anchor="center")#le place

            nbquestions = int(files[0])#recupere le nb de question depuis le fichier QCM
            bouton_questions=[]#initialise la liste des boutons des questions
            text_question = ["QUESTION ?" for i in range(nbquestions)]#initialise le nom des questions
            Questions_repondues=[False for i in range(nbquestions)] #initialise Question repondue, tel que chaque element des la liste soit False
            creation_questions()#creer les question sur le coté
            affichage_reponses(0)#affiche la premiere question

            fin = tk.Button(QCM_root, text='Soumettre les réponses',command = lambda:envoyer_reponses())#creer le bouton pour soumettre  les reponses
            fin.place(relx=0.5,y=600,anchor="center")#le place
            QCM_root.mainloop()



root.mainloop()