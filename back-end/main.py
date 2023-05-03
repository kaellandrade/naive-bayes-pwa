import psycopg2


print('estabelecendo conexao')
conn = psycopg2.connect(
    host="petindica.c6zoydxsvacn.us-east-1.rds.amazonaws.com",
    database="bd_petIndica",
    user="gabrielbtera",
    password=""
)

cur = conn.cursor()

cur.execute("SELECT * FROM petIndica.allData")

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()