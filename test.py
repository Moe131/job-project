import psycopg2

class SaveToPostgresql:
    def __init__(self):
        self.connection = psycopg2.connect(
            host = "localhost",
            user = "mohammadmirzaei",
            database = "jobProject",
            port ="5432",
        )
        self.cursor = self.connection.cursor()


    def create_raw_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS raw_table (
                jobid SERIAL PRIMARY KEY,
                data TEXT
                );
        """)
        self.connection.commit()
    

    def close_connection(self):
        self.connection.close()


if __name__ == "__main__":
    s = SaveToPostgresql()
    s.create_raw_table()
    s.close_connection()


