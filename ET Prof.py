import tkinter as tk                    
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import os
import getpass
import shutil

liste_fichiers = []
supprimer_files,Frames_files=[],[]#variables propres à l'affchage des fichiers
last_lenght=0
QCM_reponses = []


chemin_partage="I:/public/ET"

prof="I:/public/ET/prof.txt"

chemin_local="C:/Users/"+getpass.getuser()

nom_prof = getpass.getuser()



def icones_images():#programme qui crée un dictionnaire prenant en entrée l'extension (".ext") et renvoie l'icone approprié
    global images_app
    fichier_icones=chemin_partage+"/Icones"#défini le dossier où se sittue les icones (sous formats .png) nommées tel que : "extension.png"
    images_app={}
    try :#permet d'empecher l'ârret du programme à cause d'erreur non prévisible (permission, fichier corrompu,...)
        for i in os.listdir(fichier_icones):#boucle avec i le nom de chaques fichier dans le dossier prédéfini au dessus
            if i.split(".")[-1]=="png":#verifie que l'extension est bien un ".png" (tkinter ne supporte que les .png)
                images_app["."+i[:-4]]=tk.PhotoImage(file=fichier_icones+"/"+i)#ajout au dico de l'image en tant que son nom sans l'extension, c'est à dire l'extension que l'icone représente
    except Exception as e:
        print(e)#affiche le nom de l'erreur pour pouvoir tenir au courant d'eventuels utilisateurs préocupés

def print_tab(tab):  # Définition de la fonction pour afficher un tableau de manière élégante
    len_max = []  # Liste pour stocker la longueur maximale de chaque colonne
    tableau = ""  # Chaîne de caractères pour construire le tableau

    # Parcours des éléments du tableau pour calculer les longueurs maximales de chaque colonne
    for i in tab:
        s = 0  # Variable pour stocker la somme des longueurs maximales de chaque colonne
        for n, j in enumerate(i):
            j = " " + str(j) + " "  # Ajout d'espaces autour de chaque élément pour l'alignement
            if n >= len(len_max):
                len_max.append(len(j))  # Si la colonne n'existe pas encore dans len_max, on l'ajoute
            elif len_max[n] < len(j):
                len_max[n] = len(j)  # Sinon, on met à jour la longueur maximale si nécessaire
            s += len_max[n]  # On ajoute la longueur maximale de chaque colonne à la somme

    # Construction du tableau avec les éléments du tableau et les longueurs maximales de chaque colonne
    for i in tab:
        tableau += s * "-" + len(len_max) * "-" + "-\n"  # Ligne horizontale supérieure du tableau
        for n, j in enumerate(i):
            k = " " + str(j) + " "  # Ajout d'espaces autour de chaque élément pour l'alignement
            tableau += "|" + k + (len_max[n] - len(k)) * " "  # Ajout de chaque élément aligné dans sa colonne
        tableau += "|\n"  # Séparateur de colonnes
    tableau += s * "-" + len(len_max) * "-" + "-"  # Ligne horizontale inférieure du tableau
    return tableau,s  # Retourne le tableau construit

    
def initialisation():
    global F_files
    def fermeture_fenetre():# Définition de la fonction de fermeture de fenêtre
        """
        # Vérification si le fichier de partage existe, et suppression s'il est présent
        if os.path.exists(chemin_partage+"/Partage"+"/partage "+nom_prof +".txt"):
            os.remove(chemin_partage+"/Partage"+"/partage "+nom_prof +".txt")
        # Vérification si le fichier de QCM existe, et suppression s'il est présent
        if os.path.exists(chemin_partage+"/QCM/QCM "+nom_prof+ ".txt"):
            os.remove(chemin_partage+"/QCM/QCM "+nom_prof+ ".txt")
        """
        print("H2L for ever")
    def fin_partage():# renitialise le paratage
        # Vérification si le fichier de partage existe, et suppression s'il est présent
        if os.path.exists(chemin_partage+"/Partage"+"/partage "+nom_prof +".txt"):
            os.remove(chemin_partage+"/Partage"+"/partage "+nom_prof +".txt")
        ong1_4.config(text="")#supression du texte du label
        ong1_6.config(text="")#supression du texte du label
        ong1_9.config(text="")#supression du texte du label
        ong1_8.delete(0,'end')#supression du texte du label
        b.config(text="")#supression du texte du label
        img.config(text="")#supression du texte du label
        F_files.destroy()#supression du frame

    def fin_QCM():#renitialisation du QCM
        ong2_4.config(text="")#supression du texte du label
        ong2_5.config(state="disabled")#desactivation du texte du bouton
        ong2_6.config(text="")#supression du texte du label
        ong2_7.config(state="disabled")#desactivation du texte du bouton
        ong2_8.config(state="disabled")#desactivation du texte du bouton
        ong2_9.config(text="")#supression du texte du label
        ong2_10.config(text="")#supression du texte du label
        ong2_11.config(text="")#supression du texte du label
        T_Frame.config(text="")#supression du texte du label
        T_lab.config(text="")#supression du texte du label
        # Vérification si le fichier du QCM existe, et suppression s'il est présent
        if os.path.exists(chemin_partage+"/QCM/QCM "+nom_prof+ ".txt") == True:
            os.remove(chemin_partage+"/QCM/QCM "+nom_prof+ ".txt")

    def selection_eleves():
        global destinataire_QCM,file_destinataire_partage

        def destinataire_valide():#
            ong2_10.config(text="Fichier valide")#ecrit sur le bon Label "Fichier valide"
            ong2_5.config(state="normal")#active le bouton suivant

        def destinataire_n_valide():
            ong2_10.config(text="Fichier non valide")#ecrit sur le bon Label "Fichier non valide"

        def affichage_destinataire():
            titre = file_destinataire_partage.split("/")
            ong1_4.config(text=titre[-1])

        file_destinataire_partage = filedialog.askopenfilename(initialdir="/Users/antoine/Desktop/ET/Classes", title="Destinataire du QCM" ,filetypes=[('All Files', '*.*')])
        if file_destinataire_partage != "":
            titre_doc=file_destinataire_partage.split("/")
            titre_doc=titre_doc[-1]
            ong2_9.config(text=titre_doc)
            titre_doc=titre_doc.split(".")
            if titre_doc[-1]=="txt":
                fichiern = open(file_destinataire_partage, "r",encoding="ISO-8859-1")
                files=fichiern.readlines()
                fichiern.close()
                affichage_destinataire()
                prof=files[0]
                prof=prof.replace("\n","")
                if prof== nom_prof:
                    destinataire_valide()
                    destinataire_QCM=file_destinataire_partage
                else : 
                    destinataire_n_valide()
            else:
                destinataire_n_valide()

    def upload_destinataire_partage():
        global destinataire

        def destinataire_valide():
            ong1_6.config(text="Fichier valide")#ecrit sur le bon Label "Fichier valide"
            ong1_5.config(state="normal")#active le bouton suivant

        def destinataire_n_valide():
            ong1_6.config(text="Fichier non valide")#ecrit sur le bon Label "Fichier non valide"

        def affichage_destinataire():
            titre = file_destinataire_partage.split("/")
            ong1_4.config(text=titre[-1])
        
        file_destinataire_partage = filedialog.askopenfilename(initialdir="/Users/antoine/Desktop/ET/Classes", title="Destinataire du QCM" ,filetypes=[('All Files', '*.*')])
        if file_destinataire_partage != "":
            titre_doc=file_destinataire_partage.split("/")
            titre_doc=titre_doc[-1]
            titre_doc=titre_doc.split(".")
            if titre_doc[-1]=="txt":
                fichiern = open(file_destinataire_partage, "r",encoding="ISO-8859-1")
                files=fichiern.readlines()
                fichiern.close()
                affichage_destinataire()
                prof=files[0]
                prof=prof.replace("\n","")
                if prof== nom_prof:
                    destinataire_valide()
                    destinataire=file_destinataire_partage
                else : 
                    destinataire_n_valide()
            else:
                destinataire_n_valide()

    global ong2_4,ong2_5

    def affichage_reponses():
        global QCM_reponses,T_Frame,T_lab
        reponses = []
        fichiern = open(file_QCM_d+" co.txt", "r",encoding="ISO-8859-1")
        files=fichiern.readlines()
        correction=[i.rstrip() for i in files]
        fichiern.close()
        base = ["identifiant","Nom","Prénom"]

        for i in range(len(correction)):
            base.append(str(i+1))
        base.append("Note")
        basec = ["Correction","Correction","Correction"]

        for i in range(len(correction)):
            basec.append(correction[i])
        basec.append(20)
        reponses.append(base)
        reponses.append(basec)
        fichiern = open(file_destinataire_partage, "r",encoding="ISO-8859-1")
        files=fichiern.readlines()
        eleve=[i.rstrip() for i in files]
        fichiern.close()

        for i in range(len(eleve)-2):
            chemin = chemin_partage+"/QCM/"+ titre_QCM+" "+ eleve[i+2] +".txt"
            if os.path.exists(chemin) == True:
                fichiern = open(chemin, "r",encoding="ISO-8859-1")
                files=fichiern.readlines()
                reponse_eleve=[i.rstrip() for i in files]
                score=0
                for i in range(len(correction)):
                    if len(correction[i])==1:
                        if correction[i]==reponse_eleve[i+3]:
                            score+=1
                    else :
                        reponses_attendues=[]
                        for c in correction[i]:
                            reponses_attendues.append(c)
                        reponses_utilisateur=[]
                        for c in reponse_eleve[i+3]:
                            reponses_utilisateur.append(c)
                        count=0
                        for x in reponses_attendues:
                            if x in reponses_utilisateur:
                                count += 1
                        score+=count/len(reponses_attendues)
                        
                score=(score/len(correction))*20
                note=int(score)
                if score>note:
                    note+=1
                reponse_eleve.append(note)
                fichiern.close()
                reponses.append(reponse_eleve)

        T_Frame=tk.Frame(tab2)
        T_Frame.place(relx=0.5,y=350,anchor="n")
        T_listbox=tk.Listbox(T_Frame,height=10,width=print_tab(reponses)[1], font='TkFixedFont', bg='grey')
        T_listbox.pack()
        for n,i in enumerate(print_tab(reponses)[0].split("\n")):
            T_listbox.insert(n,i)
        """
        T_lab=tk.Label(T_Frame, text=print_tab(reponses), font='TkFixedFont')
        T_lab.pack(padx=10, pady=10)
        """


    def envoi_QCM():
        global titre_QCM
        ong2_11.config(text="Le QCM a été envoyé")
        ong2_7.config(state="normal")
        shutil.copy(file_QCM,chemin_partage+"/QCM")
        with open(chemin_partage+"/QCM/"+file_QCM.split("/")[-1],'a') as a:
            a.write("")
        if os.path.exists(chemin_partage+"/QCM/QCM "+nom_prof+ ".txt") == True:
            os.remove(chemin_partage+"/QCM/QCM "+nom_prof+ ".txt")
        envoi_QCM=[]
        envoi_QCM.append(destinataire_QCM)
        envoi_QCM.append(nom_file_QCM)
        titre_QCM = nom_file_QCM
        titre_QCM=titre_QCM.replace(".txt","")
        with open(chemin_partage+"/QCM/QCM "+nom_prof+ ".txt", "w") as f:
            for element in envoi_QCM:
                f.write(str(element) + "\n")
        f.close()
        
    def upload_QCM():
        global nom_file_QCM,file_QCM,file_QCM_d

        def affichage_QCM():
            ong2_8.config(state="normal")

        def QCM_valide():
            ong2_4.config(text="Le fichier est valide")

        def QCM_n_valide():
            ong2_4.config(text="Le fichier n'est pas valide")
            
        file_QCM = filedialog.askopenfilename(initialdir='C:', title='Télécharger un QCM',filetypes=[('All Files', '*.*')])

        if file_QCM :
            file_QCM_d=file_QCM.replace(".txt","")
            nom_file_QCM=file_QCM.split("/")
            nom_file_QCM=nom_file_QCM[-1]
            verification = nom_file_QCM.split(" ")
            ong2_5.config(state="disabled")
            ong2_6.config(text=nom_file_QCM)
            
            if verification[0] == "QCM":
                affichage_QCM()
                QCM_valide()
            else :
                QCM_n_valide()
            
    def nouveau_QCM():#ouvre une fenetre permettant la creation de QCM
        global liste_question
        QCM_root=tk.Tk()#creer le fenetre de creation de qcm
        QCM_root.title("Crétation d'un nouveau QCM")#la nomme en tant queue telle

        def ajouter_choix(e):#ajoute un choix, une reponses disponible
            global liste_question
            indice_question=[i[2] for i in liste_question].index(e.widget)#recupere l'indice de la question en recherchant dans la liste des widgets propres aux question au 3e emplacement (i[2]) le widget qui a lancé la fonction
            liste_question[indice_question][1].append(tk.Entry(liste_question[indice_question][1][0]))# ajoute un entry a la liste des entry des reponses
            liste_question[indice_question][1][-1].pack(side='left')#le place

        def New_question():
            global liste_question
            liste_question.append([tk.Entry(QCM_root,width=40),[tk.Frame(QCM_root,bg='green')],tk.Button(QCM_root,text="Ajouter un choix"),tk.Label(QCM_root,text="Question "+str(len(liste_question)+1)),tk.Entry(QCM_root),tk.Label(QCM_root,text="Numéro de/des reponse(s) :")])#ajoute tout les widget propres a une nouvelle question
            liste_question[-1][0].grid(column=1,row=len(liste_question*2)+2,padx=10,pady=10)#les placent
            liste_question[-1][3].grid(column=0,row=len(liste_question*2)+2,padx=10,pady=10)# 
            liste_question[-1][2].grid(column=2,row=len(liste_question*2)+2,padx=10,pady=10)# 
            liste_question[-1][4].grid(column=4,row=len(liste_question*2)+2,padx=10,pady=10)# 
            liste_question[-1][5].grid(column=3,row=len(liste_question*2)+2,padx=10,pady=10)# 
            liste_question[-1][2].bind("<Button>", ajouter_choix)#
            liste_question[-1][1][0].grid(column=0,row=len(liste_question*2)+3,padx=10,pady=10,columnspan=5)# 

        def retirer_question():#nom explicite
            global liste_question
            for n,i in enumerate(liste_question[-1]):#detruit tout les élements du dernier element de la liste
                if n!=1:#si n'est pas le deuxieme element qui est lui meme une sous liste
                    i.destroy()#le detruit
                else:
                    for j in i:#detruit tout les elements present dans le second element
                        j.destroy()
            liste_question=liste_question[:-1]#enleve le dernier element de la liste

        def sauvegarder():#sauvegarde le QCM créé
            texte=str(len(liste_question))+"\n"#initialise texte ( ce qui sera ecris dans le QCM au format texte, selon une structure ordonnée précise cf. documentation )
            if Entry_timer.get()!="":#si l'Entry dedié au temps n est pas vide
                texte+=Entry_timer.get()+"\n"#il y a une limite de temps qu'on recupere
            else:#sinon pas de limite
                texte+="-1\n"#on rajoute alors -1
            if is_random:#si le check button aleatoir est coché
                texte+="M\n\n"#on ajoute M pour melangé
            else:#sinon
                texte+="O\n\n"#on ajoute O pour ordonnée
            texte+=Entry_nom.get()+"\n\n"#ajoute 2 retour a la ligne selon la norme de structure
            for i in liste_question:#pour chaque question
                texte+=i[0].get()+"\n"#ajoute l'entry de la question posée
                if len(i[4].get())>1:#si il y a plusieurs réponses
                    texte+="M\n"#on ajoute M pour multiple
                else:#sinon
                    texte+="S\n"#on ajoute S pour single
                texte+=str(len(i[1])-1)+"\n"#ajoute le nombre de reponses
                for j in i[1][1:]:#pour chaques reponses
                    texte+=j.get()+"\n"#recupere la valeur de l'entry associé
                texte+="\n"
            texte2=""#intialise les reponses aux questions
            for i in liste_question:#pour chaque reponses
                texte2+=i[4].get()+"\n"#ajoute la liste des bonnes reponses (liste des numeros)
            chemin=filedialog.askdirectory()#demande a l'utilisateur de choisir ou sera enregistrer le dossier
            
            try :#evite les erreurs
                 with open(chemin+"/QCM "+Entry_nom.get()+".txt","w") as f:#cree un fichier QCM titre.txt
                     f.write(texte)#y ecrit texte 
                 with open(chemin+"/QCM "+Entry_nom.get()+" co.txt","w") as f:#cree un fichier QCM titre co.txt (co pour correction,donc avec les reponses)
                     f.write(texte2)#y ecrit texte2 
            except Exception as e:
                print(e)

        liste_question=[]
        is_random=False
        Bouton_new_question=tk.Button(QCM_root,text="Ajouter une question",command=New_question)
        Bouton_new_question.grid(column=0,row=0,padx=10,pady=10)

        Bouton_save=tk.Button(QCM_root,text="Sauvegarder",command=sauvegarder)
        Bouton_save.grid(column=1,row=0,padx=10,pady=10)

        Entry_timer=tk.Entry(QCM_root)
        Entry_timer.grid(column=2,row=1,padx=10,pady=10)

        Label_timer=tk.Label(QCM_root,text="        Temps en minutes pour le QCM (vide si sans limite) :        ")
        Label_timer.grid(column=1,row=1,padx=10,pady=10)

        Label_nom=tk.Label(QCM_root,text="Nom du QCM :")
        Label_nom.grid(column=2,row=0,padx=10,pady=10)

        Entry_nom=tk.Entry(QCM_root)
        Entry_nom.grid(column=3,row=0,padx=10,pady=10)

        Label_random=tk.Label(QCM_root,text="Ordre aléatoire")
        Label_random.grid(column=4,row=0,padx=10,pady=10)

        Case_random=tk.Checkbutton(QCM_root,variable=is_random)
        Case_random.grid(column=4,row=1,padx=10,pady=10)

        Bouton_new_question=tk.Button(QCM_root,text="Retirer la dernière question",command=retirer_question)
        Bouton_new_question.grid(column=0,row=1,padx=10,pady=10)

        root.mainloop()

    def envoi_document():
        envoi = []
        titre = ong1_8.get()
        envoi.append(titre)
        envoi.append(destinataire)

        for i in liste_fichiers:
            intermediate = i.split("/")
            envoi.append(intermediate[-1])
            shutil.copy(i,chemin_partage+"/Partage")

        with open(chemin_partage+"/Partage"+"/partage "+nom_prof +".txt", "w") as f:
            for element in envoi:
                f.write(str(element) + "\n")
        f.close()
        ong1_9.config(text="Les fichiers ont étés partagés")
    
    def affichage_fichiers_partages():
        global supprimer_files,Frames_files, b, img, supprimer_files, F_files

        def supprimer_fichier(x):
            global liste_fichiers
            indice_element_suprime = supprimer_files.index(x.widget)
            liste_fichiers.pop(indice_element_suprime)
            affichage_fichiers_partages()

        def appercu_on(e):
            global image_,img_appercu
            n=Frames_files.index(e.widget)
            if "."+liste_fichiers[n].split(".")[-1]==".png":
                image_=tk.PhotoImage(file=liste_fichiers[n])
            else:
                image_=tk.BitmapImage(file=liste_fichiers[n])
            img_appercu=tk.Label(root,image=image_)
            coordon=e.widget.winfo_rootx(),e.widget.winfo_rooty()
            img_appercu.place(x=coordon[0],y=coordon[1])

        def appercu_off(e):
            img_appercu.destroy()

        F_files.destroy()


        F_files=tk.Frame(tab1,bg='grey')
        F_files.place(relx=0.05,rely=0.2)

        for i in supprimer_files+Frames_files:
            i.destroy()
        supprimer_files,Frames_files=[],[]

        for n,i in enumerate(liste_fichiers):
            Frames_files.append(tk.Frame(F_files))
            b=tk.Label(Frames_files[n],text=i.split("/")[-1])
            img=tk.Label(Frames_files[n])
            b.pack()
            if "."+i.split(".")[-1]==".png" or "."+i.split(".")[-1]==".bmp":
                Frames_files[n].bind('<Enter>',appercu_on)
                Frames_files[n].bind('<Leave>',appercu_off)
            if "."+i.split(".")[-1] in images_app.keys():
                img['image']=images_app["."+i.split(".")[-1]]
            elif '.unknown' in images_app.keys():
                img['image']=images_app["unknown"]

            img.pack()
            Frames_files[n].grid(row=n%5,column=1+(n//5)*2,padx=10,pady=10)

            supprimer_files.append(tk.Button(F_files, text="Supprimer"))
            supprimer_files[n].bind("<Button>", supprimer_fichier)
            supprimer_files[n].grid(row=n%5,column=2+(n//5)*2,padx=10,pady=10)

    def upload_file():
        global liste_fichiers
        file = filedialog.askopenfilename(initialdir='C:', title='Télécharger un fichier à partager',filetypes=[('All Files', '*.*')])
        if file :
            liste_fichiers.append(file)

        affichage_fichiers_partages()
    root = tk.Tk()
    root.title("Edu Tool")
    root.geometry("1200x900")
    tabControl = ttk.Notebook(root)
    
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    
    tabControl.add(tab1, text ='Partage')
    tabControl.add(tab2, text ='QCM')
    tabControl.pack(expand = 1, fill ="both")
    


    ong1_1 = tk.Label(tab1,text ="Partage de fichiers")
    ong1_1.place(relx=0.5,y=50, anchor="center")
    ong1_1.config(font=("Arial", 30))

    ong1_2 = tk.Button(tab1, text='Télécharger un fichier',command = lambda:upload_file())
    ong1_2.place(relx=0.15,y=100,anchor="center")

    ong1_3 = tk.Button(tab1, text='Destinataire du partage',command = lambda:upload_destinataire_partage())
    ong1_3.place(relx=0.75,y=270,anchor="center")

    ong1_4 = tk.Label(tab1,text="")
    ong1_4.place(relx=0.75,y=320,anchor="center")

    ong1_5 = tk.Button(tab1, text='Envoyer les fichiers',command = lambda:envoi_document(),state="disabled")
    ong1_5.place(relx=0.75,y=450,anchor="center")

    ong1_6 = tk.Label(tab1,text ="")
    ong1_6.place(relx=0.75,y=360,anchor="center")

    ong1_7 = tk.Label(tab1,text ="Titre du partage des fichiers")
    ong1_7.place(relx=0.75, y=170,anchor="center")

    ong1_8 = tk.Entry(tab1)
    ong1_8.place(relx=0.75,y=200,anchor="center")

    ong1_9 = tk.Label(tab1,text ="")
    ong1_9.place(relx=0.75, y=490,anchor="center")

    ong1_10 = tk.Button(tab1, text="Arreter le partage",command = lambda:fin_partage(),state="normal")
    ong1_10.place(relx=0.5,y=500,anchor="center")



    ong2_1 = tk.Label(tab2,text ="QCM")
    ong2_1.place(relx=0.5,y=50, anchor="center")
    ong2_1.config(font=("Arial", 30))

    ong2_2 = tk.Button(tab2, text='Télécharger un QCM',command = lambda:upload_QCM())
    ong2_2.place(relx=0.15,y=130,anchor="center")

    ong2_3 = tk.Button(tab2, text='Créer un nouveau QCM',command = lambda:nouveau_QCM())
    ong2_3.place(relx=0.85,y=130,anchor="center")

    ong2_4 = tk.Label(tab2,text ="")
    ong2_4.place(relx=0.35,y=130, anchor="center")

    ong2_5 = tk.Button(tab2, text='Commencer le QCM',command = lambda:envoi_QCM(),state="disabled")
    ong2_5.place(relx=0.15,y=210,anchor="center")

    ong2_6 = tk.Label(tab2,text = "")
    ong2_6.place(relx=0.55,y=130, anchor="center")

    ong2_7 = tk.Button(tab2, text='Rafraichir les réponses',command = lambda:affichage_reponses(),state="disabled")
    ong2_7.place(relx=0.55,y=210,anchor="center")

    ong2_8 = tk.Button(tab2, text='Sélectioner les élèves',command = lambda:selection_eleves(),state="disabled")
    ong2_8.place(relx=0.15,y=170,anchor="center")

    ong2_9 = tk.Label(tab2,text = "")
    ong2_9.place(relx=0.35,y=170,anchor="center")

    ong2_10 = tk.Label(tab2,text = "")
    ong2_10.place(relx=0.55,y=170,anchor="center")

    ong2_11 = tk.Label(tab2,text = "")
    ong2_11.place(relx=0.35,y=210,anchor="center")

    ong2_12 = tk.Button(tab2, text="Réinitialiser le QCM",command = lambda:fin_QCM(),state="normal")
    ong2_12.place(relx=0.5,y=500,anchor="center")


    F_files=tk.Label(tab1)
    root.protocol("WM_DELETE_WINDOW", fermeture_fenetre())

    icones_images()
    root.mainloop()



initialisation()

#Fichier validé par Antoine

#A supprimer quand patch :
#Zone reste grise après avoir supprimé un document