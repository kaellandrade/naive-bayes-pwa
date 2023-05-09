import psycopg2


HOST = "indicapet.c6zoydxsvacn.us-east-1.rds.amazonaws.com"
DATABASE = "bd_petIndica"
USER = "gabrielbtera"
PASS = "biel1234"

#host: str, database: str, user: str, password: str
class DataBaseCore:
    def __init__(self) -> None:
        self.host = HOST
        self.database = DATABASE
        self.user = USER
        self.password = PASS
    
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


# dataQuery = DataBaseCore()

# result = dataQuery.run_query("SELECT * FROM petIndica.allData")

# print(result)