import Tkinter
import time
from client import Reseau

r=Reseau()

'''
################################################ BUGS A CORRIGER ############################################
   -Probleme pour cacher et faire apparaitre l'historique des achats/ventes
   -Mettre variable des scales directement, sans le bouton valider
   -Recuperer les variables dans r.ask ... -> [('banque', 250.0, 400000)]



################################################ FONCTIONNALITES #############################################
#   -Si soit le volume/prix/entreprise n'est pas renseigne revoyer un message d'erreur
#   -Voir quelle grandeur de fenetre la mieux adaptee
'''
r.creerPartie('bot')
#r.rejoindrePartie(6455,'latermocdelo')
r.top()

global compteur_history
compteur_history =1


class fenetrebourse_tk(Tkinter.Tk):         #Creation d'une classe
    def __init__(self,parent):              #Def de parent : permet la hierarchisation des objets
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent                #Reference de notre parent
        self.initialize()

    def initialize(self):                   #initialisation interface graphique
        self.grid()                         #Layout managers : grid = grille => permet de placer les widgets dans des cases comme un tableur



        ############################### Frame tableau entreprises #######################################

        tableau_entreprises = Tkinter.Frame(self)
        tableau_entreprises.grid(column=0, row=7)

        label_fix_vendre = Tkinter.Label(tableau_entreprises, text="Vendre", bg='grey')
        label_fix_vendre.grid(column=0, row=3)
        label_fix_acheter = Tkinter.Label(tableau_entreprises, text="Acheter", bg='grey')
        label_fix_acheter.grid(column=0, row=4)

        label_fix_google = Tkinter.Label(tableau_entreprises, text="Google", bg='grey')
        label_fix_google.grid(column=1, row=0)

        label_fix_apple = Tkinter.Label(tableau_entreprises, text="Apple", bg='grey')
        label_fix_apple.grid(column=2, row=0)

        label_fix_facebook = Tkinter.Label(tableau_entreprises, text="Facebook", bg='grey')
        label_fix_facebook.grid(column=3, row=0)

        label_fix_trydea = Tkinter.Label(tableau_entreprises, text="Trydea", bg='grey')
        label_fix_trydea.grid(column=4, row=0)



        label_fix_ventes = Tkinter.Label(tableau_entreprises, text="liste ordre de ventes : ", bg='grey')
        label_fix_ventes.grid(column=0, row=2)

        label_fix_achats = Tkinter.Label(tableau_entreprises, text="liste ordre d'achats : ", anchor="w",bg='grey')
        label_fix_achats.grid(column=0, row=1)


        self.label_achats_var_google = Tkinter.StringVar()
        label_achats_google = Tkinter.Label(tableau_entreprises, textvariable=self.label_achats_var_google, anchor="w")
        label_achats_google.grid(column=1, row=1)

        self.label_ventes_var_google = Tkinter.StringVar()
        label_ventes_google = Tkinter.Label(tableau_entreprises, textvariable=self.label_ventes_var_google, anchor="w")
        label_ventes_google.grid(column=1, row=2)

        self.label_achats_var_apple = Tkinter.StringVar()
        label_achats_apple = Tkinter.Label(tableau_entreprises, textvariable=self.label_achats_var_apple, anchor="w")
        label_achats_apple.grid(column=2, row=1)

        self.label_ventes_var_apple = Tkinter.StringVar()
        label_ventes_apple = Tkinter.Label(tableau_entreprises, textvariable=self.label_ventes_var_apple, anchor="w")
        label_ventes_apple.grid(column=2, row=2)

        self.ventes()
        self.achats()






        #button

        button_vendre_google = Tkinter.Button(tableau_entreprises, text="vendre", command=self.vendre_google)
        button_vendre_google.grid(column=1, row=3)

        button_acheter_google = Tkinter.Button(tableau_entreprises, text="acheter", command=self.acheter_google)
        button_acheter_google.grid(column=1, row=4)


        button_vendre_apple = Tkinter.Button(tableau_entreprises, text="vendre", command=self.vendre_apple)
        button_vendre_apple.grid(column=2, row=3)

        button_acheter_apple = Tkinter.Button(tableau_entreprises, text="acheter", command=self.acheter_apple)
        button_acheter_apple.grid(column=2, row=4)





        ############################# SELF ###########################



        #entry

        self.entry_prix_var = Tkinter.StringVar()
        self.entry_prix = Tkinter.Entry(self, textvariable=self.entry_prix_var)    #creation du widget entry
        self.entry_prix.grid(column=0, row=1, sticky='EW') #placement du widget collone=0, ligne=0,  sticky -> si cellule sagrandi -> coller Gauche Droite (E W N S)
        self.entry_prix.bind('<Return>', self.OnPressEnter_prix)
        self.entry_prix.bind('<Button-1>', self.OnPressClick_prix)
        self.entry_prix_var.set("rentrer le prix")

        self.entry_volume_var = Tkinter.StringVar()
        self.entry_volume = Tkinter.Entry(self, textvariable=self.entry_volume_var)
        self.entry_volume.grid(column=1, row=1, sticky='EW')
        self.entry_volume.bind('<Return>', self.OnPressEnter_volume)
        self.entry_volume.bind('<Button-1>', self.OnPressClick_volume)
        self.entry_volume_var.set("rentrer le volume")


        #boutons

        button_ask = Tkinter.Button(self, text="Ordre d'achat", command=self.Ask_Click)    #creation bouton, lance la commande onbuttonclick
        button_ask.grid(column=3, row=0)                        #placement du bouton

        button_bid = Tkinter.Button(self, text="Odre de vente", command=self.Bid_Click)
        button_bid.grid(column=3, row=1)

        button_history = Tkinter.Button(self, text="Historique")
        button_history.bind(self,'<ButtonRelease-1>',lambda event: self.History_Click_Hide())
        button_history.bind(self,'<ButtonPress-1>',lambda event: self.History_Click())
        button_history.grid(column=3, row=3)

        button_valide_prix = Tkinter.Button(self, text="Valider", command=self.Valide_Prix_Click)
        button_valide_prix.grid(column=0, row=4, sticky='E')

        button_valide_volume = Tkinter.Button(self, text="Valider\n volume", command=self.Valide_Volume_Click)
        button_valide_volume.grid(column=1, row=3, sticky='E')

        button_cancel_operations = Tkinter.Button(self, text="Annuler\n operations", command=self.cancel_operations)
        button_cancel_operations.grid(column=3, row=2)
        '''
        button_refresh_ventes = Tkinter.Button(self, text="REFRESH VENTES", command=self.ventes)
        button_refresh_ventes.grid(column=1, row=5, sticky='W')

        button_refresh_achats = Tkinter.Button(self, text="REFRESH ACHATS", command=self.achats)
        button_refresh_achats.grid(column=1, row=5, sticky='E')

        button_refresh_operations = Tkinter.Button(self, text="REFRESH OPERATIONS", command=self.operation_en_cours)
        button_refresh_operations.grid(column=0, row=5, sticky='W')

        button_refresh_soldes = Tkinter.Button(self, text="REFRESH ALL", command=self.refresh_all)
        button_refresh_soldes.grid(column=0, row=0, sticky='E')
        '''



        #check
        self.nom_entreprise = Tkinter.StringVar()
        check_google = Tkinter.Radiobutton(self,text="Google", variable=self.nom_entreprise, value="Google", command=self.Choix_Entreprise)
        check_trydea = Tkinter.Radiobutton(self, text="Trydea", variable=self.nom_entreprise, value="Trydea", command=self.Choix_Entreprise)
        check_facebook = Tkinter.Radiobutton(self, text="Facebook", variable=self.nom_entreprise, value="Facebook", command=self.Choix_Entreprise)
        check_apple = Tkinter.Radiobutton(self, text="Apple", variable=self.nom_entreprise, value="Apple", command=self.Choix_Entreprise)
        check_google.grid(column=2, row=0)
        check_trydea.grid(column=2, row=1)
        check_facebook.grid(column=2, row=2)
        check_apple.grid(column=2, row=3)

        #curseurs
        self.curseur_prix_var = Tkinter.DoubleVar()
        curseur_prix= Tkinter.Scale(self, orient='horizontal',length=150,variable=self.curseur_prix_var)
        curseur_prix.grid(column=0, row=3, sticky='WN')
        self.curseur_volume_var = Tkinter.DoubleVar()
        curseur_volume = Tkinter.Scale(self,orient='horizontal',length=150, variable=self.curseur_volume_var)
        curseur_volume.grid(column=1, row=3, sticky='WN')




        #labels

        self.label_prix_var = Tkinter.StringVar()            #creation variable pour contenir une valeur (ici du texte)
        label_prix = Tkinter.Label(self, textvariable=self.label_prix_var, #lier variable au widget
                              anchor="w", fg="white", bg="blue")    #anchor="w" -> aligner a gauche; fg -> foreground; bg -> background
        label_prix.grid(column=0, row=2, sticky='EW')      #columnspan=2   -> "debourdement" de la colonne: ici -> colonne 0 et colonne 1

        self.label_solde_var = Tkinter.StringVar()
        label_solde = Tkinter.Label(self, textvariable=self.label_solde_var, anchor="w", fg="black", bg="yellow" )
        label_fix_solde = Tkinter.Label(self, text="solde : ", anchor="w", fg="black", bg="white")
        label_fix_solde.grid(column=0, row=0, sticky='W')
        label_solde.grid(column=1, row=0)
        self.after(1000,self.soldes())

        self.label_operation_en_cours_var = Tkinter.StringVar()
        label_fix_operation_en_cours = Tkinter.Label(self, text="operation en cours: ", anchor="w", fg="black", bg="white")
        label_fix_operation_en_cours.grid(column=0, row=6, sticky='W')
        label_operation_en_cours = Tkinter.Label(self, textvariable=self.label_operation_en_cours_var, anchor="w", fg="black",bg="white")
        label_operation_en_cours.grid(column=1, row=6, sticky='W')
        self.operation_en_cours()





        self.label_volume_var = Tkinter.IntVar()
        label_volume = Tkinter.Label(self, textvariable=self.label_volume_var, anchor="w", fg="white", bg="blue")
        label_volume.grid(column=1, row=2, sticky='EW')

        self.label_entreprise = Tkinter.StringVar()
        label_bid = Tkinter.Label(self, textvariable=self.label_entreprise, anchor="w", fg="white", bg="red")
        label_bid.grid(column=2, row=4, sticky='EW')



        self.label_history_var = Tkinter.StringVar()
        self.label_fix_history = Tkinter.Label(textvariable=self.label_history_var, anchor="w", fg="red", bg="white")
        #self.label_fix_history = Tkinter.Label(text="voici l'historique", anchor="w", fg="red", bg="white")
        self.label_fix_history.grid(column= 3,row=4)

        self.label_message_var =  Tkinter.StringVar()
        self.label_message = Tkinter.Label(textvariable=self.label_message_var, fg='white', bg='blue')
        self.label_message.grid(column=3, row=4)



        self.grid_columnconfigure(0, weight=1)              #redimensionnement automatique: ici juste colonne 0
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        #self.resizable(True, False)                         #empeche la fenetre d'etre redimensionnee verticalement
        #self.update()                                       #permet de figer la taille de la fenetre -> pas d'adaptation auto
        #self.geometry(self.geometry())

        self.refresh_all()


    #def click

    def Ask_Click(self):
        self.label_message_var.set("vous avez bien valide ask")
        r.ask(str(self.label_entreprise.get()), float(self.label_prix_var.get()), int(self.label_volume_var.get()))

    def Bid_Click(self):
        self.label_message_var.set("vous avez bien valide bid")
        r.bid(str(self.label_entreprise.get()), float(self.label_prix_var.get()), int(self.label_volume_var.get()))

    def History_Click(self):

        self.label_fix_history.grid(column=0, row=10)


    def History_Click_Hide(self):
        self.label_fix_history.grid_forget()


    def Valide_Prix_Click(self):
        self.label_prix_var.set(self.curseur_prix_var.get())


    def Valide_Volume_Click(self):
        self.label_volume_var.set(self.curseur_volume_var.get())


    #def Press Enter

    def OnPressEnter_prix(self, event):
        self.label_prix_var.set(self.entry_prix_var.get())
        self.entry_prix_var.set("rentrer le prix")

    def OnPressEnter_volume(self, event):
        self.label_volume_var.set(self.entry_volume_var.get())
        self.entry_volume_var.set("rentrer le volume")

    def OnPressClick_prix(self, event):
        self.entry_prix_var.set("")

    def OnPressClick_volume(self, event):
        self.entry_volume_var.set("")



    #others




    def Choix_Entreprise(self):
        self.label_entreprise.set(self.nom_entreprise.get())

    def soldes(self):
        self.label_solde_var.set(r.solde())

    def operation_en_cours(self):
        self.label_operation_en_cours_var.set(r.operationsEnCours())

    def achats(self):
        self.label_achats_var_google.set(r.achats('Google',0))
        self.label_achats_var_apple.set(r.achats('Apple',0))

    def ventes(self):
        self.label_ventes_var_google.set(r.ventes('Google',0))
        self.label_ventes_var_apple.set(r.ventes('Apple',0))

    def cancel_operations(self):
        cours=r.operationsEnCours()
        l = len(cours)
        for i in range(l):
            r.annulerOperation(cours[i])

    def refresh_all(self):
        self.soldes()
        self.operation_en_cours()
        self.achats()
        self.ventes()
        self.after(100,self.refresh_all)


############################ fonctions frame tableau entreprises ############################

    def acheter_google(self):
        print(r.ventes('Google'))
        print(type(r.ventes('Google')))
        r.ask('Google',r.ventes('Google')[1],r.ventes('Google')[2])

    def vendre_google(self):
        r.bid('Google',r.achats('Google')[1],r.achats('Google')[2])


    def acheter_apple(self):
        r.ask('Apple',r.ventes('Apple')[1],r.ventes('Apple')[2])

    def vendre_apple(self):
        r.bid('Apple',r.achats('Apple')[1],r.achats('Apple')[2])



if __name__ == "__main__":                  #Creation de notre main
    app = fenetrebourse_tk(None)            #Instance de notre classe fenetrebourse_tk mais on lui donne aucun parent (None) car premier element graphique
    app.title('Fenetre bourse')

    #app.style = Tkinter.ttk.Style()
    #app.style.theme_use('classic')
    app.mainloop()                          #"bouclage" : creation d'un boucle sans fin




