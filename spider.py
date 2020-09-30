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
    def boot():
        create_project_dir(Spider.project_name)
        create_project_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)


    # here the method we are going to create is going to add the links to the queue file and the base_url to the crawled file
    # i want this method to console what page it is crawling through
    # make sure you display something because if it is not showing anything then we might think that the program is freeze of something
    # this method basically goes to a link and gathers all the links in that page and put it in the queue, removes the base url from the queue and add it in the crawled
    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name+' now crawling '+page_url)
            print('Queue: '+str(len(Spider.queue))+' | Crawled: '+str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_link(page_url)) # add_links_to_queue ??? 
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()   #??


    # connecting to a website and getting back string is quite tricky here, it gets here as computer redable byte, and we need to convert it into human readable string
    @staticmethod
    def gather_link(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8')
                
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except:
            print('Error: Can\'t crawl page')
            return set()
        return finder.page_links()

    #this method is used in crawl_page method to add the links in queue
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
             #this means if thenewboston.com is in the link or not? otherwise it is going to crawl all the pages like facebook.com
            if Spider.domain_name not in url:    
                continue
            Spider.queue.add(url)

    #this method is used in crawl_page method at the end to update whatever is in the set to add it in the files
    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
