import psycopg2
from itemadapter import ItemAdapter
from datetime import datetime


class SaveToPostgresql:

    def __init__(self):
        self.connection = psycopg2.connect(
            host="localhost",
            user="mohammadmirzaei",
            password="your_password",  # Replace with your actual password
            database="jobProject",
            port="5432",
        )
        self.cursor = self.connection.cursor()
        self.create_raw_table()  # Create the table if it doesn't exist

    def create_raw_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS raw_table (
                jobid SERIAL PRIMARY KEY
            );
        """)
        self.connection.commit()

    def update_table_columns(self, column): # Here if the column does not exist in database, add it to the table
        column_type = "TIMESTAMP WITH TIME ZONE" if "date" in column.lower() else "TEXT" # keeps the type of timestamp in database for entries that are date
        self.cursor.execute("""
            DO $$
            BEGIN
                IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name = 'raw_table' AND column_name = %s) THEN
                    EXECUTE 'ALTER TABLE raw_table ADD COLUMN ' || quote_ident(%s) || ' ' || %s;
                END IF;
            END $$;
        """, (column, column,column_type))
        self.connection.commit()

    def process_item(self, item, spider):
        data = item['data']
        item_keys = data.keys()
        # for each column in job item , if it does not exist in database it will update the database table
        for column in item_keys:
            self.update_table_columns(str(column))

        # Construct the sql insert statement 
        placeholders = ', '.join(['%s'] * len(item_keys))
        columns = ', '.join(item_keys)
        sql_query = f"INSERT INTO raw_table ({columns}) VALUES ({placeholders}) RETURNING jobid;"

        values = [str(data[key]) for key in item_keys]  # Ensure values are converted to string for insertion
        self.cursor.execute(sql_query, values)
        self.connection.commit()

        return item

    def __del__(self):
        """ Close the connection to database in the destructor """
        self.cursor.close()
        self.connection.close()

