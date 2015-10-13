import utilitaires


def supprProfs(con,ids):
	with con:
		for i in ids:
			con.execute("DELETE FROM profs WHERE id = "+str(i))

def supprEtud(con,ids):
	with con:
		for i in ids:
			con.execute("DELETE FROM etudiants WHERE id = "+str(i))


def supprCour(con,ids):
	with con:
		for i in ids:
			con.execute("DELETE FROM cours WHERE id = "+str(i))


def supprClasse(con,ids):
	with con:
		for i in ids:
			con.execute("DELETE FROM classes WHERE id = "+str(i))
