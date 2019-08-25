import sqlite3

conn = sqlite3.connect('members.sqlite')

c = conn.cursor()
c.execute('''
          DROP TABLE members
          ''')

conn.commit()
conn.close()
