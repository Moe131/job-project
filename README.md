# Structure
```
├── docker-compose.yaml
├── dockerfile
├── jobs_project
│   ├── jobs_project
│   │   ├── __init__.py
│   │   ├── items.py
│   │   ├── middlewares.py
│   │   ├── pipelines.py
│   │   ├── settings.py
│   │   └── spiders
│   │   	├── __init__.py
│   │   	└── json_spider.py
│   └── scrapy.cfg
├── query.py
├── README.md
└── requirements.txt
└── data ├── s01.json
         └── s02.json
```

#  Follow these steps to run the project

1. Place the json files into **data** folder as show above
2. build docker images by running this command :
```
 docker-compose up --build
```
3. run the project using this command

```
 docker-compose up
```



#  A brief description of the pipeline process

For each entry in the jobs array retrieved from the json file a dictionary is created. A dictionary contains all the data for that specific job. Each job goes through the pipeline and it is inserted into Postgres **raw_table**. If for a job, the column does not exist in the table, it will be dynamically added to table. Furthermore, columns that include dates will be handled and inserted into database in timestamp with time zone data type. 
After all the jobs are inserted into the database, query.py will retrieve the data and organize them into a CSV file with data separated by comma. 



# A screenshot of how jobs can be sorted in database based on updated date :

![Screen Shot 2024-06-12 at 13 10 17](https://github.com/Moe131/job-project/assets/65834335/5b9c4142-2a37-4193-bded-ccd44363f98c)

# A screenshot jobs in the database:

![Screen Shot 2024-06-12 at 13 12 21](https://github.com/Moe131/job-project/assets/65834335/00b55b87-b2dd-4215-95f9-7c000f2ee20f)
