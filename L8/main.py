import sqlite3
conn = sqlite3.connect(r':memory:')
cur = conn.cursor()
cur.execute(""" CREATE TABLE IF NOT EXISTS Classes(
    class varchar(50) PRIMARY KEY NOT NULL,
    type varchar(2) NOT NULL,
    country varchar(20) NOT NULL,
    numGuns INT,
    bore REAL,
    displacement INT);
""")
conn.commit()
cur.execute(""" CREATE TABLE IF NOT EXISTS Ships(
    name varchar(50) PRIMARY KEY NOT NULL,
    class varchar(50) NOT NULL,
    launched SMALLINT);
""")
conn.commit()
cur.execute(""" CREATE TABLE IF NOT EXISTS Outcomes(
    ship varchar(50) PRIMARY KEY NOT NULL,
    battle varchar(20) NOT NULL,
    result varchar(10) NOT NULL);
""")
conn.commit()
cur.execute(""" CREATE TABLE IF NOT EXISTS Battles(
    name varchar(20) PRIMARY KEY NOT NULL,
    [date] datetime);
""")
conn.commit()

aclasses = [('c1', 'bb', 'russia', 7, 11, 1000),
           ('c2', 'bc', 'germany', 2, 12, 2000),
           ('c3', 'bb', 'USA', 3, 13, 3000)]
aships = [('s1', 'c1', 1901),
         ('s2', 'c1', 1902),
         ('s3', 'c1', 1903),
         ('s4', 'c2', 1904),
         ('s5', 'c2', 1905),
         ('s6', 'c2', 1906),
         ('s7', 'c3', 1907)]
aOutcomes = [('s1','Fourth World War','damaged'),
            ('s2','First World War','damaged'),
            ('s3','First World War','ok'),
            ('s4','Thirt World War', 'ok'),
            ('s5','Second World War', 'ok'),
            ('s6','Thirt World War', 'ok'),
            ('s7','Second World War', 'damaged')]
aBattles = [
    ('b1', '2005-01-01'),
    ('b2','2005-01-02'),
    ('b3','2005-01-03'),
    ('b4','2005-01-04')]

cur.executemany("INSERT INTO Classes VALUES(?, ?, ?, ?, ?, ?);", aclasses)
cur.executemany("INSERT INTO Ships VALUES(?, ?, ?);", aships)
cur.executemany("INSERT INTO Outcomes VALUES(?, ?, ?);", aOutcomes)
cur.executemany("INSERT INTO Battles VALUES(?, ?);", aBattles)
conn.commit()

cur.execute("""SELECT AVG(Classes.numGuns) FROM Ships JOIN Classes on Ships.class = Classes.class WHERE Classes.type = 'bb'""")
print(round(cur.fetchall()[0][0], 2))
