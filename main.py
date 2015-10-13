import os
import utilitaires
import save
import lists
import suppr


print("Entrez le nom de la base a utilise")
print("---->S'il n'existe pas elle va etre cree")

connect = utilitaires.connection(input())
print("------>>>Pressez la touche ENTER, pour continuer")
input()
while True:
	os.system("cls" if os.name == "nt" else "clear")
	utilitaires.menu()
	slct = int(input())
	if slct == 1:
		#Debut Espace des Enregistrements
		os.system("cls" if os.name == "nt" else "clear")
		utilitaires.menuInsertion()
		inSlct = int(input())
		if inSlct == 1:
			os.system("cls" if os.name == "nt" else "clear")
			print("###-->>>Entrer le nom du professeurs")
			nom = input()
			print("###-->>>Entrer le prenom du professeurs")
			prenom = input()
			save.saveProf(connect,nom,prenom)
			os.system("cls" if os.name == "nt" else "clear")
		elif inSlct == 2:
			os.system("cls" if os.name == "nt" else "clear")
			print("###-->>>Entrer le nom de l'etudiant")
			nom = input()
			print("###-->>>Entrer le prenom de l'etudiant")
			prenom = input()
			save.saveStud(connect,nom,prenom)
			os.system("cls" if os.name == "nt" else "clear")
		elif inSlct == 3:
			os.system("cls" if os.name == "nt" else "clear")
			print("###-->>>Entrer le nom du cour")
			nom = input()
			print("###-->>>Entrer la NOTATION du cour")
			coeff = input()
			save.saveCour(connect,nom,coeff)
			os.system("cls" if os.name == "nt" else "clear")
		elif inSlct == 4:
			os.system("cls" if os.name == "nt" else "clear")
			print("###-->>>Entrer le nom de la classe")
			nom = input()
			save.saveClasse(connect,nom)
			os.system("cls" if os.name == "nt" else "clear")
		elif inSlct == 5:
			print("Veuillez Acheter la version PRO pour utiliser ce service")
			input()
		elif inSlct == 6:
			print("Veuillez Acheter la version PRO pour utiliser ce service")
			input()
		elif inSlct == 7:
			print("Veuillez Acheter la version PRO pour utiliser ce service")
			input()
		elif inSlct == 0:
			print("fin")
	elif slct ==2:
		os.system("cls" if os.name == "nt" else "clear")
		utilitaires.menuAffichage()
		inSlct = int(input())
		#gestion des affichages
		if inSlct == 1:
			lists.listProfs(connect)
			input()
		elif inSlct == 2:
			lists.listEtud(connect)
			input()
		elif inSlct == 3:
			lists.listCour(connect)
			input()
		elif inSlct == 4:
			lists.listClasse(connect)
			input()
		elif inSlct == 5:
			print("Veuillez Acheter la version PRO pour utiliser ce service")
			input()
		elif inSlct == 6:
			print("Veuillez Acheter la version PRO pour utiliser ce service")
			input()
		elif inSlct == 7:
			print("Veuillez Acheter la version PRO pour utiliser ce service")
			input()
		elif inSlct == 0:
			print("FIn")
	elif slct == 3:
		os.system("cls" if os.name=="nt" else "clear")
		utilitaires.menuSuppression()
		inSlct = int(input())
		#gestion des affichages
		if inSlct == 1:
			lists.listProfs(connect)
			print("====>Entrer un ou plusieurs numero de professeurs<====")
			slection = []
			acc = '0'
			while acc != '-':
				acc = input()
				if acc == '-':
					break
				else:
					slection.append(int(acc))
				print("Appuiyez sur (-) pour terminer")
			suppr.supprProfs(connect,slection)
			print("Professeurs Supprimees")

		elif inSlct == 2:
			lists.listEtud(connect)
			print("====>Entrer un ou plusieurs numero d'etudiants<====")
			slection = []
			acc = '0'
			while acc != '-':
				acc = input()
				if acc == '-':
					break
				else:
					slection.append(int(acc))
				print("Appuiyez sur (-) pour terminer")
			suppr.supprEtud(connect,slection)
			print("Etudiants Supprimees")
			input()
		elif inSlct == 3:
			lists.listCour(connect)
			print("====>Entrer un ou plusieurs numero de cours<====")
			slection = []
			acc = '0'
			while acc != '-':
				acc = input()
				if acc == '-':
					break
				else:
					slection.append(int(acc))
				print("Appuiyez sur (-) pour terminer")
			suppr.supprCour(connect,slection)
			print("Cours Supprimees")
			input()
		elif inSlct == 4:
			lists.listClasse(connect)
			print("====>Entrer un ou plusieurs numero de classe<====")
			slection = []
			acc = '0'
			while acc != '-':
				acc = input()
				if acc == '-':
					break
				else:
					slection.append(int(acc))
				print("Appuiyez sur (-) pour terminer")
			suppr.supprClasse(connect,slection)
			print("Classe(s) Supprimees")
			input()
		elif inSlct == 5:
			print("Veuillez Acheter la version PRO pour utiliser ce service")
			input()
		elif inSlct == 6:
			print("Veuillez Acheter la version PRO pour utiliser ce service")
			input()
		elif inSlct == 7:
			print("Veuillez Acheter la version PRO pour utiliser ce service")
			input()
		elif inSlct == 0:
			print("FIn")
		input()
	elif slct == 0:
		os.system("cls" if os.name=="nt" else "clear")
		print("Le programme est ferme")
		break
