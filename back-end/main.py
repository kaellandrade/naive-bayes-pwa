import psycopg2


HOST = "indicapet.c6zoydxsvacn.us-east-1.rds.amazonaws.com"
DATABASE = "bd_petIndica"
USER = "gabrielbtera"
PASS = "biel1234"

class DataBaseQuerys:
    def __init__(self, host: str, database: str, user: str, password: str) -> None:
        self.host = host
        self.database = database
        self.user = user
        self.password = password
    
    def run_query(self, query):
        print('estabelecendo conexao...')
        conn = psycopg2.connect(
        host=self.host,
        database=self.database,
        user=self.user,
        password=self.password
        )

        cur = conn.cursor()
        cur.execute(query)
        results = cur.fetchall()

        conn.close()

        return results


dataQuery = DataBaseQuerys(HOST, DATABASE, USER, PASS)

result = dataQuery.run_query("SELECT * FROM petIndica.allData")

print(result)