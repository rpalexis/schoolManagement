import sqlite3

def connection(dbName):
	dbName+=".db"
	try:
		open(dbName,'r+')
		con = sqlite3.connect(dbName)
		print("Connection a la base  : "+dbName+" reussie")
		print("----->Activation des clefs etrangeres")
		con.execute("PRAGMA foreign_keys = ON")#Enable foreing keys utilies in Sqlite
		return con
	except Exception:
	 	print("Creation d'une nouvelle base de type ECOLE ::: "+dbName)
	 	con = sqlite3.connect(dbName)
	 	print("Creation des tables")
	 	with con:
	 		print("----->Activation des clefs etrangeres")
	 		con.execute("PRAGMA foreign_keys = ON")#Enable foreing keys utilies in Sqlite
	 		print("----->Table Professeurs")
	 		con.execute('CREATE TABLE profs(id INTEGER PRIMARY KEY,nomProf TEXT, prenomProf TEXT)')# CREATION DE LA TABLE
	 		print("----->Table Etudiants")
	 		con.execute('CREATE TABLE etudiants(id INTEGER PRIMARY KEY,nomEtud TEXT, prenomEtud TEXT)')# CREATION DE LA TABLE
	 		print("----->Table Classes")
	 		con.execute('CREATE TABLE classes(id INTEGER PRIMARY KEY,nomClasse TEXT)')# CREATION DE LA TABLE
	 		print("----->Table Cours")
	 		con.execute('CREATE TABLE cours(id INTEGER PRIMARY KEY,nom TEXT, coeff INTEGER)')# CREATION DE LA TABLE
	 		print("Creation des tables a dependance")
	 		con.execute('CREATE TABLE prof_cours(id INTEGER PRIMARY KEY,prof_id INTEGER, cours_id INTEGER, FOREIGN KEY(prof_id) REFERENCES profs(id), FOREIGN KEY(cours_id) REFERENCES cours(id))')# CREATION DE LA TABLE
	 		con.execute('CREATE TABLE etud_cla(id INTEGER PRIMARY KEY,etud_id INTEGER, clas_id INTEGER, FOREIGN KEY(etud_id) REFERENCES etudiants(id), FOREIGN KEY(clas_id) REFERENCES classes(id))')# CREATION DE LA TABLE
	 		con.execute('CREATE TABLE etud_cours(id INTEGER PRIMARY KEY,etud_id INTEGER, cours_id INTEGER, FOREIGN KEY(etud_id) REFERENCES etudiants(id), FOREIGN KEY(cours_id) REFERENCES cours(id))')# CREATION DE LA TABLE
	 		print(dbName+" a ete cree avec succes!!@@")
	 		return con


def getCursor(con):
	con.row_factory = sqlite3.Row
	return con.cursor()


def menu():
	print("----->>> 1 Pour INSERER")
	print("----->>> 2 Pour AFFICHER")
	print("----->>> 3 Pour SUPPRIMER")
	print("----->>> 0 Pour QUITTER")

def menuInsertion():
	print("###-->>>> 1 Pour ENREGISTRER un Professeur")
	print("###-->>>> 2 Pour INSCRIR un Etudiant")
	print("###-->>>> 3 Pour AJOUTER un Cour")
	print("###-->>>> 4 Pour OUVRIR une Classe")
	print("###-->>>> 5 Pour REMPLIR une Classe")
	print("###-->>>> 6 Pour ASSIGNER un professeur a un Cour")
	print("###-->>>> 7 Pour AJOUTER un  Cour pour un etudiant")
	print("###-->>>> 0 Pour pour retourner au MENU PRINCIPAL")


def menuAffichage():
	print("###-->>>> 1 Pour LISTER les Professeurs")
	print("###-->>>> 2 Pour LISTER les Etudiants")
	print("###-->>>> 3 Pour LISTER les Cours")
	print("###-->>>> 4 Pour LISTER les Classes")
	print("###-->>>> 5 Pour LISTER les cours dispenser par M. X")
	print("###-->>>> 6 Pour LISTER les cours suivi par Etudiant X")
	print("###-->>>> 7 Pour LISTER les etudiants de la Salle X")
	print("###-->>>> 0 Pour pour retourner au MENU PRINCIPAL")


def menuSuppression():
	print("###-->>>> 1 Pour SUPPRIMER un/plusieurs Professeurs")
	print("###-->>>> 2 Pour SUPPRIMER un/plusieurs Etudiants")
	print("###-->>>> 3 Pour SUPPRIMER un/plusieurs Cours")
	print("###-->>>> 4 Pour SUPPRIMER une/plusieurs Classes")
	print("###-->>>> 5 Pour SUPPRIMER les cours dispenser par M. X")
	print("###-->>>> 6 Pour SUPPRIMER les cours suivi par Etudiant X")
	print("###-->>>> 7 Pour SUPPRIMER les etudiants de la Salle X")
	print("###-->>>> 0 Pour pour retourner au MENU PRINCIPAL")