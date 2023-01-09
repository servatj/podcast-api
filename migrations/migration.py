import sqlite3

# Conectamos a la base de datos 
conn = sqlite3.connect('podcasts.db')

# Creamos la tabla
columns = [
    "id INTEGER PRIMARY KEY",
    "title VARCHAR UNIQUE",
    "publisher VARCHAR",
    "link_url VARCHAR",
    "genre VARCHAR",
    "release_date DATETIME",
    "created_date DATETIME",
    "modified_date DATETIME",
]

create_table_cmd = f"CREATE TABLE podcast ({','.join(columns)})"
conn.execute(create_table_cmd)
conn.commit()

# Insertamos registros
podcasts = [
    "1, 'The Daily', 'The New York Times', 'https://www.nytimes.com/column/the-daily', 'News',' 2022-10-08 09:15:10', '2022-10-08 09:15:10', '2022-10-08 09:15:10'",
    "2, 'Divance Show', 'divance', 'https://www.divance.app', 'Techy','2022-10-08 09:15:10', '2022-10-08 09:15:10', '2022-10-08 09:15:10'",
]

for podcast_data in podcasts:
    insert_cmd = f"INSERT INTO person VALUES ({podcast_data})"
conn.execute(insert_cmd)
conn.commit()
