import sqlite3

conn = sqlite3.connect('play_stats.db')

c = conn.cursor()

c.execute('''CREATE TABLE stats
(title text, uuid text, type text)
''')

conn.commit()
conn.close()
