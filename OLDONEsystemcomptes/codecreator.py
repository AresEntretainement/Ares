import pickle

class Os:
	name = 'mon nom'
	def __init__(self):
		return

string = """
CREATE TABLE  IF NOT EXISTSUsers(
	ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	Pseudo TEXT,
	Password TEXT,
	Admin INT,
	Mail TEXT,
	Adress TEXT,
	Town TEXT,
	Poids INT,
	Taille INT,
	LevelBoxing TEXT,
	LevelAthletics INT
)

CREATE TABLE IF NOT EXISTS Trainings(
	ID INT,
	Training NULL,
	DateNow TEXT,
	GeneralPerfs TEXT,

)
"""
other = """
INSERT INTO Users(Pseudo, Password, Admin, Mail, Adress, Town, Poids, Taille, LevelBoxing, LevelAthletics) VALUES
('AresUser', 'ee11cbb19052e40b07aac0ca060c23ee', 0, 'user@ares.com', '16 Rue', 'Cholet', 80, 184, 'A', 10 )
'a730d90cda9087e96349ed94828d4bedd286150e7fb941bb026fad69be7233775ad0765ef9'
INSERT INTO Users(Pseudo, Password, Admin, Mail, Adress, Town, Poids, Taille, LevelBoxing, LevelAthletics) VALUES
('AresAdmin', '21232f297a57a5a743894a0e4a801fc3', 1, 'admin@ares.com', '16 Rue', 'Cholet', 81, 185, 'B', 5 )
'4284c31bf5f153a29a87fa16f6a2b538851865181c026e4b9993db83d3ee2c82b8c91e0111'
INSERT INTO Trainings(ID, Training, Date, GeneralPerfs) VALUES
(1, (?), '24-02-2018', '[]')
"""
d = Os()
chargedTrain = memoryview(pickle.dumps(d))
