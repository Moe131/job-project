# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
        

class SaveToPostgresql:

    def __init__(self):
        self.connection = psycopg2.connect(
            host = "localhost",
            user = "mohammadmirzaei",
            database = "jobProject",
            port ="5432",
        )
        self.cursor = self.connection.cursor()
        self.create_raw_table()


    def create_raw_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS raw_table (
                jobid SERIAL PRIMARY KEY,
                data TEXT
                );
        """)
        self.connection.commit() 
    
    def process_item(self, item, spider):
        self.cursor.execute("""
            INSERT INTO raw_table (data)
            VALUES (%s)
            RETURNING jobid;
        """, (str(item['data']),) )
        self.connection.commit()
        return item


    def __del__(self):
        """ close the connection to database on destrcutor of object"""
        self.connection.close()

