import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://igorborisov:@localhost:5432/hw2')
connection = engine.connect()


def insert_art():
    names = ["Bob Dylan", "Элвис Пресли", "Чак Берри", "Джими Хендрикс", "Джеймс Браун", "Литл Ричард",
             "Боб Марли", "Eminem"]
    insert_art = f"insert into artist (name) values (%s)"
    for i in range(len(names)):
        connection.execute(insert_art, names[i])


def insert_alb():
    albums = [("Women in Music Pt. III", 2018), ("Folklore", 2008), ("Gaslighter", 2018), ("Fake it Flowers", 2019),
              ("What’s Your Pleasure?", 2020), ("My Punisher", 2019), ("A Hero’s Death", 2015),
              ("Roisin Machine", 2018)]
    insert = f"insert into album (name, year_date) values (%s, %s)"
    connection.execute(insert, albums)


def insert_gen():
    genres = ["Джаз", "Рок", "Поп", "Классика", "Хип-Хоп"]
    insert = f"insert into genre (name) values (%s)"
    for i in range(len(genres)):
        connection.execute(insert, genres[i])


def insert_tr():
    tracks = [("UFO Luv", 3.24, 1), ("Мы умрем", 2.33, 2), ("Косички", 3.50, 3), ("Tuesday", 2.48, 4),
              ("Poker Face", 2.46, 5), ("Broken Angel", 3.05, 6), ("Lovely", 2.58, 7), ("Love Song, Baby", 2.43, 8),
              ("Cake By The Ocean", 3.12, 1), ("Say It Right", 3.33, 2), ("Lose Yourself", 3.58, 3),
              ("Sexy Back", 2.59, 4), ("Watermelon Sugar", 3, 5), ("Ameno Dorime", 2.39, 6), ("Rockstar", 3.2, 7)]
    insert = f"insert into track (name, length, album_id) values (%s, %s, %s)"
    connection.execute(insert, tracks)


def insert_comp():
    compilations = [("Топ 100", 2020), ("Топ 50", 2021), ("Топ 20", 2019), ("Топ 10", 2020), ("Топ 5", 2022),
                    ("Топ 3", 2021), ("Топ 80", 2020), ("Топ 150", 2019)]
    insert = f"insert into compilation (name, year_date) values (%s, %s)"
    connection.execute(insert, compilations)


def insert_art_gen():
    art_gen = [(1, 1), (2, 1), (3, 2), (4, 3), (2, 4), (5, 5), (6, 3), (7, 4), (8, 2)]
    insert = f"insert into artistgenre (artist_id, genre_id) values (%s, %s)"
    connection.execute(insert, art_gen)


def insert_art_alb():
    art_alb = [(1, 2), (2, 3), (3, 1), (4, 5), (2, 3), (5, 6), (6, 6), (7, 8), (8, 4), (4, 7), (8, 2)]
    insert = f"insert into artistalbum (artist_id, album_id) values (%s, %s)"
    connection.execute(insert, art_alb)


def insert_tr_comp():
    tr_comp = [(15, 1), (14, 1), (13, 2), (12, 2), (11, 3), (10, 4), (9, 5), (8, 6), (7, 7), (6, 8), (5, 2), (15, 3),
               (14, 4), (13, 5)]
    insert = f"insert into trackcompilation (track_id, compilation_id) values (%s, %s)"
    connection.execute(insert, tr_comp)


insert_art()
insert_alb()
insert_gen()
insert_tr()
insert_comp()
insert_art_alb()
insert_art_gen()
insert_tr_comp()
