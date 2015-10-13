import utilitaires


def saveProf(con,nom,prenom):
	with con:
		con.execute("INSERT INTO profs(nomProf,prenomProf) VALUES(?,?)",(nom,prenom))
		print("$$$###@@@Sauvegarde reussi!!@@@###$$$")
		input()


def saveStud(con,nom,prenom):
	with con:
		con.execute("INSERT INTO etudiants(nomEtud,prenomEtud) VALUES(?,?)",(nom,prenom))
		print("$$$###@@@Sauvegarde reussi!!@@@###$$$")
		input()


def saveCour(con,nom,coef):
	with con:
		con.execute("INSERT INTO cours(nom,coeff) VALUES(?,?)",(nom,int(coef)))
		print("$$$###@@@Sauvegarde reussi!!@@@###$$$")
		input()


def saveClasse(con,nom):
	with con:
		con.execute("INSERT INTO classes(nomClasse) VALUES(?)",(nom,))
		print("$$$###@@@Sauvegarde reussi!!@@@###$$$")
		input()

