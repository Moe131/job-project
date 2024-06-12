FROM python:3.11

WORKDIR /project

COPY requirements.txt ./

RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . /project

WORKDIR /project/jobProject

# Run Scrapy when the container launches
CMD scrapy crawl job_spider && python3 ../query.py

