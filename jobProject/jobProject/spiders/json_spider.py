import json
import scrapy
from jobProject.items import JobprojectItem

class JobSpider(scrapy.Spider):
    name = 'job_spider'
    
    def __init__(self, **kwargs):
        pass

    def start_requests(self):
        # your code here
        yield scrapy.Request(url='file:///Users/mohammadmirzaei/Documents/UCI/Resumes/Projects/s02.json', callback=self.parse_page)
        
    def parse_page(self, response):
        # Load JSON data from the response
        data = json.loads(response.text)
        # Loop over the jobs in the JSON data
        for job in data['jobs']:
            job_data = job['data']
            item = {}
            for key in job_data.keys():
                item[key] = job_data[key]

            yield item