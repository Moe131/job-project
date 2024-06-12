import psycopg2
import csv

class PostgresqlQuery:
    def __init__(self):
        """ Establish a connection to postgreSQL"""
        self.connection = psycopg2.connect(
            host="localhost",
            user="mohammadmirzaei",
            password="your_password",  # Replace with your actual password
            database="jobProject",
            port="5432",
        )
        self.cursor = self.connection.cursor()


    def query_data(self):
        """ Run a query to get the data in the database table raw_table"""
        self.cursor.execute("""
            SELECT * FROM raw_table;
        """)
        return self.cursor.fetchall()
 

    def query_column_names(self):
        """ Run a query to get the column names in the database table raw_table"""
        # Querying column names from information_schema.columns
        self.cursor.execute("""
            SELECT column_name FROM information_schema.columns WHERE table_name = 'raw_table';
        """)
        return self.cursor.fetchall()


    def __del__(self):
        self.connection.close()

def createCSV(database, file_name):
    columns= [tup[0] for tup in database.query_column_names()]
    data = database.query_data()
    with open(file_name, 'w') as f:
        csv_writer = csv.writer(f, delimiter=',')
        csv_writer.writerow(columns)
        for line in data:
            csv_writer.writerow(line)


if __name__ == "__main__":
    database = PostgresqlQuery()
    createCSV(database, "data.csv")

