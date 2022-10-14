
import sqlite3

# Connection a la DB
db = 'etud.db'
conn = sqlite3.connect(db)
connection = conn.cursor()

##############################################################################################


class GestionNote:
    def create_table_student(self):
        connection.execute('CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT NOT NULL, adress TEXT NOT NULL)')
        conn.commit()

        # Creation des la tables matiere
    def create_table_matiere(self):
        connection.execute(
            'CREATE TABLE IF NOT EXISTS matiere (id INTEGER PRIMARY KEY AUTOINCREMENT,libelle TEXT NOT NULL, nom_etud TEXT NOT NULL, note REAL NOT NULL)')
        conn.commit()

        # Insertion d'un étudiant
    def insert_student(self, name, adress):
        self.nom = name
        self.adress = adress
        connection.execute(
            'INSERT INTO student (nom, adress) VALUES(?,?)', (self.nom, self.adress))
        conn.commit()

        # Insertion d'une matiere
    def insert_matiere(self, libelle, name, note):
        self.libelle = libelle
        self.nom = name
        self.note = note
        if self.nom != '':
            connection.execute(
                'SELECT * FROM student WHERE nom =?;', (self.nom,))
            val = connection.fetchone()
        if val == None:
            print('etudiant introuble')
            exit()
        else:
            connection.execute('INSERT INTO matiere (libelle,nom_etud,note) VALUES(?,?,?)',
            (self.libelle, self.nom, self.note))
            conn.commit()

        # Recuperer un etudiant par son nom
    def get_student_by_nom(self, name):
        self.name = name
        connection.execute(
            'SELECT nom, adress FROM student WHERE nom =?;', (self.name,))
        val = connection.fetchone()
        if val == None:
            print('etudiant introuble')
            exit()
        else:
            for i in val:
                print(i)

        # Recuperer un etudiant par s
    def get_note_by_student(self, name):
        self.name = name
        connection.execute('SELECT note FROM matiere WHERE nom_etud =?;', (self.name,))
        val = connection.fetchone()
        if val == None:
            print('etudiant introuble')
            exit()
        else:
            for i in val:
                print(i)

        # Mise à jour d'un etudiant
    def update_student_adress(self, name, adress):
        self.name = name
        self.adress = adress
        with conn:
            connection.execute('UPDATE student SET adress = :adress WHERE nom = :nom',
            {'nom': self.name, 'adress': self.adress})
        conn.commit()

        # Mise à jour de note etudiant
    def update_student_note(self, name, note):  # update
        self.name = name
        self.note = note
        with conn:
            connection.execute('UPDATE matiere SET note = :note WHERE nom_etud = :nom',
            {'nom': self.name, 'note': self.note})
            conn.commit()

        # calcul de la moyenne
    def calcul_moyenne_by_student_matiere(self, name, libelle):
        self.nom = name
        self.libelle = libelle
        connection.execute('SELECT count(*) FROM matiere WHERE nom_etud =? AND libelle =?;', (self.nom, self.libelle,))
        nbre_libelle = connection.fetchone()
        connection.execute('SELECT SUM(note) AS note_total FROM matiere WHERE nom_etud =? AND libelle =?;', (self.nom, self.libelle,))
        val = connection.fetchone()
        moyenne = val[0]/nbre_libelle[0]
        print(f'moyenne: {moyenne}')

        # Liste des etudiant
    def list_student_grade(self, libelle):
        self.libelle = libelle
        connection.execute('SELECT nom, adress, note FROM student INNER JOIN matiere ON student.nom = matiere.nom_etud WHERE libelle =?;', (self.libelle,))
        val = connection.fetchall()
        for i, y in enumerate(val):
            print(i, y)

            gestion_note = gestion_note()
            gestion_note.create_table_student()
            gestion_note.create_table_matiere()

            monChoix = 0
            operation = {
                1: 'Ajouter un nouveau etudiant',
                2: 'Rechercher un etudiant',
                3: 'Modifier inforlation etudiant',
                4: 'Ajouter une matiere',
                5: 'rechercher une note etudiant',
                6: 'Modifier note de l etudiant',
                7: 'Calculer la moyenne des notes etudiant',
                8: 'liste des notes etudiant',
                9: 'quitter'
            }

        for i, val in operation.items():
            print(i, val)
            monChoix = int(input('Faites un choix:'))
            while (monChoix) != 0:

                # Ajout d'un nouveau etudiant
                if monChoix == 1:
                    name = input('Entrez le nom de l etudiant:')
                if name == '':
                    print('Saisir vide \n')
                    break
                adress = input('Entrez adresse etudiant:')
                if adress == '':
                    print('Saisir vide \n')
                    break
                    gestion_note.insert_student(name, adress)

            # Rechercher un etudiant
                elif monChoix == 2:
                    name = input('Entrez le nom etudiant:')
                    if name == '':
                        print('Saisir vide \n')
                        break
                    gestion_note.get_student_by_nom(name)

                    # Modification d'adresse d'un étudiant
                elif monChoix == 3:
                    name = input('Entrez le nom etudiant:')
                    if name == '':
                        print('Saisir vide \n')
                        break
                    adress = input('Entrez adresse etudiant:')
                    if adress == '':
                        print('saisir vide \n')
                        break
                    gestion_note.update_student_adress(name, adress)

                # Ajouter une matiere
                elif monChoix == 4:
                    libelle = input('Entrez le libelle de la matière:')
                    if libelle == '':
                        print('Saisir vide \n')
                        break
                    name = input('Entrez le nom etudiant:')
                    if name == '':
                        print('Saisir vide \n')
                        break
                    note = float(input('Entrez sa note:'))
                    if note == '':
                        print('saisir vide \n')
                        break
                    gestion_note.insert_matiere(libelle, name, note)

                # rechercher la note d'un etudiant
                elif monChoix == 5:
                    name = input('Entrez le nom etudiant:')
                    if name == '':
                        print('Saisir vide \n')
                        break
                    gestion_note.get_note_by_student(name)

                # Sodification d'une note étudiant
                elif monChoix == 6:
                    name = input('Entrez le nom etudiant:')
                    if name == '':
                        print('Saisir vide \n')
                        break
                    note = float(input('Entrez la note etudiant:'))
                    if note == '':
                        print('saisir vide \n')
                        break
                    gestion_note.update_student_note(name, note)

                # Calcul moyenne étudiant
                elif monChoix == 7:
                    name = input('Entrez le nom etudiant:')
                    if name == '':
                        print('Saisir vide \n')
                        break
                    libelle = input('Entrez le libelle de la matière:')
                    if libelle == '':
                        print('Saisir vide \n')
                        break
                    gestion_note.calcul_moyenne_by_student_matiere(name, libelle)

                # Liste des notes etudiant
                elif monChoix == 8:
                    libelle = input('Entrez le libelle de la matière:')
                    if libelle == '':
                        print('Saisir vide \n')
                        break
                    gestion_note.list_student_grade(libelle)
