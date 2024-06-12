import json
import scrapy
from jobProject.items import JobprojectItem

class JobSpider(scrapy.Spider):
    name = 'job_spider'
    custom_settings = {
    	'ITEM_PIPELINES': {
        		'jobProject.pipelines.SaveToPostgresql': 300,
    	},
	}
    
    def __init__(self, **kwargs):
        pass

    def start_requests(self):
        # your code here
        yield scrapy.Request(url='file:///project/data/s02.json', callback=self.parse_page)
        
    def parse_page(self, response):
        # Load JSON data from the response
        data = json.loads(response.text)
        item = JobprojectItem()
        # Loop over the jobs in the JSON data
        for job in data['jobs']:
            job_data = job['data']
            dict = {}
            for key in job_data.keys():
                dict[key] = job_data[key]
            item["data"] = dict;
            yield item