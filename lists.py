import utilitaires


def listProfs(con):
	cursor = utilitaires.getCursor(con)
	cursor.execute("SELECT * FROM profs")
	datas = cursor.fetchall()
	print("|    ID    |    NOM    |     PRENOM     |")
	for prf in datas:
		print("|    ",prf['id'],"    |","    ",prf['nomProf'],"    |","    ",prf['prenomProf'],"    |")


def listEtud(con):
	cursor = utilitaires.getCursor(con)
	cursor.execute("SELECT * FROM etudiants")
	datas = cursor.fetchall()
	print("|    ID    |    NOM    |     PRENOM     |")
	for prf in datas:
		print("|    ",prf['id'],"    |","    ",prf['nomEtud'],"    |","    ",prf['prenomEtud'],"    |")


def listCour(con):
	cursor = utilitaires.getCursor(con)
	cursor.execute("SELECT * FROM cours")
	datas = cursor.fetchall()
	print("|    ID    |    NOM    |     COEFFICIENT     |")
	for prf in datas:
		print("|    ",prf['id'],"    |","    ",prf['nom'],"    |","    ",prf['coeff'],"    |")


def listClasse(con):
	cursor = utilitaires.getCursor(con)
	cursor.execute("SELECT * FROM classes")
	datas = cursor.fetchall()
	print("|    ID    |    NOM    |")
	for prf in datas:
		print("|    ",prf['id'],"    |","    ",prf['nomClasse'],"    |")
