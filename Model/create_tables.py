import sqlite3

conn = sqlite3.connect('members.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE members
          (member_id INTEGER PRIMARY KEY ASC, 
           f_name VARCHAR(250)NOT NULL,
           l_name VARCHAR(250) NOT NULL,
           phone VARCHAR(20)  NOT NULL ,
           address VARCHAR(100)  NOT NULL,
           type VARCHAR (20) NOT NULL,
           manager_position VARCHAR(50),
           jersey_number VARCHAR(50),
          hourly_wage INTEGER ,
          player_position VARCHAR(50),
           salary INTEGER
           )
          ''')

conn.commit()
conn.close()