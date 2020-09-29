from urllib.request import urlopen
from link_finder import LinkFinder
from general import *

class Spider:
    # all the spider needs to see the variables
    # if it is inside __init__ then each spider is going to have a new instance of the variable
    # that is why we are creating the class variable
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):      #i think this is the constructor as in java
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = project_name + '/queue.txt'
        Spider.crawled_file = project_name + '/crawled.txt'     #here we are assigning the class variables with the initial values
        self.boot()     #????
        self.crawl_page('First spider', Spider.base_url)    #???

    # at first one spider has only the home page and once it crawls through the home page to find all the links 
    # we are not running multiple spiders at first because it would be pointless as it is only one page
    # once the first spider gathers multiple links thats when we are going to assign to multiple spiders
    # whenever you use class method then you use class variable 
    # you can also make method without using class variable
    @staticmethod
    def boot(self):
        create_project_dir(Spider.project_name)
        create_project_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)


    # here the method we are going to create is going to add the links to the queue file and the base_url to the crawled file
    # i want this method to console what page it is crawling through
    # make sure you display something because if it is not showing anything then we might think that the program is freeze of something
    @staticmethod
    def crawl_page():

    

        